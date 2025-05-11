---
layout: default
---

# PAPER

<div class="hero has-text-centered" id="paper">
<div class="myWrapper" markdown="1" align="left">



**[Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark]()**

***Yunkang Cao\*, Yuqi Cheng\*, Xiaohao Xu, Yiheng Zhang, Yihan Sun, Yuxiang Tan, Yuxin Zhang, Weiming Shen***<br>
Huazhong University of Science and Technology     *\* Equal contribution*

The practical deployment of Visual Anomaly Detection (VAD) systems is hindered by their sensitivity to real-world imaging variations, particularly the complex interplay between viewpoint and illumination which drastically alters defect visibility. Current benchmarks largely overlook this critical challenge. We introduce **M**ulti-View **M**ulti-Illumination **A**nomaly **D**etection (***M<sup>2</sup>AD***), a new large-scale benchmark comprising 119,880 high-resolution images designed explicitly to probe VAD robustness under such interacting conditions. By systematically capturing 999 specimens across 10 categories using 12 synchronized views and 10 illumination settings (120 configurations total), ***M<sup>2</sup>AD*** enables rigorous evaluation. We establish two evaluation protocols: ***M<sup>2</sup>AD-Synergy*** tests the ability to fuse information across diverse configurations, and ***M<sup>2</sup>AD-Invariant*** measures single-image robustness amidst realistic view-illumination effects. Our extensive benchmarking shows that state-of-the-art VAD methods struggle significantly on ***M<sup>2</sup>AD***, demonstrating the profound challenge posed by view-illumination interplay. This benchmark serves as an essential tool for developing and validating VAD methods capable of overcoming real-world complexities.

### Cite Us

If you use this dataset in your research, please cite the following paper:

```
@inproceedings{M2AD,
    title={Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark},
    author={XXX},
    booktitle={Arxiv},
    year={2025},
}
```

</div>
</div>

# THE DATASET


<div class="hero has-text-centered" id="dataset">
<div class="myWrapper" markdown="1" align="center">

## Data Acquisition


![Alt text](assets\images\multilight\image_0.jpg "0")



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

| Method  | Bird      | Car      | Cube     | Dice     | Doll    | Holder     | Motor      | Ring       | Teapot       | Tube        |
| A |   |   |   |   |   |   |   |   |   |   |
| B |   |   |   |   |   |   |   |   |   |   |
| C |   |   |   |   |   |   |   |   |   |   |
| D |   |   |   |   |   |   |   |   |   |   |
| E |   |   |   |   |   |   |   |   |   |   |

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
