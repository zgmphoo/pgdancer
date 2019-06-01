### Pgdancer：一个python的通用动态数据可视化框架
-----

[English](readme-en.md)


### 介绍
这是一个python的动态数据可视化项目，基于pygame游戏引擎。能够将pandas的Dataframe数据使用动态的方法展示。
使用Anaconda-python3.7和pygame==1.95构建

### 效果展示

![image](docs/images/demo.gif)

# 快速开始

pandas的Dataframe格式如下：

![images](https://github.com/zgmphoo/Pgdancer/blob/master/docs/images/dataframe_format.png)

```python
git clone https://github.com/zgmphoo/pgdancer.git
```
或者下载解压文件.打开pgdancer中的的examples
```python
python histogram_demo1.py
```
或者运行Jupyter Notebook 打开 histogram_demo1.ipynb
## 特别说明
字体问题: 系统默认字体是英文的,有时候显示中文会出现框框,需要
```python
import pygame
pygame.font.get_fonts()
```
从系统列表中选择适当的字体加入到pgdancer/histogram.py 文件中的Histogram对象中getFontStyle函数中的列表中
Pgdancer内置了31种16进制的颜色，会随机生成一个颜色。


