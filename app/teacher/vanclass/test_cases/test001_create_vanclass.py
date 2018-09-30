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


class CreateVanclass(unittest.TestCase):
    """创建班级"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.van = VanclassPage()
        cls.detail = VanclassDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_create_class(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                if self.van.empty_tips():  # 暂无数据
                    print('暂无班级')
                else:  # 已有班级
                    self.vanclass_statistic_operate()  # 已有班级数 统计

                    for i in range(len(class_data)):
                        self.van.add_class_button()  # 创建班级 按钮
                        self.create_vanclass_operate(i)  # 创建班级 具体操作

                    if self.van.wait_check_page():  # 页面检查点
                        self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
            
    @teststeps
    def vanclass_statistic_operate(self):
        """已有班级数 统计"""
        print('已有班级:')
        name = self.van.vanclass_name()  # 班级名称
        num = self.van.vanclass_no()  # 班号
        count = self.van.st_count()  # 学生人数

        if len(num) > 9:  # 多于一页
            if len(name) != len(num) != len(count):
                if len(count) != len(name) - 1:
                    if len(count) != len(name) + 1:
                        print('★★★ Error- 班级数、班号数、学生人数有误')
        else:
            if len(name) != len(num) != len(count):
                print('★★★ Error- 班级数、班号数、学生人数有误')

        print('----------------------')
        for i in range(len(num)):
            print(name[i].text, '  ', num[i].text, '  学生人数:', count[i].text)

    @teststeps
    def create_vanclass_operate(self, i):
        """创建班级 具体操作"""
        if self.detail.wait_check_tips_page():  # 页面检查点
            button = self.detail.commit_button()  # 确定按钮
            if i == 0:
                if self.detail.enabled(button) is 'true':
                    print('★★★ Error- 确定按钮未置灰')
            else:
                if self.detail.enabled(button) is 'false':
                    print('★★★ Error- 确定按钮不可点击')

            print('----------------------')
            self.detail.tips_title()  # 修改窗口title
            self.detail.tips_content()  # 修改窗口 提示信息

            var = self.detail.input()
            var.send_keys(class_data[i]['name'])
            length = len(class_data[i]['name'])
            print('创建班级:', class_data[i]['name'])

            size = self.detail.character_num()  # 字符数
            size1 = re.findall(r'\d+(?#\D)', size)[0]
            size2 = re.findall(r'\d+(?#\D)', size)[1]

            if int(size2) != 30:
                print('★★★ Error- 最大字符数展示有误', size2)

            button = self.detail.commit_button()  # 确定按钮
            status = self.detail.button_enbaled_judge(length, button, size1)
            if status == 'true':  # 可点击
                self.detail.click_block()  # 点击空白处取消创建
                # button.click()  # 点击 确定按钮  进入班级详情页
                # if i != len(class_data) - 1:
                #     if self.van.wait_check_vanclass_page(class_data[i]['name']):  # 页面检查点
                #         van = self.van.class_name_modify()
                #         item = van.text
                #         if class_data[i]['name'] != item:
                #             print('★★★ Error- 班级名称修改后展示有误', class_data[i]['name'], item)
                #
                #         van.click()  # 进入班级名称修改页面
                #         if self.detail.wait_check_tips_page():  # 页面检查点
                #             button = self.detail.commit_button()  # 确定按钮
                #             if self.detail.enabled(button) is False:
                #                 print('★★★ Error- 确定按钮不可点击')
                # else:  # 最后一个数据
                #     # todo 获取toast
                #     if self.van.wait_check_vanclass_page(class_data[i - 1]['name']):  # 页面检查点
                #         if class_data[i]['name'] == item:
                #             print('★★★ Error- 班级名称不可重复功能有误', class_data[i]['name'], item)
                #         self.home.back_up_button()
                #         if self.van.wait_check_page():  # 班级 页面检查点
                #             self.home.click_tab_hw()  # 返回主界面
            else:
                self.detail.click_block()
