import pandas as pd
import mne
import numpy as np
import os
from preprocessing_utils import read_eeg_data
from pathlib import Path
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

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
