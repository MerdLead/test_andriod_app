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


class ModifyVanclass(unittest.TestCase):
    """修改班级名称"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.van = VanclassPage()
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_modify_class(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                name = self.van.vanclass_name()  # 班级名称
                text = name[0].text
                name[0].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):
                    ele = self.van.all_element()
                    print(ele[1].text, ':', ele[2].text)
                    print(ele[3].text, ':', ele[4].text)
                    for i in range(5, len(ele)):
                        if ele[i].text != '':
                            print(ele[i].text)

                    if ele[2].text != text:
                        print('★★★ Error- 班级名称展示有误', ele[2].text, text)

                    if len(ele)-4 != 17:
                        print('★★★ Error- 班级详情页面元素缺失', len(ele)-4)

                    name = self.van.class_name_modify()
                    name.click()  # 进入班级名称修改页面
                    self.modify_vanclass_operate(text)  # 修改班级名称

                    if self.van.wait_check_vanclass_page(text):
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def modify_vanclass_operate(self, name):
        """修改班级名称 具体操作"""
        if self.detail.wait_check_tips_page():  # 页面检查点
            button = self.detail.commit_button()  # 确定按钮
            if self.detail.enabled(button) is False:
                print('★★★ Error- 确定按钮不可点击')

            print('----------------------')
            self.detail.tips_title()  # 修改窗口title
            self.detail.tips_content()  # 修改窗口 提示信息

            var = self.detail.input()
            if var.text != name:
                print('★★★ Error- 班级名称展示有误')

            for i in range(len(class_data)):
                var = self.detail.input()
                var.send_keys(class_data[i]['name'])
                length = len(class_data[i]['name'])
                print('班级名称修改为:', class_data[i]['name'])

                size = self.detail.character_num()  # 字符数
                size1 = re.findall(r'\d+(?#\D)', size)[0]
                size2 = re.findall(r'\d+(?#\D)', size)[1]
                if int(size2) != 30:
                    print('★★★ Error- 最大字符数展示有误', size2)
                else:
                    if length != int(size1):
                        print('★★★ Error- 字符数展示有误', size2)

                button = self.detail.commit_button()  # 确定按钮
                status = self.detail.button_enbaled_judge(length, button, size1)
                print(status)
                if status == 'true':  # 可点击
                    button.click()  # 点击 确定按钮  进入班级详情页
                    if i != len(class_data)-1:
                        if self.van.wait_check_vanclass_page(class_data[i]['name']):  # 页面检查点
                            van = self.van.class_name_modify()
                            item = van.text
                            if class_data[i]['name'] != item:
                                print('★★★ Error- 班级名称修改后展示有误', class_data[i]['name'], item)

                            van.click()  # 进入班级名称修改页面
                            if self.detail.wait_check_tips_page():  # 页面检查点
                                button = self.detail.commit_button()  # 确定按钮
                                if self.detail.enabled(button) is False:
                                    print('★★★ Error- 确定按钮不可点击')
                    else:  # 最后一个数据
                        # todo 获取toast
                        if self.van.wait_check_vanclass_page(class_data[i-1]['name']):  # 页面检查点
                            if class_data[i]['name'] == item:
                                print('★★★ Error- 班级名称不可重复功能有误', class_data[i]['name'], item)
                            self.home.back_up_button()
                print('--------------------------------')
