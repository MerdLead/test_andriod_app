#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class VanclassHw(unittest.TestCase):
    """本班作业"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_homework(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                for i in range(len(van)):
                    if van[i].text == gv.VAN_LIST:
                        van[i].click()  # 进入班级详情页
                        break
                if self.van.wait_check_vanclass_page(gv.VAN_LIST):  # 页面检查点

                    self.van.vanclass_hw()  # 进入 本班作业
                    if self.detail.wait_check_page(gv.HW_LIST):  # 页面检查点
                        print('%s 本班作业:' % gv.VAN_LIST)
                        self.hw_list_operate()  # 作业列表 具体操作

                        self.home.back_up_button()
                        if self.van.wait_check_vanclass_page(gv.VAN_LIST):  # 班级详情 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_page():  # 班级 页面检查点
                                self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 本班作业页面')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def hw_list_operate(self):
        """作业列表 具体操作"""
        ele = self.hw_operate('')  # 作业列表
        while not self.detail.end_tips():  # 如果list多于一页
            self.home.screen_swipe_up(0.5, 0.75, 0.1, 1000)
            self.hw_operate(ele)  # 作业列表

    @teststeps
    def hw_operate(self, item):
        """作业列表"""
        name = self.detail.hw_name()  # 作业name
        progress = self.detail.progress()  # 已完成x/x
        create = self.detail.create_time()  # 作业创建时间
        remind = self.detail.remind()  # 提醒按钮

        if len(create) == 5 or self.detail.end_tips() is False:  # 作业 多于一页
            for i in range(len(remind)):
                print('------------------')
                print(name[i].text, '\n',
                      progress[i].text, '\n',
                      create[i].text)
                if self.home.selected(remind[i]) is False:
                    print('★★★ Error- 提醒按钮selected 属性')

            return name[len(remind)-1].text
        elif self.detail.end_tips():  # 作业一页 and 翻页以后
            if len(item) != 0:
                if name[-1].text != item:  # 翻页成功
                    var = 0
                    for j in range(len(remind)):
                        if item == name[j].text:
                            var = j+1
                    for i in range(var, len(create)):
                        print('------------------')
                        print(name[i].text, '\n',
                              progress[i].text, '\n',
                              create[i].text)
                        if self.home.selected(remind[i]) is False:
                            print('★★★ Error- 提醒按钮selected 属性')
            else:
                for i in range(len(remind)):
                    print('------------------')
                    print(name[i].text, '\n',
                          progress[i].text, '\n',
                          create[i].text)
                    if self.home.selected(remind[i]) is False:
                        print('★★★ Error- 提醒按钮selected 属性')

            return name[len(remind)-1].text
