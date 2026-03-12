import pickle
from pathlib import Path

import mne
import pandas as pd

from preprocessing_utils import (
    compute_dropped_trials,
    compute_whitening_matrix,
    epoching,
    get_preprocessing_parser,
    make_configs_from_args,
    save_data,
    whiten,
)

parser = get_preprocessing_parser()
ARGS = parser.parse_args()

mne.set_log_level("WARNING" if not ARGS.verbose else "INFO")

PROJECT_DIR = Path(ARGS.project_dir)
SUB = ARGS.sub
CONFIGS = make_configs_from_args(ARGS)

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
test_df = compute_dropped_trials(
    epoched_test,
    stim_order.query("partition == 'stim_test'"),
    verbose=ARGS.verbose,
)
train_df = compute_dropped_trials(
    epoched_train,
    stim_order.query("partition == 'stim_train'"),
    verbose=ARGS.verbose,
)

stim_order["dropped"] = True
stim_order.loc[test_df.index, "dropped"] = False
stim_order.loc[train_df.index, "dropped"] = False
stim_order.to_parquet(OUTPUT_DIR / "experiment_metadata.parquet")

# --------------------------------------------------------------------------
# MVNN whitening -----------------------------------------------------------
if CONFIGS.mvnn_dim is not None:
    whitening_mats = compute_whitening_matrix(
        CONFIGS.mvnn_dim,
        epoched_train,
        train_df,
        verbose=ARGS.verbose,
    )
    epoched_train = whiten(epoched_train, whitening_mats)
    epoched_test = whiten(epoched_test, whitening_mats)

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
