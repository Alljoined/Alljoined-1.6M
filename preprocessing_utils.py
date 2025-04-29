import inspect
import os
import pickle
import sys
import warnings

import mne
import numpy as np
import pandas as pd
import scipy
from joblib import Parallel, delayed
from sklearn.discriminant_analysis import _cov
from tqdm.auto import tqdm

SESSIONS = list(range(1, 5))


def warn(msg):
    frame = inspect.currentframe().f_back
    file = os.path.basename(frame.f_code.co_filename)
    line = frame.f_lineno
    print(f"\033[31mWarning: {msg} [{file}:{line}]\033[0m")


def read_eeg_data(data_dir, contains="", verbose=False):
    """
    This function reads the EDF files in the specified blocks and
    restricts the data to using the recommended method.

    Args:
        data_dir: The directory containing the EDF files.
        contains: The string to search for in the file names.
        verbose: The verbose flag.

    Returns:
        The raw EEG data.
    """
    edf_file = None

    for item in os.listdir(os.path.join(data_dir)):
        if item.endswith(".raw.fif") and contains in item:
            edf_file = os.path.join(data_dir, item)
            break

    if edf_file is None:
        for item in os.listdir(os.path.join(data_dir)):
            if item.endswith(".edf") and contains in item:
                edf_file = os.path.join(data_dir, item)
                break

    with warnings.catch_warnings(record=True) as w:
        if edf_file.endswith(".edf"):
            raw = mne.io.read_raw_edf(edf_file, preload=True, verbose=False)
        else:
            raw = mne.io.read_raw_fif(edf_file, preload=True, verbose=False)
        if w and verbose:
            print(
                f"Loading EDF File {edf_file}: {w[0].message}", file=sys.stderr
            )

    if "Afz" in raw.info["ch_names"]:
        raw.rename_channels({"Afz": "AFz"})
    eeg_channels = get_electrode_channels(raw)
    raw.pick(eeg_channels)

    montage = mne.channels.make_standard_montage("standard_1020")
    raw.set_montage(montage)

    return raw


def get_electrode_channels(raw):
    """
    This function checks the electrode channels being used for this EEG experiment.

    Args:
        raw: The concatenated raw EEG data from all 16 blocks.

    Returns:
        channels): The list of electrode channels that are selected for analysis.
    """

    channels = raw.ch_names
    # Filter out the bad prefix channels
    bad_prefix = [
        "TimestampS",
        "TimestampMs",
        "OrTimestampS",
        "OrTimestampMs",
        "Counter",
        "Interpolated",
        "RawCq",
        "Battery",
        "BatteryPercent",
        "FwBufferSize",
        "FwClockTime",
        "MarkerHardware",
        "HighBitFlex",
        "SaturationFlag",
        "CQ",
        "EQ",
        "MOT",
    ]
    channels = [
        ch
        for ch in channels
        if not any([ch.startswith(prefix) for prefix in bad_prefix])
    ]
    return channels


def epoching(
    sub,
    blocks,
    project_dir,
    baseline=(None, 0),
    tmin=-0.2,
    tmax=1,
    sfreq=256,
    l_freq=None,
    h_freq=None,
    notch_freqs=None,
    reject=None,
    verbose=False,
):
    """
    This function first converts the EEG data to MNE raw format, and
    performs channel selection, epoching, baseline correction and frequency
    downsampling.

    Args:
        sub: The subject number.
        project_dir: The project directory.
        baseline: The baseline correction.
        tmin: The start time of the epoch.
        tmax: The end time of the epoch.
        sfreq: The sampling frequency.
        l_freq: The low frequency cutoff for the bandpass filter.
        h_freq: The high frequency cutoff for the bandpass filter.
        notch_freqs: The notch filter frequencies.
        reject: The rejection thresholds for the EEG data.
            If None, then no rejection is performed.
            If a dictionary is given, then the keys are the channel names
            and the values are the rejection thresholds.
        test_train_split: The block number that test blocks end, if None, only
            training data is returned.
        verbose: The verbose flag.

    Returns
        epoched_tests: epoched EEG data (trials, channels, time points),
            for each session.
        epoched_trains: same as epoched_test, but for training data.
        ch_names: EEG channel names.
        times: EEG time points.
    """
    print("Epoching...")

    assert sfreq >= 250, "Sampling frequency should be at least 250 Hz"

    # Use joblib to parallelize session processing
    # list of epoched_train or list of (epoched_test, epoched_train)
    epoched_datas = Parallel(n_jobs=-1)(
        delayed(_process_session)(
            sub,
            s,
            blocks,
            project_dir,
            baseline=baseline,
            tmin=tmin,
            tmax=tmax,
            sfreq=sfreq,
            l_freq=l_freq,
            h_freq=h_freq,
            notch_freqs=notch_freqs,
            reject=reject,
            verbose=verbose,
        )
        for s in SESSIONS
    )

    return epoched_datas


def compute_stim_order(sub, epochs, metadata, verbose=False):
    """
    Reconstructs the stimulus order for a given subject from EEG epochs and
    metadata.

    This function extracts stimulus trigger information from annotations in EEG
    epochs and uses it to build a DataFrame containing metadata entries for
    each trial. It filters out non-oddball trials and appends relevant session
    and dataset information.

    Args:
        sub: Subject identifier.
        epochs: A list of EEG epoch objects, each containing annotations.
        metadata: DataFrame containing metadata for all stimuli, indexed by
            trigger value.
        verbose: If True, enables verbose output. Defaults to False.

    Returns:
        pd.DataFrame: A DataFrame containing the reconstructed trial metadata,
        including session, dataset, subject, and image path information.
    """

    dfs = []
    for s in SESSIONS:
        events = epochs[s - 1].events
        code_to_desc = {v: k for k, v in epochs[s - 1].event_id.items()}
        trigger_values = np.array(
            [int(code_to_desc[x].split(",")[3]) for x in events[:, 2]]
        )

        df = []
        # Inherits the category information
        for t in trigger_values:
            if t < 99999:  # Otherwise oddball
                df.append(metadata.iloc[t])
        df = pd.DataFrame(df)
        df["dataset"] = "Alljoined-1.6M"
        df["session"] = s
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)

    # Reorganize filepath columns
    df = df.drop(columns=["fname"]).rename(columns={"filepath": "image_path"})
    df["subject"] = sub
    print(f"Recreated {len(df)} trials from raw EEG data")
    return df


def compute_whitening_matrix(
    mvnn_dim,
    epoched_datas,
    stim_order,
    verbose=False,
):
    """
    Compute the covariance matrices of the EEG data (calculated for each
    time-point or epoch/repetitions of each image condition), and then average
    them across image conditions and data partitions. The inverse of the
    resulting averaged covariance matrix is used to whiten the EEG data
    (independently for each session).

    Args:
        mvnn_dim: The dimension to compute the covariance matrices.
        epoched_datas: The epoched EEG data.
        stim_order: The stimulus order.
        sessions: The list of sessions to compute the whitening matrices.
            if None, it is inferred from the epoched data.
        verbose: The verbose flag.

    Returns:
        whitening_mats: The whitening matrices.
    """

    print("Computing whitening matrices...")

    ### Loop across data collection sessions ###
    whitening_mats = []
    for i in tqdm(SESSIONS, desc="Sessions", unit="sess"):
        part_metadata = stim_order[(stim_order["session"] == i)].reset_index(
            drop=True
        )
        session_data = epoched_datas[i - 1].get_data()
        # Image conditions covariance matrix of shape:
        # Image conditions × EEG channels × EEG channels
        if mvnn_dim == "time":
            only_one_trial = (
                part_metadata.groupby("image_path")
                .filter(lambda x: len(x) == 1)
                .reset_index(drop=True)["image_index"]
                .tolist()
            )
            if len(only_one_trial) > 0 and verbose:
                warn(
                    f"{len(only_one_trial)} Image conditions with only one"
                    " trial"
                )
        sigma_cond = np.array(
            Parallel(n_jobs=-1)(
                delayed(_compute_sigma_cond)(
                    mvnn_dim, session_data[group.index]
                )
                for _, group in tqdm(
                    part_metadata.groupby("image_path"),
                    desc="Image conditions",
                    unit="img",
                    leave=False,
                )
            )
        )
        # Average the covariance matrices across image conditions
        sigma_tot = sigma_cond.mean(axis=0)
        whitening_mats.append(
            scipy.linalg.fractional_matrix_power(sigma_tot, -0.5)
        )

    return whitening_mats


def whiten(epoched_datas, whitening_matrices):
    """
    Apply the computed whitening matrices to each session of epoched EEG data.

    Args:
        epoched_datas: List of mne.Epochs objects for each session.
        whitening_matrices: List of whitening matrices corresponding to each session.

    Returns:
        List of whitened mne.Epochs objects.
    """
    for i in range(len(epoched_datas)):
        data = epoched_datas[i].get_data()
        data = whitening_matrices[i] @ data
        epoched_datas[i]._data = data
    return epoched_datas


def save_data(
    output_file,
    datas,
    verbose=False,
):
    """
    Merge the EEG data of all sessions together, shuffle the EEG repetitions
    across sessions and reshaping the data to the format:
    Image conditions x EEG repetitions x EEG channels x EEG time points.
    Then, the data of both test and training EEG partitions is saved.

    Args:
        output_file: The output file.
        datas: The whitened EEG data.
        no_merge: The flag to not merge the data across sessions.
        verbose: The verbose flag.
    """

    output_dir = os.path.dirname(output_file)

    # Saving directories
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if output_file.endswith(".pkl"):
        # Dump just the session wise mne.Epoch object
        with open(output_file, "wb") as f:
            pickle.dump(datas, f, protocol=pickle.HIGHEST_PROTOCOL)
        print(f"Saved preprocessed data to {output_file}")
        return

    ### Merge and save the data ###
    # Data matrix of shape:
    # trials × EEG channels × EEG time points
    sfreq = datas[0].info["sfreq"]
    start = int(sfreq) // 5
    end = start + 250
    epoched_data = [x.get_data()[..., start:end] for x in datas]
    merged_data = np.concatenate(epoched_data, axis=0)
    ch_names = datas[0].info["ch_names"]
    times = datas[0].times
    # Shuffle the repetitions of different sessions
    # Insert the data into a dictionary
    train_dict = {
        "preprocessed_eeg_data": merged_data,
        "ch_names": ch_names,
        "times": times,
    }
    # Dump the data that can be used for model training
    with open(output_file, "wb") as f:
        pickle.dump(train_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Saved preprocessed data to {output_file}")


# Epoch the given session
def _process_session(
    sub,
    sess,
    blocks,
    project_dir,
    baseline=(None, 0),
    tmin=-0.2,
    tmax=1,
    sfreq=256,
    l_freq=None,
    h_freq=None,
    notch_freqs=None,
    reject=None,
    verbose=False,
):

    # Load the EEG data
    data_dir = os.path.join(
        project_dir,
        "raw_eeg",
        "Alljoined-1.6M",
        f"sub-{sub:02d}",
        f"session_{sess:02d}",
    )
    raws = [
        read_eeg_data(
            os.path.join(data_dir, f"block_{index:02d}"), verbose=verbose
        )
        for index in blocks
    ]

    # Make event names unique
    for i in range(len(blocks)):
        a = raws[i].annotations

        # Highpass lowpass
        if l_freq != None or h_freq != None:
            raws[i].filter(l_freq=l_freq, h_freq=h_freq, verbose=verbose)

        # Notch filter
        if notch_freqs != None:
            raws[i].notch_filter(notch_freqs, verbose=verbose)

        raws[i].set_annotations(
            mne.Annotations(
                onset=a.onset,
                duration=a.duration,
                description=[
                    f"session_{sess},block_{i+1},{x}" for x in a.description
                ],
                orig_time=a.orig_time,
            )
        )

    raws = mne.concatenate_raws(raws)

    events, event_id = mne.events_from_annotations(
        raws,
        regexp=".*stim",
        verbose=False,
    )

    ### Epoching, baseline correction and resampling ###
    epochs = mne.Epochs(
        raws,
        events,
        event_id=event_id,
        tmin=tmin,
        tmax=tmax,
        baseline=baseline,
        preload=True,
        reject=reject,
        event_repeated="drop",
        verbose=verbose,
    )

    # Resampling IF sfreq is not 256, which is hardcoded but shouldn't be!
    # TODO: we should have a class that determines which hardware we're using
    # and the sfreq it collects
    if sfreq != 256:
        epochs.resample(sfreq, verbose=verbose)

    return epochs


def _compute_sigma_cond(mvnn_dim, cond_data):
    """
    This function computes the average covariance matrix of a specific
    image condition, over all timestamps.
    """

    # Compute covariace matrices at each time point, and then
    # average across time points

    if mvnn_dim not in ["time", "epochs"]:
        raise ValueError(
            f"mvnn_dim should be either 'time' or 'epochs', got {mvnn_dim}"
        )

    cond_data = cond_data - np.mean(cond_data, axis=0, keepdims=True)

    with warnings.catch_warnings(record=True):
        if mvnn_dim == "time":
            return np.mean(
                [
                    _cov(cond_data[:, :, t], shrinkage="auto")
                    for t in range(cond_data.shape[2])
                ],
                axis=0,
            )
        # Compute covariace matrices at each epoch (EEG repetition),
        # and then average across epochs/repetitions
        elif mvnn_dim == "epochs":
            return np.mean(
                [
                    _cov(
                        np.transpose(cond_data[e]),
                        shrinkage="auto",
                    )
                    for e in range(cond_data.shape[0])
                ],
                axis=0,
            )
