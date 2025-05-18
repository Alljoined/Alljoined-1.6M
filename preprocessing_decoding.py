import itertools
import os
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd
from mne.decoding import CSP
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from mne.decoding import CSP

from all_categories import get_categories
from lda_utils import prep_decoding_data_hierarchical, run_LDA
from preprocessing_utils import (
    compute_dropped_trials,
    compute_whitening_matrix,
    epoching,
    get_preprocessing_parser,
    make_configs_from_args,
    whiten,
)

parser = get_preprocessing_parser()
parser.add_argument("--cat1", type=str)
parser.add_argument("--cat2", type=str)
ARGS = parser.parse_args()

mne.set_log_level("WARNING" if not ARGS.verbose else "INFO")

PROJECT_DIR = Path(ARGS.project_dir)
SUB = ARGS.sub
CONFIGS = make_configs_from_args(ARGS)

stim_order = pd.read_parquet(
    PROJECT_DIR
    / "preprocessed_data"
    / "Alljoined-1.6M"
    / f"sub-{SUB:02d}"
    / "stim_order.parquet"
)

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

test_df = compute_dropped_trials(
    epoched_test,
    stim_order.query("partition == 'stim_test'"),
    verbose=ARGS.verbose,
)
test_df = test_df[~test_df["dropped"]].reset_index(drop=True)
train_df = compute_dropped_trials(
    epoched_train,
    stim_order.query("partition == 'stim_train'"),
    verbose=ARGS.verbose,
)
train_df = train_df[~train_df["dropped"]].reset_index(drop=True)

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
# Classification -----------------------------------------------------------
# Create CSP + LDA pipeline
csp = CSP(n_components=4, reg=None, log=None, transform_into="csp_space")
lda = LinearDiscriminantAnalysis()
flatten = FunctionTransformer(
    lambda x: x.reshape(x.shape[0], -1) if x.ndim > 2 else x, validate=True
)
classifier = Pipeline(
    [
        # ('CSP', csp),
        ("flatten", flatten),
        ("LDA", lda),
    ]
)

epoched_test = np.concatenate([x.get_data() for x in epoched_test])
epoched_train = np.concatenate([x.get_data() for x in epoched_train])


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
):
    if cat1 == cat2:
        return

    train_A, train_B, test_A, test_B = prep_decoding_data_hierarchical(
        merged_train,
        merged_test,
        [cat1],
        [cat2],
        train_df,
        test_df,
        categories_lib,
    )
    if train_A.shape[0] == 0:
        raise ValueError(f"No train data for category: {cat1}")
    if train_B.shape[0] == 0:
        raise ValueError(f"No train data for category: {cat2}")
    if test_A.shape[0] == 0:
        raise ValueError(f"No test data for category: {cat1}")
    if test_B.shape[0] == 0:
        raise ValueError(f"No test data for category: {cat2}")

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

    # # Save results
    n_samples = int((1.0 + 0.200) * 256)  # total duration * sfreq
    times = np.linspace(-0.200, 1.0, n_samples, endpoint=False)

    # Create plot
    plt.figure(figsize=(8, 5))
    start = n_samples - int(
        sum_accs.shape[0]
    )  # Calculating the begginnig as the data will start not a time 0 but at time 1 or 2, depending on resampling
    types = f"{cat1}, {cat2}"
    plt.plot(times[start:], sum_accs, linewidth=2)
    plt.xlabel("Time (ms)")
    plt.ylabel("AUC")
    plt.title(f"LDA Decoding AUC: Subject {sub} {types}")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()

    # Save figure
    os.makedirs(f"figs", exist_ok=True)
    plt.savefig(f"figs/LDA Decoding AUC: Subject {sub} {types}.png")


cat1 = ARGS.cat1
cat2 = ARGS.cat2
categories_lib = get_categories()
if cat1 is not None and cat2 is not None:
    category_pairs = [(cat1, cat2)]
elif cat1 is None and cat2 is None:
    category_pairs = itertools.combinations(categories_lib.keys(), 2)
else:
    if cat1 is None:
        cat1, cat2 = cat2, cat1
    category_pairs = [(cat1, x) for x in categories_lib.keys() if x != cat1]

for cat1, cat2 in category_pairs:
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
    )
