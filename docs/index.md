---
layout: default
---

# PAPER

<div class="hero has-text-centered" id="paper">
<div class="myWrapper" markdown="1" align="left">



**[Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark](https://arxiv.org/abs/2505.10996)  (accepted by Pattern Recognition)**

***Yunkang Cao\*, Yuqi Cheng\*, Yuxin Zhang, Xiaohao Xu, Yiheng Zhang, Yihan Sun, Yuxiang Tan, Xiaonan Huang, Chao Huang, Weiming Shen***<br>
Huazhong University of Science and Technology     *\* Equal contribution*


The practical deployment of Visual Anomaly Detection (VAD) systems is hindered by their sensitivity to real-world imaging variations, particularly the complex interplay between viewpoint and illumination which drastically alters defect visibility. Current benchmarks largely overlook this critical challenge. We introduce **M**ulti-View **M**ulti-Illumination **A**nomaly **D**etection (***M<sup>2</sup>AD***), a new large-scale benchmark comprising 119,880 high-resolution images designed explicitly to probe VAD robustness under such interacting conditions. By systematically capturing 999 specimens across 10 categories using 12 synchronized views and 10 illumination settings (120 configurations total), ***M<sup>2</sup>AD*** enables rigorous evaluation. We establish two evaluation protocols: ***M<sup>2</sup>AD-Synergy*** tests the ability to fuse information across diverse configurations, and ***M<sup>2</sup>AD-Invariant*** measures single-image robustness amidst realistic view-illumination effects. Our extensive benchmarking shows that state-of-the-art VAD methods struggle significantly on ***M<sup>2</sup>AD***, demonstrating the profound challenge posed by view-illumination interplay. This benchmark serves as an essential tool for developing and validating VAD methods capable of overcoming real-world complexities.

### Cite Us

If you use this dataset in your research, please cite the following paper:

```
@inproceedings{M2AD,
    title={Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark},
    author={Cao, Yunkang and Cheng, Yuqi and Xu, Xiaohao and Zhang, Yiheng and Sun, Yihan and Tan, Yuxiang and Zhang, Yuxin and Huang, Xiaonan and Shen, Weiming},
    booktitle={https://arxiv.org/abs/2505.10996},
    year={2025},
}
```

```
@inproceedings{M2AD,
    title={Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark},
    author={Cao, Yunkang and Cheng, Yuqi and Zhang, Yuxin and Xu, Xiaohao and Zhang, Yiheng and Sun, Yihan and Tan, Yuxiang and Huang, Xiaonan and Huang, Chao and Shen, Weiming},
    booktitle={Pattern Recognition},
    year={2026},
}
```

</div>
</div>

# THE DATASET


<div class="hero has-text-centered" id="dataset">
<div class="myWrapper" markdown="1" align="center">

## Data Acquisition


![Alt text](assets\images\collection.gif "0")



## Ten Object Classes
<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:800px;">

| Bird      | Car      | Cube      | Dice      | Doll      |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- | --------------------------- | --------------- |
| ![Alt text](assets\images\Obj_gif\bird.gif "bird") | ![Alt text](assets\images\Obj_gif\car.gif "car") | ![Alt text](assets\images\Obj_gif\cube.gif "cube") | ![Alt text](assets\images\Obj_gif\dice.gif "dice") | ![Alt text](assets\images\Obj_gif\doll.gif "doll") |


<!-- this space is essential -->

| Holder       | Motor          | Ring           | Teapot           | Tube             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Alt text](assets\images\Obj_gif\holder.gif "holder") | ![Alt text](assets\images\Obj_gif\motor.gif "motor") | ![Alt text](assets\images\Obj_gif\ring.gif "ring") | ![Alt text](assets\images\Obj_gif\teapot.gif "teapot") | ![Alt text](assets\images\Obj_gif\tube.gif "tube") |

</div>
</div>

## Multi-View

<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:100px;">

| Bird      | Car      | Cube      | Dice      | Doll      |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- | --------------------------- | --------------- |
| ![Alt text](assets\images\MV_gif\bird.gif "bird") | ![Alt text](assets\images\MV_gif\car.gif "car") | ![Alt text](assets\images\MV_gif\cube.gif "cube") | ![Alt text](assets\images\MV_gif\dice.gif "dice") | ![Alt text](assets\images\MV_gif\doll.gif "doll") |


<!-- this space is essential -->

| Holder       | Motor          | Ring           | Teapot           | Tube             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Alt text](assets\images\MV_gif\holder.gif "holder") | ![Alt text](assets\images\MV_gif\motor.gif "motor") | ![Alt text](assets\images\MV_gif\ring.gif "ring") | ![Alt text](assets\images\MV_gif\teapot.gif "teapot") | ![Alt text](assets\images\MV_gif\tube.gif "tube") |


</div>
</div>


## Multi-Illumination

<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:800px;">

| Bird      | Car      | Cube      | Dice      | Doll      |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- | --------------------------- | --------------- |
| ![Alt text](assets\images\MI_gif\bird.gif "bird") | ![Alt text](assets\images\MI_gif\car.gif "car") | ![Alt text](assets\images\MI_gif\cube.gif "cube") | ![Alt text](assets\images\MI_gif\dice.gif "dice") | ![Alt text](assets\images\MI_gif\doll.gif "doll") |


<!-- this space is essential -->

| Holder       | Motor          | Ring           | Teapot           | Tube             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Alt text](assets\images\MI_gif\holder.gif "holder") | ![Alt text](assets\images\MI_gif\motor.gif "motor") | ![Alt text](assets\images\MI_gif\ring.gif "ring") | ![Alt text](assets\images\MI_gif\teapot.gif "teapot") | ![Alt text](assets\images\MI_gif\tube.gif "tube") |

</div>
</div>

## Multi-View & Multi-Illumination

<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:800px;">

| Bird      | Car      | Cube      | Dice      | Doll      |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- | --------------------------- | --------------- |
| ![Alt text](assets\images\MIV_gif\bird.gif "bird") | ![Alt text](assets\images\MIV_gif\car.gif "car") | ![Alt text](assets\images\MIV_gif\cube.gif "cube") | ![Alt text](assets\images\MIV_gif\dice.gif "dice") | ![Alt text](assets\images\MIV_gif\doll.gif "doll") |


<!-- this space is essential -->

| Holder       | Motor          | Ring           | Teapot           | Tube             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Alt text](assets\images\MIV_gif\holder.gif "holder") | ![Alt text](assets\images\MIV_gif\motor.gif "motor") | ![Alt text](assets\images\MIV_gif\ring.gif "ring") | ![Alt text](assets\images\MIV_gif\teapot.gif "teapot") | ![Alt text](assets\images\MIV_gif\tube.gif "tube") |


</div>
</div>

</div>
</div>

# LEADERBOARD


    
<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:400px;">

| Method     | Bird            | Car             | Cube            | Dice            | Doll            | Holder          | Motor           | Ring            | Teapot          | Tube            | Mean            |
| CDO        | 70.6/74.1/90.1  | 76.8/65.2/77.9  | 72.2/64.9/72.4  | 93.0/82.0/82.2  | 69.9/64.0/74.4  | 96.0/78.1/72.9  | 83.7/69.7/94.0  | 91.6/84.9/88.8  | 92.6/79.8/92.6  | 96.5/81.8/93.7  | 84.3/74.4/83.9  |
| RD++       | 90.3/70.2/79.8  | 85.0/68.2/75.6  | 83.1/74.6/80.7  | 98.4/89.4/85.6  | 66.8/65.9/85.4  | 99.1/87.8/81.0  | 92.2/87.9/94.9  | 95.5/90.9/77.2  | 91.3/86.0/91.7  | 92.1/81.2/90.9  | 89.4/80.2/84.3  |
| MSFlow     | 85.0/62.0/71.4  | 67.9/55.9/67.4  | 66.0/57.8/58.7  | 76.8/69.4/77.0  | 56.4/55.1/68.9  | 98.0/76.6/59.6  | 86.0/61.4/86.7  | 74.7/72.4/83.9  | 83.0/63.9/77.3  | 89.0/67.3/84.1  | 78.3/64.2/73.5  |  
| Dinomaly   | 75.1/74.9/86.9  | 86.7/75.1/78.3  | 82.3/77.8/86.0  | 98.1/93.0/85.7  | 74.4/72.6/89.0  | 99.7/85.8/90.0  | 95.4/85.4/94.2  | 91.2/87.3/77.8  | 99.9/94.6/94.3  | 97.2/83.3/77.0  | 90.0/83.0/85.9  |  
| INP-Former | 80.0/67.2/84.1  | 58.1/53.9/72.1  | 77.9/74.5/80.6  | 93.3/83.7/87.7  | 72.5/73.7/85.8  | 99.2/76.4/81.0  | 83.7/61.1/91.9  | 75.5/71.7/91.4  | 91.6/79.1/92.4  | 78.0/64.1/85.9  | 71.0/70.5/85.3  |  

</div>
</div>

## Submit Your Results

<div class="myWrapper" align="left" markdown="1">


Send us the performance of your method on our dataset, and we will add your results to our leaderboard!  

Please send an e-mail to **yuqicheng@hust.edu.cn** with subject "results of {Your method name} on M2AD" and the following info:

- The full **name**/s of your method/s.
- A link to a published **paper** describing it/them.
- A **csv or xlsx** file with detailed results.

Feel free to ask us any questions!

</div>
