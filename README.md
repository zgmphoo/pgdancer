### pgdancer：一个python的通用动态数据可视化框架
-----

[English](readme-en.md)


## 介绍
这是一个python的动态数据可视化项目，基于pygame游戏引擎。能够将pandas的Dataframe数据结构使用动态的方法展示。

## Requirements
* Anaconda-python 3.61+ and pygame 1.95+
* Works on Linux, windows, Mac OSX

## 效果展示

![image](docs/images/demo.gif)

# 快速开始

```python
pip install pgdancer
```

打开命令行终端

```python
pgdancer startproject my_project
cd my_project
```

在项目目录中，会生成 settings.py 文件作为设置文件，当你需要它的时候
#### 下载示例csv文件,[点我下载](examples/brands_data.csv)
把文件放在命令行终端的文件夹路径中

```python
vim demo.py
```

写入以下内容并保存

```python
import pandas as pd


from pgdancer import histogram


if __name__ == '__main__':
    # example code
    df = pd.read_csv("brands_data.csv", index_col="brands", thousands=",").fillna(0)
    df = df.astype("int")
    h = histogram.Histogram(df, 1600, 900, window_type=0)
    h.run("pgdancer", "Top 15 Best Global Brands Ranking", "---Datasource:https://www.interbrand.com", \
          "Top 15 Best Global Brands Ranking", "Brand Value:$m")

```

运行python脚本
```python
python demo.py
```

## 使用文档
文档正在编写中

## 特别说明
字体问题: pygame默认字体是英文的,显示中文或特殊文字会出现框框,
以下方法可以获取系统字体列表，增加histogram.py源码中getFontStyle函数中的font_list列表可以解决
PS：后续版本会解决字体问题
```python
import pygame
pygame.font.get_fonts()
```
颜色问题：
pgdancer内置了31种颜色，Dataframe.index 超过31个则会报错
PS：后续版本会解决颜色问题

# 未来的版本
1. 加入有图片的动态样式
2. 加入背景音乐功能
3. 组件化
4. 更漂亮
