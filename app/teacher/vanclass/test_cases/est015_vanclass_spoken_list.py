#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.homework.object_page.spoken_detail_page import SpokenDetailPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class VanclassSpoken(unittest.TestCase):
    """本班 口语"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.v_detail = HwDetailPage()
        cls.van = VanclassPage()
        cls.speak = SpokenDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_spoken(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                van[3].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 页面检查点

                    self.van.vanclass_spoken()  # 进入 本班口语 todo
                    if self.detail.wait_check_page(gv.SPOKEN_ANALY):  # 页面检查点
                        if self.home.empty_tips():  # 无口语作业时
                            print('暂无口语作业')
                        else:  # 有卷子
                            print('口语作业:')
                            self.spoken_list_operate()

                        self.home.back_up_button()
                        if self.detail.wait_check_page(gv.SPOKEN_ANALY):  # 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 班级详情 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_page():  # 班级 页面检查点
                                    self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 口语作业页面')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def spoken_list_operate(self):
        """口语作业 列表 具体操作"""
        name = self.detail.hw_name()  # 口语作业包 name
        var = name[0].text
        name[0].click()  # 进入 口语作业
        if self.speak.wait_check_spoken_page():  # 页面检查点
            print('口语:', var)
            self.analysis_operate()

    @teststeps
    def analysis_operate(self):
        """具体操作"""
        if self.v_detail.load_empty():
            print('暂无数据')
        else:
            self.answer_analysis_detail(['', ''])  # 口语游戏list

    @teststeps
    def answer_analysis_detail(self, content):
        """口语游戏list"""
        mode = self.v_detail.game_type()  # 游戏类型
        name = self.v_detail.game_name()  # 游戏name
        rate = self.v_detail.average_achievement()  # 本班完成率

        if len(mode) > 5 and content[0] == '':
            content = []
            for j in range(len(mode) - 1):
                print(mode[j].text, name[j].text, rate[j].text)
            print('---------------------------')

            content.append(name[-1].text)  # 最后一个game的name
            content.append(mode[-1].text)  # 最后一个game的type
            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
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
            print('---------------------------')
