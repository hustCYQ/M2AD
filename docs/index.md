---
layout: default
---

# PAPER

<div class="hero has-text-centered" id="paper">
<div class="myWrapper" markdown="1" align="left">



**[Visual Anomaly Detection under Complex View-Illumination Interplay: A Large-Scale Benchmark]()**

***Yunkang Cao\*, Yuqi Cheng\*, Xiaohao Xu, Yiheng Zhang, Yihan Sun, Yuxiang Tan, Yuxin Zhang, Weiming Shen***<br>
Huazhong University of Science and Technology     *\* Equal contribution*

The practical deployment of Visual Anomaly Detection (VAD) systems is hindered by their sensitivity to real-world imaging variations, particularly the complex interplay between viewpoint and illumination which drastically alters defect visibility. Current benchmarks largely overlook this critical challenge. We introduce **M**ulti-View **M**ulti-Illumination **A**nomaly **D**etection (***M<sup>2</sup>AD***), a new large-scale benchmark comprising 119,880 high-resolution images designed explicitly to probe VAD robustness under such interacting conditions. By systematically capturing 1,000 specimens across 10 categories using 12 synchronized views and 10 illumination settings (120 configurations total), ***M<sup>2</sup>AD*** enables rigorous evaluation. We establish two evaluation protocols: ***M<sup>2</sup>AD-Synergy*** tests the ability to fuse information across diverse configurations, and ***M<sup>2</sup>AD-Invariant*** measures single-image robustness amidst realistic view-illumination effects. Our extensive benchmarking shows that state-of-the-art VAD methods struggle significantly on ***M<sup>2</sup>AD***, demonstrating the profound challenge posed by view-illumination interplay. This benchmark serves as an essential tool for developing and validating VAD methods capable of overcoming real-world complexities.

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

| View-0°                                        | View-30°                                            | View-60°                                             | View-90°                                              | View-120°                                             | View-150° x                                      |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| ![Alt text](assets\images\multilight\image_0.jpg "0") | ![Alt text](assets\images\multilight\image_1.jpg "1") | ![Alt text](assets\images\multilight\image_2.jpg "2") | ![Alt text](assets\images\multilight\image_3.jpg "3") | ![Alt text](assets\images\multilight\image_4.jpg "4") | ![Alt text](assets\images\multilight\image_5.jpg "5") |

<!-- this space is essential -->

| View-180°                                         | View-210°                                            | View-240°                                             | View-270°                                               | View-300°                                              | View-330°                                       |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| ![Alt text](assets\images\multilight\image_0.jpg "0") | ![Alt text](assets\images\multilight\image_1.jpg "1") | ![Alt text](assets\images\multilight\image_2.jpg "2") | ![Alt text](assets\images\multilight\image_3.jpg "3") | ![Alt text](assets\images\multilight\image_4.jpg "4") | ![Alt text](assets\images\multilight\image_5.jpg "5") |

</div>
</div>


## Multi-Illumination

<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:800px;">

| Illumination-1      | Illumination-2      | Illumination-3      | Illumination-4      | Illumination-5      |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- | --------------------------- | --------------- |
| ![Alt text](assets\images\rgb_gifs\candy_cane.gif "candy cane") | ![Alt text](assets\images\rgb_gifs\chocolate_cookie.gif "chocolate cookie") | ![Alt text](assets\images\rgb_gifs\chocolate_praline.gif "chocolate_praline") | ![Alt text](assets\images\rgb_gifs\confetto.gif "confetto") | ![Alt text](assets\images\rgb_gifs\gummy_bear.gif "gummy_bear") |


<!-- this space is essential -->

| Illumination-6      | Illumination-7      | Illumination-8      | Illumination-9      | Illumination-10      |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Alt text](assets\images\rgb_gifs\hazelnut_truffle.gif "hazelnut_truffle") | ![Alt text](assets\images\rgb_gifs\licorice_sandwich.gif "licorice_sandwitch") | ![Alt text](assets\images\rgb_gifs\lollipop.gif "lollipop") | ![Alt text](assets\images\rgb_gifs\marshmallow.gif "marshmallow") | ![Alt text](assets\images\rgb_gifs\peppermint_candy.gif "peppermint candy") |

</div>
</div>

## Overview

<div markdown="1" style="overflow-x:scroll;">
<div markdown="1" style="min-width:800px;">

| Bird      | Car      | Cube      | Dice      | Doll      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------- |
| ![Alt text](assets\images\light_gifs\candy_cane.gif "candy cane") | ![Alt text](assets\images\light_gifs\chocolate_cookie.gif "chocolate cookie") | ![Alt text](assets\images\light_gifs\chocolate_praline.gif "chocolate_praline") | ![Alt text](assets\images\light_gifs\confetto.gif "confetto") | ![Alt text](assets\images\light_gifs\gummy_bear.gif "gummy_bear") |


<!-- this space is essential -->

| Holder       | Motor          | Ring           | Teapot           | Tube             |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![Alt text](assets\images\light_gifs\hazelnut_truffle.gif "hazelnut_truffle") | ![Alt text](assets\images\light_gifs\licorice_sandwich.gif "licorice_sandwitch") | ![Alt text](assets\images\light_gifs\lollipop.gif "lollipop") | ![Alt text](assets\images\light_gifs\marshmallow.gif "marshmallow") | ![Alt text](assets\images\light_gifs\peppermint_candy.gif "peppermint candy") |

</div>
</div>

</div>
</div>

# LEADERBOARD

<div class="hero" id="leaderboard" markdown="1">
<div markdown="1" style="overflow-x: scroll;">
| Method | Bird      | Car      | Cube     | Dice     | Doll    | Holder     | Motor      | Ring       | Teapot       | Tube        |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | ---: |
| Header | Title | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this |
| Paragraph | Text | And more | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this | Here's this |

<br>
<div class="myWrapper" align="left" markdown="1">


    

## Submit Your Results

Send us your results on the private test set so we can add your method to our leaderboard!

To do so, send an e-mail to **info@eyecan.ai** with subject "Eyecandies results submission" and the following info:

- The **name**/s of your method/s.
- A link to a published **paper** describing it/them.
- A download link with your results for every proposed method, with predicted heatmaps for every test set sample. We will compute metrics on those heatmaps.

Download the [template submission](https://drive.google.com/file/d/17qTSfqFesnb5BG6BdgegjWLv7bHKJJMs/view?usp=sharing) for more info on how to create your own and take a look at the [Eyecandies](https://github.com/eyecan-ai/eyecandies) repo for examples and tutorials. The dataset is formatted as a Pipelime underfolder, so take a look at [Pipelime](https://github.com/eyecan-ai/pipelime-python) as well!

Feel free to ask us any questions!

</div>
</div>
