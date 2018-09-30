#!/usr/bin/env python
# encoding:UTF-8
import unittest
import re

import time

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.vanclass.object_page.vanclass_group_manage_page import GroupDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.test_data.create_vanclass_data import class_data
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class GroupManage(unittest.TestCase):
    """小组管理"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.group = GroupDetailPage()
        cls.release = ReleasePage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_group_manage(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                text = van[3].text
                van[3].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):  # class two

                    self.van.group_manage()  # 进入 小组管理
                    if self.group.wait_check_page(text):  # 页面检查点
                        print('小组管理页面:')
                        time.sleep(3)
                        if self.home.empty_tips():
                            print('暂时没有数据')
                        else:
                            name = self.group.group_name()  # 名字
                            for i in range(len(name)):
                                if self.group.wait_check_page(text):  # 页面检查点
                                    name = self.group.group_name()  # 名字
                                    group_name = name[0].text
                                    name[0].click()  # 进入小组详情页
                                    if self.group.wait_check_page(group_name):
                                        self.group.delete_button()
                                        self.release.tips_operate()
                                        print('---------------------------')

                        if self.group.wait_check_page(text):
                            for i in range(len(class_data)):
                                self.detail.add_group()  # 添加 小组按钮
                                self.create_group_operate(i, text)  # 创建小组 具体操作

                            if self.group.wait_check_page(text):
                                self.group_manage_operate()  # 具体操作
                                self.group_detail_operate()  # 小组 详情页面

                                if self.group.wait_check_page(text):  # 页面检查点
                                    self.home.back_up_button()
                                    if self.van.wait_check_vanclass_page(text):  # 班级详情 页面检查点
                                        self.home.back_up_button()
                                        if self.van.wait_check_page():  # 班级 页面检查点
                                            self.home.click_tab_hw()  # 返回主界面
                else:
                    print('未进入 班级详情页面')
                    self.home.back_up_button()
                    if self.van.wait_check_page():  # 班级 页面检查点
                        self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def group_manage_operate(self):
        """小组管理 页面具体操作"""
        name = self.group.group_name()  # 名字
        count = self.group.st_count()  # 学生人数

        if len(name) < 10:  # 少于10个
            if len(name) != len(count):
                print('★★★ Error- 小组name、学生人数 个数不等')
            else:
                for i in range(len(name)):
                    print('  ', name[i].text, count[i].text)
                print('------------------')
        else:  # 多于8个 todo 多于7个翻页
            print('todo 多于7个翻页:', len(name))
            for i in range(9):
                print('  ', name[i].text, count[i].text)
        print('------------------')

    @teststeps
    def group_detail_operate(self):
        """小组 详情页面具体操作"""
        name = self.group.group_name()  # 名字
        count = self.group.st_count()  # 学生人数
        # for i in range(len(name)):
        #     if count[i].text != 0:
        #         name[i].click()
        print('小组:', name[0].text, '学生人数:', count[0].text)
        var = name[0].text
        name[0].click()

        if self.group.wait_check_page(var):
            self.group.edit_button()  # 编辑 按钮
            if self.detail.wait_check_tips_page():
                self.detail.tips_title()
                modify = self.detail.input()
                print(modify.text)
                print('--------------------')
                self.group.commit_button()

        if self.group.wait_check_page(var):
            self.group.delete_button()  # 删除按钮
            if self.detail.wait_check_tips_page():
                self.detail.tips_title()
                self.detail.tips_content()
                self.group.cancel_button()

        self.home.back_up_button()

    @teststeps
    def create_group_operate(self, i, van):
        """创建小组 具体操作"""
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
                button.click()  # 点击 确定按钮  进入小组管理 页面

                if self.detail.wait_check_page(van):  # 页面检查点
                    if i != len(class_data) - 1:
                        if self.van.wait_check_vanclass_page(class_data[i]['name']):  # 页面检查点
                            group = self.group.group_name()  # todo
                            item = group[0].text
                            if class_data[i]['name'] != item:
                                print('★★★ Error- 班级名称修改后展示有误', class_data[i]['name'], item)

                            # group[0].click()  # 进入班级名称修改页面
                            # if self.detail.wait_check_tips_page():  # 页面检查点
                            #     button = self.detail.commit_button()  # 确定按钮
                            #     if self.detail.enabled(button) is False:
                            #         print('★★★ Error- 确定按钮不可点击')
                    else:  # 最后一个数据
                        # todo 获取toast
                        if self.van.wait_check_vanclass_page(class_data[i - 1]['name']):  # 页面检查点
                            group = self.group.group_name()  # todo
                            item = group[0].text
                            if class_data[i]['name'] != item:
                                print('★★★ Error- 班级名称不可重复功能有误', class_data[i]['name'], item)
            else:
                self.detail.click_block()
