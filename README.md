# Idcard-landmarks
## 实现功能
 - 身份证RFB版本的训练
 - 身份证4个关键点检测
# 带有关键点检测的超轻量级身份证检测器


### Contents
- [Installation](#installation)
- [Training](#training)
- [References](#references)

## Installation
##### Clone and install
1. git clone https://github.com/Vivianyzw/Idcard-landmarks.git

2. Pytorch version 1.1.0+ and torchvision 0.3.0+ are needed.

3. Codes are based on Python 3

##### Data
1. The dataset directory as follows:

```Shell
  ./data/idcard/
    train/
    val/
    train.txt
    val.txt
```
2. We provide the organized dataset we used as in the above directory structure.

```
# train.txt, path to image ,x1 y1 x2 y1 ptx1 pty1 ptx2 pty2 ptx3 pty3 ptx4 pty4 cls
# train/1_02.png
279.545 581.909 1243.182 1472.818 320.455 618.273 1202.273 629.636 1197.727 1402.364 304.545 1416.0 0.0
# train/1_00.png
382.818 625.818 1137.364 1244.0 414.636 662.182 1105.545 666.727 1110.091 1203.091 414.636 1198.545 0.0
```

## Training

1. Before training, you can check network configuration (e.g. batch_size, min_sizes and steps etc..) in ``data/config.py and train.py``.

2. Train the model :
  ```Shell
  CUDA_VISIBLE_DEVICES=0 python train.py --network RFB
  ```

If you don't want to train, we also provide a trained model on ./weights
  ```Shell
  RBF_Final.pth
  ```
## References
- [Face-Detector-1MB-with-landmark](https://github.com/biubug6/Face-Detector-1MB-with-landmark)
```
@inproceedings{deng2019retinaface,
title={RetinaFace: Single-stage Dense Face Localisation in the Wild},
author={Deng, Jiankang and Guo, Jia and Yuxiang, Zhou and Jinke Yu and Irene Kotsia and Zafeiriou, Stefanos},
booktitle={arxiv},
year={2019}
```