# The core objects and functions of this file store program
import os
import sys


class Recter(object):
    def __init__(self, name, y, v, diff_x, diff_y, x_mean, old_x):
        """
        this class is draw Rect
        :param name: name
        :param y: rect->pos.y
        :param v: value
        :param diff_x: rect length increase
        :param diff_y: rect y increase
        :param x_mean: value increase
        :param old_x: rect initial length
        """
        self.name = name
        self.y = y
        self.v = v
        self.diff_x = diff_x
        self.diff_y = diff_y
        self.x_mean = x_mean
        self.old_x = old_x


class DataLine(object):
    """
    DataLine对象   --- DataLine object
    """

    def __init__(self, x, diff_x, value):
        self.x = x
        self.diff_x = diff_x
        self.value = value


def genDict(series1, series2):
    # 生成根据value排名的字典
    # generate dict[index] = rank
    index1 = series1.sort_values(ascending=False).index
    dic1 = dict()
    for i in range(len(index1)):
        dic1[index1[i]] = i

    index2 = series2.sort_values(ascending=False).index
    dic2 = dict()
    for i in range(len(index2)):
        dic2[index2[i]] = i
    return dic1, dic2


def roundDown(number):
    # 向下取整
    # round int down
    num = str(round(number))
    l = len(num) - 1
    n = int(num[0])
    return n * 10 ** l


def getRoundDownList(number, line_max):
    mean = roundDown(int(number) / line_max)
    round_lst = list()
    value = mean
    while value < number:
        round_lst.append(value)
        value += mean
    return round_lst


def read_settings(file_path):
    # read settings
    settings_dict = dict()
    with open(file_path, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line[0] == '#':
                continue
            else:
                num = line.find("=")
                if num == -1:
                    continue
                else:
                    key = line[:num]
                    value = eval(line[num+1:].strip())
                    settings_dict[key] = value
    return settings_dict
