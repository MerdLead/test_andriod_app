#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from conf.base_page import BasePage
from conf.decorator import teststeps
from utils.click_bounds import ClickBounds


@teststeps
def games_keyboard(key):
    """小键盘 q w e等字母"""
    screen = BasePage().get_window_size()
    keyboard = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                'capslock', 'z', 'x', 'c', 'v', 'b', 'n', 'm', "backspace",
                ',', '.', '-', 'blank', "'", 'enter']
    if key.lower() in keyboard:
        i = keyboard.index(key.lower())
        if i < 10:
            ClickBounds().click_bounds(0.08888 * screen[0] * (i+0.5) + 0.011 * screen[0]*(i+1), 1010)
        elif i in range(10, 19):
            ClickBounds().click_bounds((0.08888+0.011) * screen[0] * (i - 9), 1085)  # i +1-10
        elif i in range(19, 27):
            ClickBounds().click_bounds((0.08888+0.011) * screen[0] * (i - 18), 1158)  # i+1-19
        else:  # 27--32
            if i > 30:
                ClickBounds().click_bounds(0.08888 * screen[0] * (i-25+0.5) + 0.011 * screen[0]*(i - 23), 1240)  #
            else:
                ClickBounds().click_bounds(0.08888 * screen[0] * (i - 28 + 0.5) + 0.011 * screen[0] * (i - 26), 1240)

    # if key.lower() in keyboard:
    #     i = keyboard.index(key.lower())
    #     print(key.lower())
    #     if i < 10:
    #         ClickBounds().click_bounds(90 * (i + 0.5) + 15 * (i + 1), 1385)
    #     elif i in range(10, 19):
    #         ClickBounds().click_bounds(105 * (i - 9), 1535)  # i +1-10
    #     elif i in range(19, 28):
    #         ClickBounds().click_bounds(105 * (i - 18), 1685)  # i+1-19
    #     else:  # 28--32
    #         if i > 30:
    #             ClickBounds().click_bounds(90 * (i - 25 + 0.5) + 15 * (i - 23), 1835)  #
    #         else:
    #             ClickBounds().click_bounds(90 * (i - 28 + 0.5) + 15 * (i - 26), 1835)

    """小键盘
    第一行： # 90 * (i+0.5) 一个按钮大小为90 及点击按钮中心点+0.5
            # 15*(i+1)  按钮间隔
    第二行：# 90 * (i-10+0.5+0.5) 一个按钮大小为90及点击按钮中心点+0.5及第一个按钮之前的缩进+0.5
            # 15*(i-10+1)  按钮间隔
    第三行：  # 90 * (i-19+0.5+0.5) 一个按钮大小为90及点击按钮中心点+0.5及第一个按钮之前的缩进+0.5
            # 15*(i-19+1)  按钮间隔
    第四行：
            ！> 30: # 90 * (i-24+0.5) 一个按钮大小为90及点击按钮中心点+0.5
                    # 15*(i + 2 -26+1)  按钮间隔
            ! < 31:  # 90 * (i-27+0.5) 一个按钮大小为90及点击按钮中心点+0.5
                # 15*(i-27+1)  按钮间隔
    """
