# ============================================================================
# usage: preprocessing.py [-h] --sub SUB [--n_ses N_SES] [--sfreq SFREQ]
#                         [--l_freq L_FREQ] [--h_freq H_FREQ]
#                         [--notch_freqs NOTCH_FREQS [NOTCH_FREQS ...]]
#                         [--mvnn_dim MVNN_DIM] [--project_dir PROJECT_DIR]
#
# Preprocess EEG data for a specific subject: epoching, filtering, MVNN, and saving.
#
# options:
#   -h, --help            show this help message and exit
#   --sub SUB, -s SUB     Subject number (e.g., 1 for sub-01)
#   --sfreq SFREQ         Target sampling frequency after downsampling (default: 250 Hz)
#   --l_freq L_FREQ       Low cutoff frequency for bandpass filter
#   --h_freq H_FREQ       High cutoff frequency for bandpass filter
#   --notch_freqs NOTCH_FREQS [NOTCH_FREQS ...]
#                         Frequencies for notch filtering to remove line noise
#   --mvnn_dim MVNN_DIM   MVNN computation mode: 'epochs', 'time' or 'off'
#   --project_dir PROJECT_DIR
#                         Base path to the EEG data project directory
#   --verbose             Enable verbose output during preprocessing
# ============================================================================
import argparse
import os
import pickle

import mne
import pandas as pd
from preprocessing_utils import (
    compute_stim_order,
    compute_whitening_matrix,
    epoching,
    save_data,
    whiten,
)

mne.set_log_level("WARNING")
# =============================================================================
# Input arguments
# =============================================================================
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(
    description=(
        "Preprocess EEG data for a specific subject: epoching, filtering,"
        " MVNN, and saving."
    )
)

parser.add_argument(
    "--sub",
    "-s",
    required=True,
    type=int,
    help="Subject number (e.g., 1 for sub-01)",
)
parser.add_argument(
    "--sfreq",
    default=250,
    type=int,
    help="Target sampling frequency after downsampling (default: 250 Hz)",
)
parser.add_argument(
    "--l_freq",
    type=float,
    help="Low cutoff frequency for bandpass filter",
)
parser.add_argument(
    "--h_freq",
    type=float,
    help="High cutoff frequency for bandpass filter",
)
parser.add_argument(
    "--notch_freqs",
    nargs="+",
    type=float,
    help="Frequencies for notch filtering to remove line noise",
)
parser.add_argument(
    "--mvnn_dim",
    default="epochs",
    type=str,
    help="MVNN computation mode: 'epochs', 'time' or 'off'",
)
parser.add_argument(
    "--project_dir",
    default="/srv/eeg_reconstruction/shared/data/",
    type=str,
    help="Base path to the EEG data project directory",
)
parser.add_argument(
    "--verbose",
    default=False,
    action="store_true",
    help="Enable verbose output during preprocessing",
)

args = parser.parse_args()

# =============================================================================

project_dir = args.project_dir
sub = args.sub

output_dir = os.path.join(
    project_dir, "preprocessed_data", "Alljoined-1.6M", f"sub-{sub:02d}"
)
os.makedirs(output_dir, exist_ok=True)
metadata = pd.read_parquet(
    os.path.join(
        project_dir, "preprocessed_data", "Alljoined-1.6M", "metadata.parquet"
    )
)

# =============================================================================
# Epoch and sort the data
# =============================================================================
# Channel selection, epoching, baseline correction and frequency downsampling of
# the training data partitions.
# Then, the conditions are sorted and the EEG data is reshaped to:
# Image conditions × EEG repetitions × EEG channels × EEG time points
# This step is applied independently to the data of each partition and session.

# We use the first 4 blocks of each session for testing data and the rest
# for training data.
TEST_BLOCKS = range(1, 5)
TRAIN_BLOCKS = range(5, 20)

epoched_test = epoching(
    sub,
    blocks=TEST_BLOCKS,
    project_dir=project_dir,
    l_freq=args.l_freq,
    h_freq=args.h_freq,
    sfreq=args.sfreq,
    notch_freqs=args.notch_freqs,
    verbose=args.verbose,
)

epoched_train = epoching(
    sub,
    blocks=TRAIN_BLOCKS,
    project_dir=project_dir,
    l_freq=args.l_freq,
    h_freq=args.h_freq,
    sfreq=args.sfreq,
    notch_freqs=args.notch_freqs,
    verbose=args.verbose,
)

# Compute the number of dropped trials
test_df = compute_stim_order(sub, epoched_test, metadata, verbose=args.verbose)
train_df = compute_stim_order(
    sub, epoched_train, metadata, verbose=args.verbose
)
stim_order = pd.concat([test_df, train_df], ignore_index=True)
stim_order.to_parquet(
    os.path.join(output_dir, f"experiment_metadata.parquet"),
)

# =============================================================================
# Multivariate Noise Normalization
# =============================================================================

if args.mvnn_dim != "off":
    # dict of format {session: white}
    whitening_matrices = compute_whitening_matrix(
        mvnn_dim=args.mvnn_dim,
        epoched_datas=epoched_train,
        stim_order=train_df,
        verbose=args.verbose,
    )

    epoched_train = whiten(epoched_train, whitening_matrices)
    epoched_test = whiten(epoched_test, whitening_matrices)

    with open(
        os.path.join(output_dir, f"mvnn_whitening_matrices.pkl"), "wb"
    ) as f:
        pickle.dump(whitening_matrices, f)

# =============================================================================
# Merge and save the preprocessed data
# =============================================================================

save_data(
    os.path.join(output_dir, "preprocessed_eeg_test_flat.npy"), epoched_train
)
save_data(
    os.path.join(output_dir, "preprocessed_eeg_training_flat.npy"),
    epoched_train,
)
