# M2AD Benchmark


> [**Paper**] [**论文名字**](https://export.arxiv.org/abs/2409.13162). [**HomePage**] (https://export.arxiv.org/abs/2409.13162).
>
> by [Yuqi Cheng*](https://hustcyq.github.io/), [Yunkang Cao*](https://caoyunkang.github.io/), [Guoyang Xie](https://guoyang-xie.github.io/), Zhichao Lu, [Weiming Shen](https://scholar.google.com/citations?user=FuSHsx4AAAAJ&hl=en),

## Introduction 
Detecting anomalies within point clouds is crucial for various industrial applications, but traditional unsupervised methods face challenges due to data acquisition costs, early-stage production constraints, and limited generalization across product categories. To overcome these challenges, we introduce the Multi-View Projection (MVP) framework, leveraging pre-trained Vision-Language Models (VLMs) to detect anomalies. Specifically, MVP projects point cloud data into multi-view depth images, thereby translating point cloud anomaly detection into image anomaly detection. Following zero-shot image anomaly detection methods, pre-trained VLMs are utilized to detect anomalies on these depth images. Given that pre-trained VLMs are not inherently tailored for zero-shot point cloud anomaly detection and may lack specificity, we propose the integration of learnable visual and adaptive text prompting techniques to fine-tune these VLMs, thereby enhancing their detection performance. Extensive experiments on the MVTec 3D-AD and Real3D-AD demonstrate our proposed MVP framework's superior zero-shot anomaly detection performance and the prompting techniques' effectiveness. Real-world evaluations on automotive plastic part inspection further showcase that the proposed method can also be generalized to practical unseen scenarios.

## Overview of M2AD
### 采集过程
<img src="./Imgs/F5.png" width="800px">

### 10个类别
<img src="./Imgs/F5.png" width="800px">

### 多光照-多视角
<img src="./Imgs/F5.png" width="800px">


## 🛠️ Getting Started

### Installation
To set up the MVP-PVLIP environment, follow one of the methods below:

- Clone this repo:
  ```shell
  git clone https://github.com/hustCYQ/MVP-PCLIP.git && cd MVP-PCLIP
  ```
- Construct the experimental environment, follow these steps:
    ```shell
  conda create --name ADer python=3.9
  conda activate ADer
  pip install timm==0.8.15dev0 opencv-python==4.9.0.80 opencv-contrib-python==4.9.0.80 numpy==1.26 # not sure, but seems ADEval requires opencv-python==4.9.0.80  
  pip install thop seaborn mmselfsup pandas transformers openpyxl imgaug numba  tensorboard fvcore  Ninja ftfy scikit-learn einops 
  pip install git+https://gitcode.com/gh_mirrors/cl/CLIP
  conda install -c conda-forge accimage
  pip install mmdet==2.25.3
  pip install --upgrade protobuf==3.20.1 scikit-image faiss-gpu
  pip install adeval tensorboardX
  pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu118
  pip install fastprogress geomloss FrEIA fvcore==0.1.5.post20221221  
  ```


### Dataset Preparation 
You can choose to download **original** datasets and process them according to **Preprocess**. You are also welcome to directly download our **processed** datasets. All datasets need to be placed in your `DATA_ROOT`. 

| Dataset | Google Drive | Baidu Drive | Note
|------------|------------------|------------------| ------------------|
| M2AD-256    | [Google Drive] | [Baidu Drive](https://pan.baidu.com/s/1juZIAOqIwD4EWri1D5TiIw?pwd=flg9) | Original |
| M2AD-256    | [Google Drive] | [Baidu Drive](https://pan.baidu.com/s/1OUoZA8hW8FoYBom5PP4WxQ?pwd=pwus) | Original |


- preprare data, adjust data/dataset_info
  ```shell
  python gen_meta_data.py -d miv    
  ```


### Train & Test
```
python run_exps.py
```

## Main Results

### 1. Results on M2AD 256x256
<img src="./Imgs/T1.png" width="800px">

### 2. Results on M2AD 512x512
<img src="./Imgs/T2.png" width="800px">


## 💘 Acknowledgements
Our work is largely inspired by the following projects. Thanks for their admiring contribution.

- [ADer]()
- [informer]()
- [Dinomaly]()




## Citation

If you find this project helpful for your research, please consider citing the following BibTeX entry.

```BibTex

@inproceedings{PCLIP,
  title={Towards Zero-shot Point Cloud Anomaly Detection: A Multi-View Projection Framework},
  author={Yuqi, Cheng and Yunkang, Cao and Guoyang, Xie and Zhichao, Lu and Weiming, Shen},
  booktitle={},
  year={2024}
}

```




