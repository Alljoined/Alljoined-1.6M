import argparse
import json
import os
import pickle
from pathlib import Path
from typing import Tuple, Dict

import mne
import pandas as pd

from preprocessing_utils import (
    Configs,
    compute_dropped_trials,
    compute_whitening_matrix,
    epoching,
    save_data,
    whiten,
)

# --------------------------------------------------------------------------
# helpers ------------------------------------------------------------------
# --------------------------------------------------------------------------


def _parse_float_tuple(text: str) -> Tuple[float | None, float]:
    """Parse 'None,0' or '-0.2,0' → (None, 0.0) or (-0.2, 0.0)."""
    a, b = [x.strip() for x in text.split(",")]
    return (None if a.lower() == "none" else float(a), float(b))


def _parse_reject(text: str) -> Dict[str, float]:
    """
    Parse JSON or 'EEG001:1e-4,EEG002:1.2e-4' → {'EEG001': 1e-4, 'EEG002': 1.2e-4}
    """
    if text.lstrip().startswith("{"):
        return json.loads(text)
    out: Dict[str, float] = {}
    for pair in text.split(","):
        ch, thr = pair.split(":")
        out[ch.strip()] = float(thr)
    return out


def _mvnn_arg(text: str) -> str | None:
    """Return 'epochs', 'time', or None (for the string 'none')."""
    t = text.lower()
    if t == "none":
        return None
    if t in {"epochs", "time"}:
        return t
    raise argparse.ArgumentTypeError(
        "mvnn_dim must be 'epochs', 'time', or 'None'"
    )


def _make_configs_from_args(args: argparse.Namespace) -> Configs:
    """Instantiate a Configs object from parsed CLI args."""
    return Configs(
        baseline=args.baseline,
        tmin=args.tmin,
        tmax=args.tmax,
        sfreq=args.sfreq,
        l_freq=args.l_freq,
        h_freq=args.h_freq,
        notch_freqs=args.notch_freqs,
        mvnn_dim=args.mvnn_dim,
        reject=args.reject,
    )


# --------------------------------------------------------------------------
# CLI ----------------------------------------------------------------------
# --------------------------------------------------------------------------

parser = argparse.ArgumentParser(
    prog="preprocessing.py",
    description=(
        "Preprocess EEG data for a specific subject: epoching, filtering, "
        "MVNN, and saving."
    ),
)

# required
parser.add_argument(
    "-s",
    "--sub",
    required=True,
    type=int,
    help="Subject number (e.g.  1 for sub-01)",
)

# Configs-related ----------------------------------------------------------
parser.add_argument(
    "--tmin",
    type=float,
    default=-0.2,
    help="Epoch start (seconds, default -0.2)",
)
parser.add_argument(
    "--tmax", type=float, default=1.0, help="Epoch end (seconds, default 1.0)"
)
parser.add_argument(
    "--baseline",
    type=_parse_float_tuple,
    default="None,0",
    help=(
        'Baseline tuple "None,0" or "-0.2,0" (use None for '
        "no pre-stim baseline)"
    ),
)
parser.add_argument(
    "--sfreq",
    type=int,
    default=250,
    help="Target sampling rate after downsampling (Hz)",
)
parser.add_argument(
    "--l_freq", type=float, help="Low cutoff for band-pass filter (Hz)"
)
parser.add_argument(
    "--h_freq", type=float, help="High cutoff for band-pass filter (Hz)"
)
parser.add_argument(
    "--notch_freqs",
    nargs="+",
    type=float,
    help="One or more notch filter frequencies (Hz)",
)
parser.add_argument(
    "--reject",
    type=_parse_reject,
    help=(
        'Artifact-rejection dict; JSON or "CH1:thr,CH2:thr" '
        '(mV, e.g. "EEG001:1e-4").'
    ),
)
parser.add_argument(
    "--mvnn_dim",
    type=_mvnn_arg,
    default="epochs",
    help="MVNN mode (off to skip whitening)",
)

# misc ---------------------------------------------------------------------
parser.add_argument(
    "--project_dir",
    default="/srv/eeg_reconstruction/shared/data/",
    help="Root of the project directory tree",
)
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output during preprocessing",
)

ARGS = parser.parse_args()

# --------------------------------------------------------------------------
# main ---------------------------------------------------------------------
# --------------------------------------------------------------------------

mne.set_log_level("WARNING" if not ARGS.verbose else "INFO")

PROJECT_DIR = Path(ARGS.project_dir)
SUB = ARGS.sub
CONFIGS = _make_configs_from_args(ARGS)

OUTPUT_DIR = (
    PROJECT_DIR / "preprocessed_data" / "Alljoined-1.6M" / f"sub-{SUB:02d}"
)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

stim_order = pd.read_parquet(OUTPUT_DIR / "stim_order.parquet")

# ---- subject-specific fix (trigger swap) ---------------------------------
if SUB == 6:
    print("Swapping mismatched triggers for subject 6")
    row_to_move = stim_order.iloc[73762]
    stim_order = pd.concat(
        [
            stim_order.drop(index=73762).iloc[:73760],
            row_to_move.to_frame().T,
            stim_order.drop(index=73762).iloc[73760:],
        ]
    )

# --------------------------------------------------------------------------
# epoching -----------------------------------------------------------------
TEST_BLOCKS: range = range(1, 5)
TRAIN_BLOCKS: range = range(5, 20)

epoched_test = epoching(
    SUB, TEST_BLOCKS, PROJECT_DIR, configs=CONFIGS, verbose=ARGS.verbose
)
epoched_train = epoching(
    SUB, TRAIN_BLOCKS, PROJECT_DIR, configs=CONFIGS, verbose=ARGS.verbose
)

# dropped-trial bookkeeping -------------------------------------------------
test_df = stim_order.query("partition == 'stim_test'")
train_df = stim_order.query("partition == 'stim_train'")

test_keep = compute_dropped_trials(epoched_test, test_df, verbose=ARGS.verbose)
train_keep = compute_dropped_trials(
    epoched_train, train_df, verbose=ARGS.verbose
)


stim_order["dropped"] = True
stim_order.loc[test_keep, "dropped"] = False
stim_order.loc[train_keep, "dropped"] = False
stim_order.to_parquet(OUTPUT_DIR / "experiment_metadata.parquet")

# --------------------------------------------------------------------------
# MVNN whitening -----------------------------------------------------------
if CONFIGS.mvnn_dim is not None:
    whitening_mats = compute_whitening_matrix(
        CONFIGS.mvnn_dim,
        epoched_train,
        stim_order.query("partition == 'stim_train'"),
        verbose=ARGS.verbose,
    )
    epoched_train = whiten(epoched_train, whitening_mats)
    epoched_test = whiten(epoched_test, whitening_mats)

    with open(OUTPUT_DIR / "mvnn_whitening_matrices.pkl", "wb") as f:
        pickle.dump(whitening_mats, f)

# --------------------------------------------------------------------------
# save ---------------------------------------------------------------------
save_data(
    OUTPUT_DIR / "preprocessed_eeg_test_flat.npy",
    epoched_test,
    CONFIGS,
    verbose=ARGS.verbose,
)
save_data(
    OUTPUT_DIR / "preprocessed_eeg_training_flat.npy",
    epoched_train,
    CONFIGS,
    verbose=ARGS.verbose,
)
