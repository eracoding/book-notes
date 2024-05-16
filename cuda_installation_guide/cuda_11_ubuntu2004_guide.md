# Step by step instruction how to install CUDA 11 Ubuntu 20.04


## NVidia Ubuntu 20.04 repository for CUDA 11

If you need CUDA Tolkit 11 with `nvcc`, other tools and libraries you can install it from NVIDIA Ubunutu 20.04 repository.

Add Ubuntu 20.04 repository 

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600

#add public keys

# Old key
#sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub

# new key, added 2022-04-25 22:52
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub

sudo add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"

```

## Install cuda toolkit

Update and install cuda toolkit, you will gain access to many version of cuda and cuda toolkit. 

Write `apt install cuda-toolkit` and press tab it will show list of all available versions  

```
sudo apt update
sudo apt install cuda-toolkit-11-6

```


## Install cuDNN

[Download cuDNN from NVidia](https://developer.nvidia.com/cudnn). You'll have to log in, answer a few questions then you will be redirected to download. Find the right cuDNN binary packages and save it on you computer.

```
tar -xzvf cudnn-11.2-linux-x64-v8.1.1.33.tgz

sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```

## Add CUDA_HOME to PATH environmet


Edit `/home/$USER/.bashrc` file


```
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
export CUDA_HOME=/usr/local/cuda
export PATH="/usr/local/cuda/bin:$PATH"
```


## Disable Sleep on Ubuntu Server

New drivers automatically install some xorg server packages and it activates power management options. Probably on your server you want to disable power management (sleep, hibernate).


```
sudo systemctl mask sleep.target suspend.target hibernate.target
```
