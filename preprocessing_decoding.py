import argparse
import itertools
import json
import os
import pickle
from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd
from mne.decoding import CSP
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.svm import LinearSVC
from mne.decoding import CSP

from all_categories import get_categories
from lda_utils import prep_decoding_data_hierarchical, run_LDA
from preprocessing_utils import Configs, compute_dropped_trials, epoching

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


def _make_configs_from_ARGS(ARGS: argparse.Namespace) -> Configs:
    """Instantiate a Configs object from parsed CLI ARGS."""
    return Configs(
        baseline=ARGS.baseline,
        tmin=ARGS.tmin,
        tmax=ARGS.tmax,
        sfreq=ARGS.sfreq,
        l_freq=ARGS.l_freq,
        h_freq=ARGS.h_freq,
        notch_freqs=ARGS.notch_freqs,
        mvnn_dim=ARGS.mvnn_dim,
        reject=ARGS.reject,
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

parser.add_argument(
    "--dataset",
    type=str,
    default="Alljoined-1.6M",
    help="selected dataset to run script",
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

parser.add_argument("--suffix", default="", type=str)

parser.add_argument("--cat1", default="animals", type=str)
parser.add_argument("--cat2", default="foods_and_plants", type=str)

ARGS = parser.parse_args()

# --------------------------------------------------------------------------
# main ---------------------------------------------------------------------
# --------------------------------------------------------------------------

mne.set_log_level("WARNING" if not ARGS.verbose else "INFO")

PROJECT_DIR = Path(ARGS.project_dir)
SUB = ARGS.sub
dataset = ARGS.dataset
CONFIGS = _make_configs_from_ARGS(ARGS)


OUTPUT_DIR = (
    PROJECT_DIR / "preprocessed_data" / "Alljoined-1.6M" / f"sub-{SUB:02d}"
)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

cat1 = ARGS.cat1
cat2 = ARGS.cat2

test_data_path = os.path.join(
    ARGS.project_dir, "preprocessed_data", ARGS.dataset, f"sub-{ARGS.sub:02d}", f"preprocessed_eeg_test_flat.npy"
)

train_data_path = os.path.join(
    ARGS.project_dir, "preprocessed_data", ARGS.dataset, f"sub-{ARGS.sub:02d}", f"preprocessed_eeg_training_flat.npy"
)

meta_path = os.path.join(
    ARGS.project_dir, "preprocessed_data", ARGS.dataset, f"sub-{ARGS.sub:02d}", f"experiment_metadata.parquet"
)

# Load data
epoched_test = np.load(test_data_path, allow_pickle = True)  # shape: (n_trials, n_channels, n_times)
epoched_train = np.load(train_data_path, allow_pickle = True)  # shape: (n_trials, n_channels, n_times)

stim_order = pd.read_parquet(meta_path)


train_df = stim_order[
    (stim_order["partition"] == "stim_train") & ~stim_order["dropped"]
].reset_index(drop=True)

test_df = stim_order[
    (stim_order["partition"] == "stim_test") & ~stim_order["dropped"]
].reset_index(drop=True)

print(len(test_df))

print(epoched_test['preprocessed_eeg_data'].shape)

# df = df[df['partition'] == f"stim_{ARGS.dataset_split}"]

# Classifier pipeline
flatten = FunctionTransformer(lambda x: x.reshape(x.shape[0], -1) if x.ndim > 2 else x)

categories_lib = get_categories()

category_pairs = itertools.combinations(categories_lib, 2)

# Create CSP + LDA pipeline
csp = CSP(n_components=4, reg=None, log=None, transform_into="csp_space")
lda = LinearDiscriminantAnalysis()

flatten = FunctionTransformer(
    lambda x: x.reshape(x.shape[0], -1) if x.ndim > 2 else x, validate=True
)

clf = Pipeline(
    [
        # ('CSP', csp),
        ("flatten", flatten),
        ("LDA", lda),
    ]
)

clf = Pipeline([
    ('flatten', flatten),
    ('LDA', lda)
])

classifier = clf

epoched_test = epoched_test['preprocessed_eeg_data']
epoched_train = epoched_train['preprocessed_eeg_data']


def run_cat_pairs(
    sub,
    merged_train,
    merged_test,
    cat1,
    cat2,
    train_df,
    test_df,
    categories_lib,
    classifier,
    dataset = ""
):
    types = f"{cat1}, {cat2}"
    # if dataset == "Alljoined-1.6M":
    #     dataset = ""

    train_A, train_B, test_A, test_B = prep_decoding_data_hierarchical(
        merged_train,
        merged_test,
        [cat1],
        [cat2],
        train_df,
        test_df,
        categories_lib
    )
    if train_A.shape[0] == 0:
        raise ValueError(f"No train data for category: {cat1}")
    if train_B.shape[0] == 0:
        raise ValueError(f"No train data for category: {cat2}")
    if test_A.shape[0] == 0:
        raise ValueError(f"No test data for category: {cat1}")
    if test_B.shape[0] == 0:
        raise ValueError(f"No test data for category: {cat2}")

    

    # import sys
    # sys.exit()

    acc = run_LDA(
        train_A,
        train_B,
        test_A,
        test_B,
        classifier,
        window=1,
        step=1,
    )

    sum_accs = np.array([result["AUC"] for result in acc])

    out_dict = {}
    out_dict[f"{cat1}_vs_{cat2}"] = sum_accs

    # # Save results
    os.makedirs(f"results_{dataset}", exist_ok=True)
    with open(
        f"results_{dataset}/semantic_snr_results_{sub}_{types}.pkl",
        "wb",
    ) as f:
        pickle.dump(out_dict, f)

    n_samples = int((1.0 + 0.200) * 1000)  # total duration * sfreq
    times = np.linspace(-0.200, 1.0, n_samples, endpoint=False)

    # Create plot
    plt.figure(figsize=(8, 5))
    start = n_samples - int(
        sum_accs.shape[0]
    )  # Calculating the begginnig as the data will start not a time 0 but at time 1 or 2, depending on resampling
    plt.plot(times[start:], sum_accs, label=f"{types}", linewidth=2)
    plt.xlabel("Time (ms)")
    plt.ylabel("AUC")
    plt.title(f"LDA Decoding AUC:{dataset} Subject {sub} {types}")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()

    # Save figure
    os.makedirs(f"figs", exist_ok=True)
    plt.savefig(f"figs/LDA Decoding AUC:{dataset} Subject {sub} {types}.png")


for cat1, cat2 in category_pairs:

    types = f"{cat1}, {cat2}"
    # if dataset == "Alljoined-1.6M":
    #     dataset = ""
    filename = f"results_{dataset}/semantic_snr_results_{SUB}_{types}.pkl"

    if os.path.exists(filename):
        print(f"File {filename} exists, not running.")
        
    else:
        print(f"File {filename} does not exist, running")
        #try:
        run_cat_pairs(
            SUB,
            epoched_train,
            epoched_test,
            cat1,
            cat2,
            train_df,
            test_df,
            categories_lib,
            classifier,
            dataset
        )

        # except Exception as e:
        #     print(f"Error processing {dataset} sub {SUB}, {types}: {e}")
        #     continue

        
