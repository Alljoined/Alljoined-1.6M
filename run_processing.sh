#!/bin/bash
#SBATCH --job-name=preproc
#SBATCH --output=slurm_logs/preproc_sub$1_%j.out
#SBATCH --error=slurm_logs/preproc_sub$1_%j.err
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=80GB
#SBATCH --ntasks=1
#SBATCH --priority=100000


# Load environment
source ~/.bashrc

if [ -z "$CONDA_PREFIX" ] || [ "$CONDA_DEFAULT_ENV" = "base" ]; then
    if [ -d "/srv/envs/$USER/miniconda3" ]; then
        source "/srv/envs/$USER/miniconda3/etc/profile.d/conda.sh"
        source "/srv/envs/$USER/miniconda3/etc/profile.d/mamba.sh"
    else
        echo "No miniconda3 found."
        exit 1
    fi
    mamba activate eeg-data-preprocessing
fi

# Run Python script
python -m preprocessing --sub "$1" ${@:2}
