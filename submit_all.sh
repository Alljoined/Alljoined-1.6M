#!/bin/bash
#SBATCH --priority=100000

# First collect subject numbers until we hit a flag
subjects=()
while [[ "$1" != --* && $# -gt 0 ]]; do
  subjects+=("$1")
  shift
done

# Save remaining args to pass along
extra_args="$@"

# Loop over subjects and submit one job per subject
for sub in "${subjects[@]}"; do
  echo "Submitting job for subject $sub"
  sbatch run_processing.sh "$sub" $extra_args
done
