#!/usr/bin/env python
# encoding:UTF-8
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


def remote_info_511():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = '127.0.0.1'
    desired_caps['app'] = PATH('..\\student_debug_1.2.2.apk')
    desired_caps['appPackage'] = "com.vanthink.student.debug"
    desired_caps['appActivity'] = "com.vanthink.vanthinkstudent.v2.ui.splash.SplashActivity"
    desired_caps["automationName"] = "uiautomator2"
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True

    return desired_caps


def remote_info_442():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '127.0.0.1'

    desired_caps['app'] = PATH('..\\student_debug_1.2.2.apk')
    desired_caps['appPackage'] = "com.vanthink.student.debug"
    desired_caps['appActivity'] = "com.vanthink.vanthinkstudent.v2.ui.splash.SplashActivity"
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    return desired_caps
