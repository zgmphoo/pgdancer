### pgdancer：common dynamic data visualization framework for python
-----

[中文](README.md)


## Overview
This is a python dynamic data visualization project，Power by Pygame and Pandas。
Ability to display Pandas Dataframe data structures in a dynamic way。

## Requirements
* Anaconda-python 3.61+ and pygame 1.95+
* Works on Linux, windows, Mac OSX

## Show project GIF

![image](docs/images/demo.gif)

# Quick start

```python
pip install pgdancer
```

Open the command line terminal

```python
pgdancer startproject my_project
cd my_project
```

In the project directory, the settings.py file is generated as the settings file when you need it.
#### Download the CSV file：[examples/brands_data.csv](examples/brands_data.csv)
Place the CSV file in the folder path of the command line terminal

```python
vim demo.py
```

Write the following and save it

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

Run the python file
```python
python demo.py
```

## Documentation
Documentation in progress

## Special note
Font problem: The default font of the pygame is English, and the box will appear when displaying Chinese or special text.
The following methods can be used to obtain the font list of the system. Adding the font_list list list of getFontStyle function in the source code of histogram.py can solve this problem.
PS: Subsequent versions will solve the font problem
```python
import pygame
pygame.font.get_fonts()
```
Colour problem：
Pgdancer has 31 colors built in, and more than 31 Dataframe.index will report errors
PS: Subsequent versions will solve the color problem

# future Version
1. Add a dynamic style with pictures
2. Add Background Music in settings
3. Componentization
4. More beautiful 
