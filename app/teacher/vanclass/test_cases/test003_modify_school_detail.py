#!/usr/bin/env python
# encoding:UTF-8
import re
import unittest

from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.test_data.create_vanclass_data import class_data
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class ModifySchool(unittest.TestCase):
    """修改学校名称"""

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
    def test_modify_school(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                name = self.van.vanclass_name()  # 班级名称
                text = name[0].text
                name[0].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):
                    print('班级%s的详情页:' % text)
                    ele = self.van.all_element()
                    school = ele[4].text  # 展示的学校名称

                    name = self.van.school_name_modify()
                    name.click()  # 进入学校名称修改页面
                    self.modify_school_operate(school, text)  # 修改学校名称
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def modify_school_operate(self, school, van):
        """
            修改学校名称 具体操作  --
            自由老师可修改保存；在编老师修改后保存不成功
        """
        if self.detail.wait_check_tips_page():  # 页面检查点
            button = self.detail.commit_button()  # 确定按钮
            if self.detail.enabled(button) is False:
                print('★★★ Error- 确定按钮不可点击')

            print('----------------------')
            self.detail.tips_title()  # 修改窗口title
            self.detail.tips_content()  # 修改窗口 提示信息

            var = self.detail.input()
            if var.text != school:
                print('★★★ Error- 学校名称展示有误', var.text, school)

            var.send_keys(class_data[4]['name'])
            length = len(class_data[4]['name'])
            print('学校名称修改为:', class_data[4]['name'])

            size = self.detail.character_num()  # 字符数
            size1 = re.findall(r'\d+(?#\D)', size)[0]
            size2 = re.findall(r'\d+(?#\D)', size)[1]
            if int(size2) != 30:
                print('★★★ Error- 最大字符数展示有误', size2)
            else:
                if length != int(size1):
                    print('★★★ Error- 字符数展示有误', size2)

            button = self.detail.commit_button()  # 确定按钮
            self.button_enbaled_judge(length, button, size1)
            button.click()  # 点击 确定按钮  进入班级详情页
            if self.van.wait_check_vanclass_page(van):  # 页面检查点
                Toast().find_toast('没有权限')
                print('----------------------')
                print('没有权限')
                self.home.back_up_button()
                if self.van.wait_check_page():  # 班级 页面检查点
                    self.home.click_tab_hw()  # 返回主界面

    @teststeps
    def button_enbaled_judge(self, length, button, size1):
        """确定按钮enabled状态"""
        if 0 <= length <= 30:
            if length != int(size1):
                print('★★★ Error- 字符数展示有误', length, size1)
            else:
                if self.detail.enabled(button) is False:
                    print('★★★ Error- 确定按钮不可点击')
        elif length > 30:
            if length != int(size1):
                print('★★★ Error- 字符数展示有误', length, size1)
            else:
                if self.detail.enabled(button) is True:
                    print('★★★ Error- 确定按钮未置灰可点击')
