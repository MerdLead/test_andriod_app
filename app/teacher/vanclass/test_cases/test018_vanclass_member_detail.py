#!/usr/bin/env python
# encoding:UTF-8
import unittest

import time

import re

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.object_page.vanclass_student_info_page import StDetailPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.edit_text import DelEditText
from utils.toast_find import Toast


class VanclassMember(unittest.TestCase):
    """班级成员 - 学生详情页"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.st = StDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_member_detail(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                text = van[1].text
                van[1].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):

                    self.van.vanclass_member()  # 进入 班级成员
                    if self.detail.wait_check_page(text):  # 页面检查点
                        print('班级成员页面:')
                        self.detail.tips_operate(5)  # tips弹框

                        if self.home.empty_tips():
                            print('暂时没有数据')
                        else:
                            self.member_info_operate()  # 学生具体信息页面

                        if self.detail.wait_check_page(text):  # 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_vanclass_page(text):  # 班级详情 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_page():  # 班级 页面检查点
                                    self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 班级成员页面')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def member_info_operate(self):
        """班级成员- 学生具体信息页面"""
        st = self.detail.st_title()
        st[0].click()  # 进入学生 具体信息页面
        if self.st.wait_check_page():
            print('学生信息页面:')
            ele = self.st.all_element()
            print(ele[1][1])
            print(ele[1][2])
            print(ele[1][3], ':', ele[1][4])
            print(ele[1][5])
            print(ele[1][7])
            print(ele[1][9])
            print('---------------------------------')

            name = self.st.st_name()  # 备注名
            if self.st.judge_st_tags():  # 提分
                print(self.st.st_tags())
            nick = self.st.st_nickname()  # 昵称

            self.st.data_statistic()  # 数据统计
            if self.st.wait_check_data_page():
                self.st.st_commit_button()
                time.sleep(1)
                self.home.back_up_button()

                if self.st.wait_check_page():
                    self.picture_page_operate(nick)  # 拼图卡片

                    if self.st.wait_check_page():
                        self.hw_page_operate(name)  # 作业列表

                        if self.st.wait_check_page():
                            self.home.back_up_button()

    @teststeps
    def picture_page_operate(self, nick):
        """拼图卡片"""
        self.st.picture_count()  # 拼图
        if self.st.wait_check_picture_hw_page(nick[4:]):
            print(self.st.picture_report())  # 拼图报告
            if self.st.judge_picture():
                num = self.st.picture_num()
                print(num[0].text)
                self.home.back_up_button()

    @teststeps
    def hw_page_operate(self, name):
        """作业列表"""
        self.st.hw_count()  # 作业list
        if self.st.wait_check_picture_hw_page(name):

            self.home.back_up_button()
