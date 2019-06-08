import os
import sys
import math

import pandas as pd
import pygame

from pgdancer.core import genDict, Recter, getRoundDownList, DataLine, read_settings
from pgdancer.core_settings import default_settings, color_set


class Histogram(object):
    """
    Class: Dynamic data visualization bar chart
    """

    def __init__(self, dataframe, window_width=1600, window_height=900, window_type=0, settings=None,):
        """
        
        :param dataframe: type pandas's Dataframe 
        :param window_width: window's width
        :param window_height: window's height
        :param window_type: window's type, user: 0, 1, 2, 3
        type_dict = {0: 0,   ---> commom window
                    1: pygame.NOFRAME,   ---> no have close button
                    2: pygame.FULLSCREEN  --->full screen window
                    }
        :param settings: Your settings file's name, example: "settings.py"
        """
        if isinstance(dataframe, pd.DataFrame):
            self.df = dataframe
        else:
            raise Exception("dataframe not pandas.Dataframe")
        if isinstance(window_type, int):
            type_dict = {0: 0, 1: pygame.NOFRAME, 2: pygame.FULLSCREEN}
            self.window_type = type_dict.get(window_type, 0)
        else:
            raise TypeError("window_type not int")
        if isinstance(window_width, int) and isinstance(window_height, int):
            self.width = window_width
            self.height = window_height
        else:
            raise TypeError("window_width or window_height not int")
        # 窗口分为100份
        # window_size average 100
        self.grad_x = int(self.width / 100)
        self.half_grad_x = int(self.grad_x / 2)
        self.grad_y = int(self.height / 100)
        if settings is None:
            self.settings = default_settings
        else:
            if isinstance(settings, str):
                file_path = os.path.join(os.getcwd(), settings)
                print(file_path)
                setting = read_settings(file_path)
                default_settings.update(setting)
                self.settings = default_settings
            else:
                raise Exception("param:Your_settings should type:str! example: 'settings.py'")


    def terminate(self):
        pygame.quit()
        sys.exit()

    def getFontStyle(self):
        """
        :return: a usable font style
        """
        font_list = ["microsoftyaheimicrosoftyaheiuibold", "notosanscjksc", "microsoftyahei", "pingfangttc", \
                     "microsoftyaheitruetypemicrosoftyaheiuibold"]
        font_style = None
        for i in range(len(font_list)):
            if font_list[i] in pygame.font.get_fonts():
                font_style = font_list[i]
                break
        return font_style

    def showStartScreen(self, first_headline, first_subtitle):
        """
        Start Screen
        :param first_headline: start screen headline
        :param first_subtitle: start screen subtitle
        :return: 
        """
        # 首页大字体的设置
        # start screen headline font setings
        headline_color = pygame.Color(self.settings["first_headline_color"])
        headline_font = pygame.font.SysFont(font_style, int(self.settings["first_headline_size"] * self.grad_x), \
                                            self.settings["first_headline_bold"])
        if isinstance(first_headline, str):
            headline_surf = headline_font.render(first_headline, True, headline_color)
        else:
            raise TypeError("first_headline not str!")
        headline_rect = headline_surf.get_rect( \
            center=(
                self.settings["headline_center_x"] * self.grad_x,
                self.settings["headline_center_y"] * self.grad_y))

        # 首页小字体的设置
        # start screen subtitle font setings
        subtitle_color = pygame.Color(self.settings["first_subtitle_color"])
        subtitle_font = pygame.font.SysFont(font_style, int(self.settings["first_subtitle_size"] * self.grad_x), \
                                            self.settings["first_subtitle_bold"])
        if isinstance(first_subtitle, str):
            subtitle_surf = subtitle_font.render(first_subtitle, True, subtitle_color)
        else:
            raise TypeError("first_subtitle not str!")
        subtitle_rect = subtitle_surf.get_rect( \
            center=(
                self.settings["subtitle_center_x"] * self.grad_x,
                self.settings["subtitle_center_y"] * self.grad_y))

        # 缩放图片
        # transform start image
        red_surf = pygame.image.load(os.path.join(os.path.dirname(__file__), "images", self.settings["red_start"])).convert_alpha()
        start_rect = red_surf.get_rect()
        red_surf = pygame.transform.smoothscale(red_surf, (start_rect.width // 2, start_rect.height // 2))
        center = (self.settings["red_start_x"] * self.grad_x, self.settings["red_start_y"] * self.grad_y)
        start_rect = red_surf.get_rect(center=center)
        r = (start_rect.right - start_rect.left) / 2
        green_surf = pygame.image.load(os.path.join(os.path.dirname(__file__), "images", self.settings["green_start"])).convert_alpha()
        green_surf = pygame.transform.smoothscale(green_surf, (start_rect.width, start_rect.height))
        can_click = False

        while True:
            # 事件处理
            # Handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN and can_click is True:
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.terminate()
            screen.fill(pygame.Color(self.settings["start_background"]))
            screen.blit(headline_surf, headline_rect)
            screen.blit(subtitle_surf, subtitle_rect)
            x, y = pygame.mouse.get_pos()
            space = math.hypot(x - center[0], y - center[1])
            if space > r:
                screen.blit(red_surf, start_rect)
                can_click = False
            else:
                screen.blit(green_surf, start_rect)
                can_click = True
            pygame.display.update()
            fclock.tick(self.settings["FPS"])

    def showDrawScreen(self, second_headline, second_subtitle):
        """
        draw screen
        :param second_headline: one font content
        :param second_subtitle: two font content
        :return: 
        """
        # Defining var
        # 这里定义进度条的初始位置
        start_x = self.settings["start_x"] * self.grad_x
        start_y = self.settings["start_y"] * self.grad_y

        # one_font
        draw_one_font = pygame.font.SysFont(font_style, int(self.settings["draw_one_size"] * self.grad_x), \
                                            self.settings["draw_one_bold"])
        draw_one_surf = draw_one_font.render(second_headline, True, pygame.Color(self.settings["draw_one_color"]))
        draw_one_rect = draw_one_surf.get_rect( \
            center=(
                self.settings["draw_one_center_x"] * self.grad_x,
                self.settings["draw_one_center_y"] * self.grad_y))

        # two font
        draw_two_font = pygame.font.SysFont(font_style, int(self.settings["draw_two_size"] * self.grad_x), \
                                            self.settings["draw_two_bold"])
        draw_two_surf = draw_two_font.render(second_subtitle, True, pygame.Color(self.settings["draw_two_color"]))
        draw_two_rect = draw_two_surf.get_rect( \
            center=(
                self.settings["draw_two_center_x"] * self.grad_x,
                self.settings["draw_two_center_y"] * self.grad_y))

        # three font
        draw_three_font = pygame.font.SysFont(font_style, int(self.settings["draw_three_size"] * self.grad_x), \
                                              self.settings["draw_three_bold"])

        # four font
        draw_four_font = pygame.font.SysFont(font_style, int(self.settings["draw_four_size"] * self.grad_x), \
                                             self.settings["draw_four_bold"])

        # five font
        draw_five_font = pygame.font.SysFont(font_style, int(self.settings["draw_five_size"] * self.grad_x), \
                                             self.settings["draw_five_bold"])

        # six font
        draw_six_font = pygame.font.SysFont(font_style, int(self.settings["draw_six_size"] * self.grad_x), \
                                            self.settings["draw_six_bold"])

        six_center_y = self.settings["draw_six_center_y"] * self.grad_y
        line_color = pygame.Color(self.settings["line_color"])
        line_top = self.settings["line_top"] * self.grad_y
        line_bottom = self.settings["line_bottom"] * self.grad_y
        background_color = pygame.Color(self.settings["draw_background"])
        # 设置前多少名排名
        # settings rank_number
        if self.settings["rank_number"] is None:
            rank_number = len(self.df.index)
        else:
            rank_number = self.settings["rank_number"]
        # 设置宽度和柱形图的高度
        # calculation Rect's width
        full_height = 80 / rank_number * self.grad_y
        rect_height = 0.6 * full_height
        # 处理Dataframe
        # processing Dataframe
        df_lst = self.df.columns
        # 得到datanode节点
        # get datanode's list
        data_line_list = getRoundDownList(self.df.values.max(), self.settings["line_number_max"])
        # columns's length
        number = len(df_lst)
        index_lst = list(self.df.index)
        color_dic = dict()
        # Chinese
        # 为每个index的设定颜色
        # 这个很重要,如果你想要一个自定义颜色的话，自定义颜色的字典为index的name，　自定义颜色值为16进制的颜色，
        # 然后在循环赋值之后加入　　color_dict = your_dict
        # English
        # Set the color for each index
        # This is very important,if you want a custom color,
        # the dictionary of Custom colors is the name of the index, and the custom color value is 16 of the binary color
        for i in range(len(index_lst)):
            if i > 30:
                raise Exception("颜色数量不足，这里仅仅内置了31种颜色！")
            rand_color = color_set.pop()
            color_dic[index_lst[i]] = rand_color

        # FPS
        ftime = self.settings["FPS"] * self.settings["time"]
        # 循环获取series，每次获取两组
        n = 0
        while n < number - 1:
            series1 = self.df[df_lst[n]]
            series2 = self.df[df_lst[n + 1]]
            dic1, dic2 = genDict(series1, series2)
            maxValue1 = max(series1)
            maxValue2 = max(series2)
            # 这里80代表界面的百分之80
            # 80 on behalf of screen
            mean1 = 80 / maxValue1 * self.grad_x
            mean2 = 80 / maxValue2 * self.grad_x
            # 装Recter的列表
            # append Recter
            all_lst = list()
            # 装dataline的列表
            # append datanode
            node_lst = list()
            # append dataline
            for i in range(len(data_line_list)):
                node_value = data_line_list[i]  # 值
                node1 = mean1 * node_value  # 这是node1的位置X的位置
                node2 = mean2 * node_value  # 这是相同的值在不同的位置中的位置
                line_node = DataLine(node1, (node2 - node1) / ftime, node_value)
                node_lst.append(line_node)

            # 计算并且实例化Recter
            # append Recter
            for name, value in dic1.items():  # key is name, value is rank
                v = series1[name]  # this is series's value
                # rect  length increase
                x_diff = (series2[name] * mean2 - v * mean1) / ftime
                # value increase
                x_mean = (series2[name] - v) / ftime
                # rect initial length
                old_x = v * mean1
                if value < rank_number:  # Previously the top rank_number
                    y = start_y + value * full_height
                    if dic2[name] < rank_number:  # Continue to be the top rank_number behind
                        y_diff = ((dic2[name] - value) * full_height) / ftime
                    else:  # Previously the top rank_number and later retired from the top rank_number
                        y_diff = ((self.height + 5 * self.grad_y) - y) / ftime
                    recter = Recter(name, y, v, x_diff, y_diff, x_mean, old_x)
                    all_lst.append(recter)
                else:  # Not the top rank_number before
                    y = self.height + 5 * self.grad_y
                    if dic2[name] < rank_number:  # Then entered the top rank_number
                        y_diff = ((start_y + dic2[name] * full_height) - y) / ftime
                    else:  # Not yet the top rank_number
                        y_diff = 0
                    recter = Recter(name, y, v, x_diff, y_diff, x_mean, old_x)
                    all_lst.append(recter)
            # draw screen
            m = 1
            while m <= ftime:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.terminate()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.terminate()

                screen.fill(background_color)
                screen.blit(draw_one_surf, draw_one_rect)
                screen.blit(draw_two_surf, draw_two_rect)

                # draw datalines
                for i in range(len(node_lst)):
                    n_v = node_lst[i].value  # 值
                    n_diff_x = node_lst[i].diff_x  # 偏差
                    n_x = start_x + node_lst[i].x + m * n_diff_x  # 位置
                    n_headline_surf = draw_six_font.render(str(n_v), True,
                                                           pygame.Color(self.settings["draw_six_color"]))
                    n_headline_rect = n_headline_surf.get_rect(center=(n_x, six_center_y))
                    screen.blit(n_headline_surf, n_headline_rect)
                    pygame.draw.aaline(screen, line_color, [n_x, line_top], [n_x, line_bottom])
                # draw Recters
                for i in range(len(all_lst)):
                    diff_x = all_lst[i].diff_x  # x增长的长度
                    diff_y = all_lst[i].diff_y  # y增长
                    mean_x = all_lst[i].x_mean  # value的平均值
                    color = pygame.Color(color_dic[all_lst[i].name])  # 颜色
                    rect_y = all_lst[i].y + m * diff_y  # 坐标Y
                    rect_v = all_lst[i].v + m * mean_x  # 确定的值
                    old_x = all_lst[i].old_x  # 初始长度
                    pygame.draw.rect(screen, color, (start_x, rect_y, old_x + m * diff_x, rect_height))
                    font_name_surf = draw_three_font.render(all_lst[i].name, True, color)
                    font_name_rect = font_name_surf.get_rect()
                    font_name_rect.right = start_x - self.half_grad_x
                    font_name_rect.bottom = rect_y + rect_height
                    screen.blit(font_name_surf, font_name_rect)
                    font_num_surf = draw_four_font.render(str(int(rect_v)), True, color)
                    font_num_rect = font_num_surf.get_rect()
                    font_num_rect.left = start_x + old_x + m * diff_x + self.half_grad_x
                    font_num_rect.bottom = font_name_rect.bottom
                    screen.blit(font_num_surf, font_num_rect)

                m += 1
                # draw five font
                names = series1.name
                draw_five_surf = draw_five_font.render(names, True,
                                                       pygame.Color(self.settings["draw_five_color"]))
                draw_five_rect = draw_five_surf.get_rect( \
                    center=(self.settings["draw_five_center_x"] * self.grad_x, \
                            self.settings["draw_five_center_y"] * self.grad_y))

                screen.blit(draw_five_surf, draw_five_rect)
                pygame.display.update()
                fclock.tick(self.settings["FPS"])
            n += 1

        # last screen
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.terminate()

            screen.fill(background_color)
            screen.blit(draw_one_surf, draw_one_rect)
            screen.blit(draw_two_surf, draw_two_rect)
            for i in range(len(all_lst)):
                last_name = all_lst[i].name
                diff_x = all_lst[i].diff_x  # x增长的长度
                diff_y = all_lst[i].diff_y  # y增长
                mean_x = all_lst[i].x_mean  # value的平均值
                color = pygame.Color(color_dic[all_lst[i].name])  # 颜色
                rect_y = all_lst[i].y + m * diff_y  # 坐标Y
                rect_v = series2[last_name]  # 确定的值
                old_x = all_lst[i].old_x  # 初始长度
                pygame.draw.rect(screen, color, (start_x, rect_y, old_x + m * diff_x, rect_height))
                font_name_surf = draw_three_font.render(last_name, True, color)
                font_name_rect = font_name_surf.get_rect()
                font_name_rect.right = start_x - self.half_grad_x
                font_name_rect.bottom = rect_y + rect_height
                screen.blit(font_name_surf, font_name_rect)
                font_num_surf = draw_four_font.render(str(int(rect_v)), True, color)
                font_num_rect = font_num_surf.get_rect()
                font_num_rect.left = start_x + old_x + m * diff_x + self.half_grad_x
                font_num_rect.bottom = font_name_rect.bottom
                screen.blit(font_num_surf, font_num_rect)

            names = series2.name
            draw_five_surf = draw_five_font.render(names, True,
                                                   pygame.Color(self.settings["draw_five_color"]))
            draw_five_rect = draw_five_surf.get_rect(center=(self.settings["draw_five_center_x"] * self.grad_x, \
                                                             self.settings["draw_five_center_y"] * self.grad_y))

            screen.blit(draw_five_surf, draw_five_rect)
            pygame.display.update()
            fclock.tick(self.settings["FPS"])

    def run(self, window_name, first_headline, first_subtitle, second_headline, second_subtitle):
        global fclock, screen, font_style
        pygame.init()
        size = self.width, self.height
        fclock = pygame.time.Clock()
        icon = pygame.image.load(os.path.join(os.path.dirname(__file__), "images", self.settings["icon"]))
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode(size, self.window_type)
        if isinstance(window_name, str):
            pygame.display.set_caption(window_name)
        else:
            raise TypeError("window_name's type not str!")
        if self.settings["font_style"] is None:
            font_style = self.getFontStyle()
        else:
            font_style = self.settings["font_style"]
        # start screen
        self.showStartScreen(first_headline, first_subtitle)
        # draw screen
        self.showDrawScreen(second_headline, second_subtitle)


