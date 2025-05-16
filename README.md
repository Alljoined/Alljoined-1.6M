# Alljoined-1.6M

## Setup

**Before setting up the environment, ensure you have `mamba` installed.** 

### Create the Environment
Run the following command to create the environment using mamba:
```
mamba env create -f environment.yml
```
This will create a new environment with all required dependencies as specified in `environment.yml`.

### Activate the Environment
After the installation completes, activate the environment:
```
mamba activate aj-preprocessing 
```

### Updating the Enviroment
If new dependencies are added to `environment.yml`, update your environment with:
```
mamba env update -f environment.yml
```


## Preprocessing the data
We can run the preprocessing script from the root directory as a module:
```
python -m preprocessing --sub <subject>
```
By default, it will not show you warnings unless you add the `--verbose` argument.

The preprocessed data is then saved to  `preprocessed_eeg_{test,train}_flat.npy`.

### Epoching

In this stage, we concatenate all the raw edf files for each block, filter out oddball trials, and then throw the data into `mne.Epoch` to get epoched data. After this stage, we already get a numpy array of desired shape `(trials, channels, times)`.

### MVNN

The next stage is whitening the data, we throw the epoched training data, for each image condition, we compute the covariance of the channels for each timestamp, and then take the average. Then we take the average of all the average covariance matrix for each image condition, to obtain this average of average covariance matrix $\Sigma_{cond}$ and then apply $\Sigma_{cond}^{-1/2}$ to every epoched train and test trial.Z
