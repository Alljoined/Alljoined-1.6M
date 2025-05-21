import pandas as pd
import mne
import numpy as np
import os
from preprocessing_utils import read_eeg_data
from pathlib import Path
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score

cnt = np.zeros((6, 20), dtype=int)
data_dir = Path("/srv/eeg_reconstruction/shared/data/raw_eeg/Alljoined-1.6M")

for sub in tqdm(range(1, 21)):
    for sess in tqdm(range(1, 5), leave=False):
        try:
            for b in range(1, 20):
                raw = read_eeg_data(
                    data_dir
                    / f"sub-{sub:02d}"
                    / f"session_{sess:02d}"
                    / f"block_{b:02d}"
                )
                events, event_id = mne.events_from_annotations(
                    raw, regexp="behav.*", verbose=False
                )

                for e in event_id.keys():
                    behav_val = int(e.split(",")[1])
                    cnt[behav_val, sub - 1] += 1
        except FileNotFoundError:
            continue

plt.figure(figsize=(20, 6))
sns.heatmap(cnt, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Subject")
plt.xticks(ticks=np.arange(20) + 0.5, labels=np.arange(1, 21))
plt.ylabel("Behavioral Value")
plt.title("Count of Behavioral Values per Subject")
plt.savefig("behavioral_counts.png")

tot = cnt.sum(axis=0)
pct = np.vstack(
    (
        (cnt[0] + cnt[3]).reshape(1, -1),
        (cnt[1] + cnt[2]).reshape(1, -1),
        (cnt[4] + cnt[5]).reshape(1, -1),
    )
)
pct = pct / tot
plt.figure(figsize=(20, 6))
sns.heatmap(pct, annot=True, fmt=".2f", cmap="Blues")
plt.xlabel("Subject")
plt.xticks(ticks=np.arange(20) + 0.5, labels=np.arange(1, 21))
plt.ylabel("Accuracy percent")
plt.yticks(
    ticks=np.arange(3) + 0.5, labels=["Correct", "Incorrect", "No Response"]
)
plt.title("Count of Behavioral Values per Subject")
plt.savefig("behavioral_accuracy.png")

# Calculate AUC for each subject
aucs = []

for subj in range(20):
    y_true = []
    y_pred = []
    y_score = []

    # Expand counts into lists
    # 0: Yes, correct → Woody present → label 1, response 1
    y_true += [1] * cnt[0, subj]
    y_pred += [1] * cnt[0, subj]

    # 1: Yes, incorrect → Woody absent → label 0, response 1
    y_true += [0] * cnt[1, subj]
    y_pred += [1] * cnt[1, subj]

    # 2: No, incorrect → Woody present → label 1, response 0
    y_true += [1] * cnt[2, subj]
    y_pred += [0] * cnt[2, subj]

    # 3: No, correct → Woody absent → label 0, response 0
    y_true += [0] * cnt[3, subj]
    y_pred += [0] * cnt[3, subj]

    # Ignore missed responses (4 & 5)

    try:
        auc = roc_auc_score(y_true, y_pred)
    except ValueError:
        auc = np.nan  # Handle subjects with no data
    aucs.append(auc)

# Create APA-style table
auc_table = pd.DataFrame({"Subject": np.arange(1, 21), "AUC": aucs})
auc_table = auc_table.round(3)

# Save to APA-style CSV
auc_table.to_csv("subject_auc_table.csv", index=False)

# Optionally visualize
plt.figure(figsize=(10, 4))
sns.barplot(x="Subject", y="AUC", data=auc_table, palette="Blues_d")
plt.ylim(0.5, 1.05)
plt.title("Subjects Performance (in AUC) in the Oddball Task")
plt.savefig("auc_per_subject.png")
