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
    """班级成员"""

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
    def test_vanclass_member(self):
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
                            self.member_list_operate()  # 具体操作
                            self.menu_operate()  # 学生 左键长按

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
    def member_list_operate(self):
        """班级成员 页面具体操作"""
        st = self.detail.st_title()
        phone = self.detail.st_phone()

        if len(phone) < 7:  # 少于7个
            if len(st) != len(phone):
                print('★★★ Error- 学生、手机号个数不等')
            else:

                for i in range(len(st)):
                    print(' 学生:', st[i].text, '\n', "手机号:", phone[i].text)
                    self.judge_phone(phone[i].text)  # 验证手机号格式
                    print('-----------------------')
        else:  # 多于8个 todo 多于7个翻页
            print('todo 多于7个翻页:', len(phone))
            for i in range(7):
                print(' 学生:', st[i].text, '\n', "手机号:", phone[i].text)
                self.judge_phone(phone[i].text)  # 验证手机号格式
                print('-----------------------')
        print('---------------------------------')

    @teststeps
    def judge_phone(self, var):
        """验证 手机号格式 （中间4位显示成*）"""
        var1 = var[:3] + var[7:]

        if not self.isDigit(var1):
            print('★★★ Error- 其他部分不为数字', var)
        if var[3:7] != '****':
            print('★★★ Error- 中间4位未显示成*', var)

    @teststeps
    def isDigit(self, var):
        try:
            var = int(var)
            return isinstance(var, int)
        except ValueError:
            return False

    @teststeps
    def menu_operate(self):
        """学生条目 左键长按菜单"""
        st = self.detail.st_title()
        self.detail.open_menu(st[1])  # 学生条目 左键长按

        self.detail.menu_item(1)  # 修改备注名
        if self.detail.wait_check_tips_page():
            self.detail.tips_title()  # 修改窗口title
            var = self.detail.input()
            DelEditText().del_text(var)
            var.send_keys('SFF0821')
            print('修改为:', 'SFF0821')
            print('----------------------')
            self.detail.character_num()
            button = self.detail.commit_button()
            if self.detail.selected(button):
                button.click()  # 点击确定按钮

        # st = self.detail.st_title()
        # self.detail.open_menu(st[1])  # 学生条目 左键长按
        # self.detail.menu_item(0)  # 修改备注名
