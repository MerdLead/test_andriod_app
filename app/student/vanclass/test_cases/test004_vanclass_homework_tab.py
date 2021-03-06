#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.vanclass.object_page.vanclass_page import VanclassPage
from app.student.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.student.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class VanclassHw(unittest.TestCase):
    """本班作业 - 各tab信息"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = LoginPage()
        cls.home = HomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_homework_tab(self):
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
                    if self.detail.wait_check_page(gv.VAN_LIST):  # 页面检查点
                        print('%s 本班作业:' % gv.VAN_LIST)
                        self.all_hw_operate()  # 全部 tab
                        self.incomplete_operate()  # 未完成 tab
                        self.complete_operate()  # 已完成 tab

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
            try:
                Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            except Exception:
                print("未进入主界面")
                raise

    @teststeps
    def all_hw_operate(self):
        """全部tab 具体操作"""
        all_hw = self.detail.all_finish_tab(1)  # 全部 tab
        if self.detail.selected(all_hw) is False:
            print('★★★ Error- 未默认在 全部页面')
        else:
            print('--------------全部tab-------------------')
            if self.van.empty_tips():
                print('暂无数据')
            else:
                self.hw_list_operate()

    @teststeps
    def incomplete_operate(self):
        """未完成tab 具体操作"""
        incomplete = self.detail.all_finish_tab(2)  # 未完成 tab
        if self.detail.selected(incomplete) is True:
            print('★★★ Error- 默认在 未完成 tab页')
        else:
            incomplete.click()  # 进入 未完成 tab页
            if self.detail.selected(incomplete) is False:
                print('★★★ Error- 未进入 未完成 tab页')
            else:
                print('--------------未完成tab-------------------')
                if self.van.empty_tips():
                    print('暂无数据')
                else:
                    self.hw_list_operate()

    @teststeps
    def complete_operate(self):
        """已完成tab 具体操作"""
        complete = self.detail.all_finish_tab(3)  # 已完成 tab
        if self.detail.selected(complete) is True:
            print('★★★ Error- 默认在 已完成 tab页')
        else:
            complete.click()  # 进入 已完成 tab页
            if self.detail.selected(complete) is False:
                print('★★★ Error- 未进入 已完成 tab页')
            else:
                print('--------------已完成tab-------------------')
                if self.van.empty_tips():
                    print('暂无数据')
                else:
                    self.hw_list_operate()

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
        # progress = self.detail.progress()  # 完成进度
        finish = self.detail.finish_status()  # 已经有x人完成

        if len(name) == 5 or self.detail.end_tips() is False:  # 作业 多于一页
            for i in range(len(name)):
                print('------------------')
                print(name[i].text, '\n',
                      finish[i].text)

            return name[-1].text
        elif self.detail.end_tips():  # 作业一页 and 翻页以后
            if len(item) != 0:
                if name[-1].text != item:  # 翻页成功
                    var = 0
                    for j in range(len(name)):
                        if item == name[j].text:
                            var = j + 1
                    for i in range(var, len(name)):
                        print('------------------')
                        print(name[i].text, '\n',
                              finish[i].text)
            else:
                for i in range(len(name)):
                    print('------------------')
                    print(name[i].text, '\n',
                          finish[i].text)

            return name[-1].text
