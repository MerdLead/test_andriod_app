#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.spoken_detail_page import SpokenDetailPage
from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Spoken(unittest.TestCase):
    """ 口语 答题分析tab"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = HwDetailPage()
        cls.speak = SpokenDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_spoken_analysis_detail(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            print('##########################################')
            if self.home.wait_check_no_page():
                print('无最新动态 -- (用户指南) 欢迎使用在线助教,打开看看吧!')
            else:
                name = self.home.get_type('口语')
                for i in range(len(name[1])):
                    var = name[0][name[1][i]].text  # 作业名称
                    print(var[4:])
                    if var[4:] == '口语test':
                        name[0][name[1][1]].click()  # 进入作业
                        break

                if self.speak.wait_check_spoken_page():  # 页面检查点
                    print('口语:', '口语test')
                    self.analysis_operate()

                    self.home.back_up_button()

            print('##########################################')

        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def analysis_operate(self):
        """具体操作"""
        if self.detail.load_empty():
            print('暂无数据')
        else:
            self.answer_analysis_detail(['', ''])  # 口语游戏list

    @teststeps
    def answer_analysis_detail(self, content):
        """口语游戏list"""
        mode = self.detail.game_type()  # 游戏类型
        name = self.detail.game_name()  # 游戏name
        rate = self.detail.average_achievement()  # 本班完成率

        if len(mode) > 5 and content[0] == '':
            content = []
            for j in range(len(mode) - 1):
                print(mode[j].text, name[j].text, rate[j].text)

            content.append(name[-1].text)  # 最后一个game的name
            content.append(mode[-1].text)  # 最后一个game的type
            self.speak.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.answer_analysis_detail(content)

            return content
        else:
            var = 0
            for k in range(len(mode)):
                if content[0] == name[k].text and content[1] == mode[k].text:
                    var += k
                    break

            for j in range(var, len(mode)):
                print(mode[j].text, name[j].text, rate[j].text)
