import os

default_settings = {
    # 开始界面的背景，16进制的颜色
    # Start screen background, hexadecimal color
    "start_background": "#171F3A",  # type:str

    # 数据可视化界面的背景，16进制的颜色
    # draw  screen background, hexadecimal color
    "draw_background": "#171F3A",  # type:str

    # 背景音乐的文件位置，支持的音乐有,　下个版本加播放音乐功能
    # background_music : File location, Play music features in the next release
    # "background_music": None,  # type:str  example:>>>  "background_music": "background_music.mp3"


    # 绘制出前多少名
    # How many to drawn
    "rank_number": 15,  # type:int

    # 柱状图第一个位置
    # Histogram's first position
    "start_x": 14,  # type:int
    "start_y": 15,  # type:int

    # FPS设置一秒多少帧
    # setings screen FPS
    "FPS": 30,  # type:int

    # 一列数据切换到另一列数据使用的时长
    # The length of time a column of data is switched to another column of data
    "time": 3,  # type:int

    # 设置字体样式，如果为None，自动匹配合适的字体样式
    # Set font style, if None, automatically match the appropriate font style
    "font_style": None,  # type:str

    # 图标位置
    # Icon location
    "icon": "icon.png",  # type:str
    "red_start": "red_start.png",  # type:str
    "red_start_x": 50,  # type:int
    "red_start_y": 65,  # type:int
    "green_start": "green_start.png",  # type:str

    # 首页大字体的设置
    # start screen headline font settings
    "first_headline_size": 5,  # type:int
    "first_headline_color": "#ECF0F1",  # type:str
    "first_headline_bold": True,  # type:bool(True, False)
    "headline_center_x": 50,  # type:int
    "headline_center_y": 20,  # type:int

    # 首页小字体的设置
    # start screen subtitle font settings
    "first_subtitle_size": 2,  # type:int
    "first_subtitle_color": "#DC7633",  # type:str
    "first_subtitle_bold": False,  # type:bool(True, False)
    "subtitle_center_x": 75,  # type:int
    "subtitle_center_y": 35,  # type:int

    # 数据可视化界面标题字体的设置
    # draw screen font settings
    # one font
    "draw_one_size": 4,  # type:int
    "draw_one_color": "#F2F5FF",  # type:str
    "draw_one_bold": True,  # type:bool(True, False)
    "draw_one_center_x": 50,  # type:int
    "draw_one_center_y": 5,  # type:int

    # two font
    "draw_two_size": 1.5,  # type:int
    "draw_two_color": "#F2F5FF",  # type:str
    "draw_two_bold": False,  # type:bool(True, False)
    "draw_two_center_x": 92,  # type:int
    "draw_two_center_y": 10,  # type:int

    # three font
    "draw_three_size": 1.5,  # type:int
    "draw_three_bold": True,  # type:bool

    # four font
    "draw_four_size": 1.5,  # type:int
    "draw_four_bold": False,  # type:bool

    # five font
    "draw_five_size": 8,  # type:int
    "draw_five_color": "#EAEAF7",  # type:str
    "draw_five_bold": True,  # type:bool(True, False)
    "draw_five_center_x": 85,  # type:int
    "draw_five_center_y": 75,  # type:int

    # six font
    "draw_six_size": 1,  # type:int
    "draw_six_color": "#006699",  # type:str
    "draw_six_bold": False,  # type:bool
    "draw_six_center_y": 98,  # type:int

    # setting data lines style
    "line_color": "#006699",  # type:str
    "line_top" : 15, # type:int
    "line_bottom": 95,  # type:int
    # line number max　　最多五根线
    "line_number_max": 8,  #type:int
}

# 内置了31种颜色
# defaut 31 colors
color_set = {"#5566CE", "#FF6668", "#FF9935", "#EFAACD", "#FF2278", "#0177EF", "#995433", "#F0BB68",
             "#FFCC01", "#6598FF", "#89AA56", "#AB7656", "#683266", "#9BCBFF", "#FE6633", "#FF779B",
             "#45BAFF", "#EF9957", "#0277CD", "#DC0178", "#FF9988", "#DF4267", "#346600", "#89CC98",
             "#9866BB", "#E03266", "#8988BB", "#A97766", "#FA1C1C", "#4B69C0", "#76C9E4"}

# color_set = {'#98CC32', '#28821B', '#634FB7', '#588939', '#D77268', '#DF0078', '#9868BD', '#B34136', '#FA1C1C', '#7584BF',
#              '#CEBB9A', '#4B69C0', '#B01112', '#FF7B47', '#3399AC', '#76C9E4', '#13A2CE', '#CBAC30', '#45BAFF', '#369DAB',
#              '#8F837D', '#FF779B', '#13339B', '#9866BB', '#898889', '#5F0002', '#FF9988', '#8A71C5', '#56B0B1', '#EF9957',
#              '#08CBAD'}
