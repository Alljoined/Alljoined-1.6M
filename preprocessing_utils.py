import argparse
import dataclasses
import inspect
import os
import pickle
import sys
import warnings
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import mne
import numpy as np
import pandas as pd
import scipy
from joblib import Parallel, delayed
from sklearn.discriminant_analysis import _cov
from tqdm.auto import tqdm

###############################################################################
# CONFIGURATION
###############################################################################


@dataclass
class Configs:
    """Container for all preprocessing hyper-parameters.

    Attributes:
        baseline (Tuple[Optional[float], float]):
            Two-tuple ``(tmin, tmax)`` in **seconds** passed to
            :class:`mne.Epochs` for baseline correction. ``tmin`` can be
            ``None`` to use the first data sample.
        tmin (float):
            Start of the epoch (s) relative to the trigger.
        tmax (float):
            End of the epoch (s) relative to the trigger.
        sfreq (int):
            Target sampling frequency *after* resampling (Hz). Must be ≥ 250.
        l_freq (Optional[float]):
            Low cut-off for band-pass filter (Hz). ``None`` disables the low
            edge.
        h_freq (Optional[float]):
            High cut-off for band-pass filter (Hz). ``None`` disables the high
            edge.
        notch_freqs (Optional[List[float]]):
            Frequencies (Hz) for a notch filter. ``None`` disables notch
            filtering.
        mvnn_dim (str):
            Multivariate noise-normalisation mode: ``"epochs"``, ``"time"`` or
            ``"off"``.
        reject (Optional[Dict[str, float]]):
            Peak-to-peak rejection thresholds (volts) per channel name.
            ``None`` disables automatic rejection.
        verbose (bool):
            Whether to print extra information during preprocessing.
    """

    baseline: Tuple[Optional[float], float] = (None, 0)
    tmin: float = -0.2
    tmax: float = 1.0
    sfreq: int = 250
    l_freq: Optional[float] = None
    h_freq: Optional[float] = None
    notch_freqs: Optional[List[float]] = None
    mvnn_dim: str = "epochs"
    reject: Optional[Dict[str, float]] = None
    verbose: bool = False


DEFAULT_CONFIGS = Configs()
SESSIONS = list(range(1, 5))

###############################################################################
# HELPER FUNCTIONS
###############################################################################


def _warn(msg: str) -> None:
    """Emit a red-colored warning with filename and line context.

    Args:
        msg (str): Human-readable message to display.
    """
    frame = inspect.currentframe().f_back
    file = os.path.basename(frame.f_code.co_filename)
    line = frame.f_lineno
    print(f"\033[31mWarning: {msg} [{file}:{line}]\033[0m", file=sys.stderr)


def read_eeg_data(data_dir: str, contains: str = "", verbose: bool = False):
    """Load a single EEG recording block.

    The function loads an EDF file in a specific directory. There should be
    only 1 EDF file present in the directory specified.

    Args:
        data_dir (str): Directory that **contains** the EDF file.
        contains (str, optional): Sub-string that must be present in the file
            name (e.g. to distinguish *stim* vs. *rest* recordings).
            Defaults to "".
        verbose (bool, optional): If ``True`` prints any warnings emitted by
            :pymod:`mne` during file reading. Defaults to ``False``.

    Returns:
        mne.io.BaseRaw: Raw object restricted to EEG channels only.

    Raises:
        FileNotFoundError: If no matching EDF file is found.
    """
    edf_file = None
    for fname in os.listdir(data_dir):
        if fname.endswith(".edf") and contains in fname:
            edf_file = os.path.join(data_dir, fname)
            break
    if edf_file is None:
        raise FileNotFoundError(f"No EDF file found in {data_dir!r}.")

    with warnings.catch_warnings(record=True) as w:
        if edf_file.endswith(".edf"):
            raw = mne.io.read_raw_edf(edf_file, preload=True, verbose=False)
        else:
            raw = mne.io.read_raw_fif(edf_file, preload=True, verbose=False)
        if w and verbose:
            print(f"Loading {edf_file}: {w[0].message}")

    # Fix mis-capitalisation by EMOTIV
    if "Afz" in raw.info["ch_names"]:
        raw.rename_channels({"Afz": "AFz"})

    raw.pick(_get_electrode_channels(raw))
    raw.set_montage(mne.channels.make_standard_montage("standard_1020"))
    return raw


def _get_electrode_channels(raw) -> List[str]:
    """Return genuine EEG channel names (drop markers, battery, etc.)."""
    # fmt: off
    bad_prefixes = {
        "TimestampS", "TimestampMs", "OrTimestampS", "OrTimestampMs",
        "Counter", "Interpolated", "RawCq", "Battery", "BatteryPercent",
        "FwBufferSize", "FwClockTime", "MarkerHardware", "HighBitFlex",
        "SaturationFlag", "CQ", "EQ", "MOT",
    }
    # fmt: on
    return [
        ch
        for ch in raw.ch_names
        if not any(ch.startswith(p) for p in bad_prefixes)
    ]


def _compute_sigma_cond(mvnn_dim: str, cond_data: np.ndarray) -> np.ndarray:
    """Compute a condition-specific covariance matrix and average it.

    Args:
        mvnn_dim (str): ``"epochs"`` or ``"time"`` — decides the covariance
            computation axis.
        cond_data (np.ndarray): Data array of shape
            ``(trials, channels, time)`` for one image condition.

    Returns:
        np.ndarray: The mean covariance matrix for the given condition
        (shape ``[n_channels, n_channels]``).

    """
    if mvnn_dim not in {"time", "epochs"}:
        raise ValueError(
            f"mvnn_dim must be 'time' or 'epochs', got {mvnn_dim}"
        )

    # Demean across epochs to avoid bias from absolute potential shifts
    cond_data = cond_data - cond_data.mean(axis=0, keepdims=True)

    if mvnn_dim == "time":
        # One covariance matrix per time point: (epochs × channels)
        covs = [
            _cov(cond_data[:, :, t], shrinkage="auto")
            for t in range(cond_data.shape[2])
        ]
    else:  # 'epochs'
        # One covariance matrix per epoch: (time × channels)
        covs = [
            _cov(cond_data[e].T, shrinkage="auto")
            for e in range(cond_data.shape[0])
        ]

    return np.mean(covs, axis=0)


###############################################################################
# CORE PIPELINE
###############################################################################


def epoching(
    sub: int,
    blocks,
    project_dir: str,
    configs: Configs = DEFAULT_CONFIGS,
    verbose: bool = False,
):
    """Epoch and filter EEG data for a given subject.

    Args:
        sub (int): Subject identifier (1-based; *not* zero-padded).
        blocks (Iterable[int]): Block indices **within** a session (1-based).
        project_dir (str): Base directory containing
            ``raw_eeg/Alljoined-1.6M``.
        configs (Configs, optional): Pre-processing configuration.
            Defaults to ``DEFAULT_CONFIGS``.
        verbose (bool, optional): Forwarded to low-level MNE functions.
            Defaults to ``False``.

    Returns:
        list[mne.Epochs]: One Epochs object per recording session.

    Raises:
        ValueError: If ``configs.sfreq`` is lower than 250 Hz.
    """
    if configs.sfreq < 250:
        raise ValueError("Sampling frequency must be at least 250 Hz.")

    def _process_session(sess: int):
        """Helper that loads and epochs a single session."""
        data_dir = os.path.join(
            project_dir,
            "raw_eeg",
            "Alljoined-1.6M",
            f"sub-{sub:02d}",
            f"session_{sess:02d}",
        )
        raws = [
            read_eeg_data(
                os.path.join(data_dir, f"block_{idx:02d}"), verbose=verbose
            )
            for idx in blocks
        ]

        # Filter and make annotation descriptions unique
        for b_idx, raw in enumerate(raws, start=1):
            a = raw.annotations
            if configs.l_freq is not None or configs.h_freq is not None:
                raw.filter(configs.l_freq, configs.h_freq, verbose=verbose)
            if configs.notch_freqs is not None:
                raw.notch_filter(configs.notch_freqs, verbose=verbose)
            raw.set_annotations(
                mne.Annotations(
                    onset=a.onset,
                    duration=a.duration,
                    description=[
                        f"session_{sess},block_{b_idx},{d}"
                        for d in a.description
                    ],
                    orig_time=a.orig_time,
                )
            )

        raw_concat = mne.concatenate_raws(raws)
        events, event_id = mne.events_from_annotations(
            raw_concat, regexp=".*stim", verbose=False
        )

        epochs = mne.Epochs(
            raw_concat,
            events,
            event_id=event_id,
            tmin=configs.tmin,
            tmax=configs.tmax,
            baseline=configs.baseline,
            preload=True,
            reject=configs.reject,
            event_repeated="drop",
            verbose=verbose,
        )
        if epochs.info["sfreq"] != configs.sfreq:
            epochs.resample(configs.sfreq, verbose=verbose)
        return epochs

    print("Epoching...")
    return Parallel(n_jobs=-1)(delayed(_process_session)(s) for s in SESSIONS)


def compute_dropped_trials(
    epochs: List[mne.Epochs],
    stim_order: pd.DataFrame,
    verbose: bool = False,
) -> np.ndarray:
    """Return indices of trials that have a *matching* trigger in the EEG.

    For each session we treat the recorded trigger values as a subsequence that
    should appear (in order) within *stim_order*.  Any rows of *stim_order*
    that are skipped constitute *dropped trials*.

    Args:
        epochs (list[mne.Epochs]): One :class:`mne.Epochs` object per session.
        stim_order (pd.DataFrame): Stimulus-order metadata for **all** sessions.
        verbose (bool, optional): If ``True``, print warnings about dropped
            triggers. Defaults to ``False``.

    Returns:
        np.ndarray: A 1-D array of row indices (into ``stim_order``) that
        survived all trigger-matching checks across sessions.
    """
    print("Computing dropped trials...")
    kept_indices: List[int] = []
    for sess in SESSIONS:
        ev = epochs[sess - 1].events
        code_to_desc = {v: k for k, v in epochs[sess - 1].event_id.items()}
        trigger_vals = np.array(
            [int(code_to_desc[e].split(",")[3]) for e in ev[:, 2]]
        )

        session_df = stim_order[stim_order["session"] == sess].copy()
        session_df["image_idx"] = (
            session_df["image_path"].str[-9:-4].astype(int)
        )
        img_idx_arr = session_df["image_idx"].to_numpy()

        indices: List[int] = []
        ptr = 0  # pointer into img_idx_arr
        for val in trigger_vals:
            while ptr < len(img_idx_arr) and img_idx_arr[ptr] != val:
                ptr += 1
            if ptr == len(img_idx_arr):
                raise ValueError(
                    f"Session {sess}: trigger sequence is not a subsequence of"
                    " stim_order."
                )
            indices.append(session_df.index[ptr])
            ptr += 1

        n_dropped = len(img_idx_arr) - len(indices)
        if verbose and n_dropped:
            _warn(f"{n_dropped} triggers dropped in session {sess}")

        kept_indices.extend(indices)
    return np.array(kept_indices)


def compute_whitening_matrix(
    mvnn_dim: str,
    epoched_datas: List[mne.Epochs],
    stim_order: pd.DataFrame,
    verbose: bool = False,
) -> List[np.ndarray]:
    """Compute MVNN whitening matrices session-wise.

    Args:
        mvnn_dim (str): Dimension along which to compute covariance
            (``"epochs"`` or ``"time"``).
        epoched_datas (list[mne.Epochs]): Epoched EEG data for every session.
        stim_order (pd.DataFrame): Metadata used to group trials by image.
        verbose (bool, optional): If ``True``, emit informative warnings.
            Defaults to ``False``.

    Returns:
        list[np.ndarray]: One whitening matrix (shape
        ``[n_channels, n_channels]``) per session in ``SESSIONS`` order.
    """
    print("Computing whitening matrices...")
    whitening_mats: List[np.ndarray] = []
    for sess in tqdm(SESSIONS, desc="Sessions", unit="sess"):
        part_meta = stim_order[stim_order["session"] == sess].reset_index(
            drop=True
        )
        data = epoched_datas[sess - 1].get_data()

        if mvnn_dim == "time":
            single_trial_imgs = part_meta.groupby("image_path").filter(
                lambda g: len(g) == 1
            )
            if not single_trial_imgs.empty and verbose:
                _warn(
                    f"{len(single_trial_imgs)} image conditions with only one"
                    f" trial in session {sess}"
                )

        sigma_cond = np.array(
            Parallel(n_jobs=-1)(
                delayed(_compute_sigma_cond)(mvnn_dim, data[g.index])
                for _, g in tqdm(
                    part_meta.groupby("image_path"),
                    desc="Images",
                    unit="img",
                    leave=False,
                )
            )
        )
        sigma_tot = sigma_cond.mean(axis=0)
        whitening_mats.append(
            scipy.linalg.fractional_matrix_power(sigma_tot, -0.5)
        )
    return whitening_mats


def whiten(
    epoched_datas: List[mne.Epochs], whitening_matrices: List[np.ndarray]
) -> List[mne.Epochs]:
    """Apply MVNN whitening matrices in-place and return the modified list.

    Args:
        epoched_datas (list[mne.Epochs]): Data to be whitened (modified in-place).
        whitening_matrices (list[np.ndarray]): One pre-computed whitening
            matrix per session.
    Returns:
        list[mne.Epochs]: The same list as ``epoched_datas`` but with each
        dataset's ``_data`` array replaced by its whitened version.

    """
    for i, epochs in enumerate(epoched_datas):
        epochs._data = whitening_matrices[i] @ epochs.get_data()
    return epoched_datas


def save_data(
    output_file: str,
    datas: List[mne.Epochs],
    configs: Configs,
    verbose: bool = False,
):
    """Persist pre-processed data to *output_file*.

    If *output_file* ends with ``.pkl`` the list of Epochs is pickled directly.
    Otherwise a flat NumPy array is saved (also pickled) together with channel
    names, times and the serialised ``Configs``.

    Args:
        output_file (str): Path where the NumPy/Pickle file will be written.
        datas (list[mne.Epochs]): Whitened, epoched EEG data (one per session).
        configs (Configs): The exact configuration object used to create the
            data (pickled alongside the output).
        verbose (bool, optional): Print extra status messages when ``True``.
            Defaults to ``False``.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    if output_file.suffix == ".pkl":
        with open(output_file, "wb") as f:
            pickle.dump(datas, f, protocol=pickle.HIGHEST_PROTOCOL)
        if verbose:
            print(f"Saved session-wise Epochs to {output_file}")
        return

    sfreq = datas[0].info["sfreq"]
    start = int(sfreq) // 5  # 0.2 s offset
    end = start + 250  # 1 s window at 250 Hz

    merged = np.concatenate(
        [x.get_data()[..., start:end] for x in datas], axis=0
    )
    export_dict = {
        "preprocessed_eeg_data": merged,
        "configs": dataclasses.asdict(configs),
        "ch_names": datas[0].info["ch_names"],
        "times": datas[0].times[start:end],
    }
    with open(output_file, "wb") as f:
        pickle.dump(export_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
    if verbose:
        print(f"Saved flat data to {output_file}")
