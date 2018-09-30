#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.vanclass.object_page.vanclass_group_manage_page import GroupDetailPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class InviteStudent(unittest.TestCase):
    """邀请学生"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.group = GroupDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_invite_student(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                text = van[3].text
                van[3].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):  # class two
                    self.van.invite_st_button()  # 邀请学生按钮
                    if self.van.wait_check_tips_page():
                        self.van.tips_title()
                        self.van.tips_content()

                        self.van.copy_link_button()  # 复制链接
                        Toast().find_toast('班级链接已复制到粘贴板')

                        if self.van.wait_check_vanclass_page(text):  # class two
                            self.van.invite_st_button()  # 邀请学生按钮
                            if self.van.wait_check_tips_page():
                                self.van.copy_no_button()  # 复制班号
                                Toast().find_toast('班号已复制到粘贴板')

                        # self.share_operate(text)  # 分享 具体操作

                    self.home.back_up_button()
                    if self.van.wait_check_page():  # 班级 页面检查点
                        self.home.click_tab_hw()  # 返回主界面
                else:
                    print('未进入 入班详情页面')
                    self.home.back_up_button()
                    if self.van.wait_check_page():  # 班级 页面检查点
                        self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def share_operate(self, text):
        """分享"""
        if self.van.wait_check_vanclass_page(text):  # class two
            self.van.invite_st_button()  # 邀请学生按钮
            if self.van.wait_check_tips_page():

                self.van.share_button()  # 分享按钮
                if self.van.wait_check_share_tips_page():
                    self.van.share_title()
                    self.van.share_content()

                    self.detail.click_block()
