#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Homework(unittest.TestCase):
    """作业 更多按钮"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.release = ReleasePage()
        cls.detail = HwDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_hw_more_button(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            if self.home.wait_check_no_page():
                print('无最新动态 -- (用户指南) 欢迎使用在线助教,打开看看吧!')
            else:
                name = self.home.get_type('习题')
                var = name[0][name[1][0]].text  # 作业名称
                name[0][name[1][0]].click()  # 进入作业

                if self.detail.wait_check_page():  # 页面检查点
                    print('进入作业:', var)
                    self.detail.more_button()  # 更多 按钮
                    time.sleep(2)
                    self.detail.edit_delete_button(0)  # 编辑按钮
                    if self.detail.wait_check_edit_page():  # 页面检查点
                        self.edit_hw_operate()

                    if self.detail.wait_check_page():  # 页面检查点
                        self.detail.more_button()  # 更多 按钮
                        time.sleep(2)
                        self.detail.edit_delete_button(1)  # 删除按钮
                        self.tips_page_info()  # 删除提示框

                        if self.detail.wait_check_page():  # 页面检查点
                            self.home.back_up_button()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def edit_hw_operate(self):
        """编辑作业 详情页"""
        self.release.tips_operate()  # 温馨提示 页面

        if self.detail.wait_check_edit_page():  # 页面检查点
            print('----------------------------')
            ele = self.home.all_element()
            title = self.release.hw_title()
            name = self.release.hw_name_edit()

            name.send_keys('测试345')  # 修改name
            print(title, ":", name.text)  # 打印元素 作业名称

            print(ele[2].text, ":", ele[3].text)  # 打印元素 题目列表

            self.release.hw_mode_operate(ele)  # 作业模式 操作
            print(ele[6].text)  # 打印元素 发布作业到

            # self.release.screen_swipe_up(0.5, 0.8, 0.2, 1000)
            van = self.release.van_name()  # 班级名
            button = self.release.choose_button()  # 单选
            count = self.release.choose_count()  # 班级描述

            vanclass = []
            if len(button) != len(van):
                print('★★★ Error- 单选框的个数与班级个数不同', len(button), len(van))
            else:
                for i in range(len(count)):
                    print(van[i].text, '\n',
                          count[i].text)
                    print('-------')
                    vanclass.append(van[i].text)

            self.release.hw_adjust_order()  # 调整题目顺序
            self.release.confirm_button()  # 确定按钮

            if self.release.wait_check_release_page():  # 页面检查点
                self.choose_class_operate(van, vanclass)  # 选择班级 学生

                if self.release.wait_check_release_page():  # 页面检查点
                    self.detail.cancel_button()  # 取消编辑 按钮

    @teststeps
    def choose_class_operate(self, van, vanclass):
        """选择班级 学生"""
        print('----------------------------')
        button = self.release.choose_button()
        print('所选择的班级:', '\n',
              vanclass[0])
        button[0].click()  # 选择一个班

        van[1].click()  # 进入第二个班级
        print('-----------------', '\n',
              vanclass[1])
        if self.release.wait_check_class_page(vanclass[1]):
            st = self.release.st_title()  # 学生
            phone = self.release.st_phone()  # 手机号
            for i in range(len(phone)):
                print('  ', st[i].text, phone[i].text)
            print('------------------')

            button = self.release.choose_button()
            button[0].click()  # 选择一个学生
            self.release.confirm_button()  # 确定按钮

    @teststeps
    def tips_page_info(self):
        """温馨提示 页面信息"""
        print('------------------------------------------')
        print('删除提示 页面:')

        if self.detail.wait_check_tips_page():
            self.release.tips_title()
            self.release.tips_content()
            self.release.cancel_button()  # 取消按钮
        else:
            print('★★★ Error- 无删除提示框')
