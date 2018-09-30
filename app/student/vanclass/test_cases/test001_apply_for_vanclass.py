#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.student.vanclass.object_page.vanclass_page import VanclassPage
from app.student.vanclass.test_data.remark_name_data import name_data
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class ApplyVanclass(unittest.TestCase):
    """申请 入班"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = LoginPage()
        cls.home = HomePage()
        cls.van = VanclassPage()
        cls.detail = VanclassDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_apply_for_vanclass(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                if self.van.empty_tips():  # 暂无数据
                    print('暂无班级')
                else:  # 已有班级
                    self.vanclass_statistic_operate()  # 已有班级数 统计

                    for i in range(len(name_data)):
                        if self.van.wait_check_page():  # 页面检查点
                            self.van.add_class_button()  # 添加班级 按钮
                            self.apply_vanclass_operate(i)  # 申请入班 具体操作

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
        print('----------------------')

    @teststeps
    def apply_vanclass_operate(self, i):
        """申请班级 具体操作"""
        if self.detail.wait_check_tips_page():  # 页面检查点
            self.detail.tips_title()  # 修改窗口title
            button = self.detail.commit_button()  # 确定按钮
            if self.detail.enabled(button) is 'true':
                print('★★★ Error- 确定按钮未置灰')

            var = self.detail.input()
            var.send_keys('9235')
            print('9235')

            self.detail.commit_button().click()  # 点击确定按钮
            if self.van.wait_check_apply_page():
                if self.van.status_error_hint():
                    print('班级不存在 点击屏幕 重新加载')
                    self.home.back_up_button()  # 返回
                else:
                    if i == 0:
                        ele = self.van.all_element()
                        print(ele[1][1], self.van.class_name_modify())
                        print(ele[1][3], self.van.apply_vanclass_no())
                        print(ele[1][5], self.van.apply_teacher_name())

                    remark = self.van.remark_name_modify()  # 备注名
                    remark.click()
                    remark.send_keys(name_data[i]['name'])
                    print('填入的备注名是:', name_data[i]['name'])
                    self.van.apply_class_button()  # 申请入班 按钮
                    time.sleep(1)

                    if self.van.wait_check_apply_page(5):  # 页面检查点
                        Toast().find_toast(name_data[i]['assert'])
                        self.home.back_up_button()
                    elif self.van.wait_check_page():  # 页面检查点
                        num = self.van.vanclass_no()[-1].text  # 班号
                        count = self.van.st_count()  # 学生人数

                        if count[-1].text == '申请中':
                            if num[3:] != '9235':
                                print('★★★ Error- 申请班号 信息不符', num[3:])
                            else:
                                count[-1].click()  # 删除申请信息
                                if self.detail.wait_check_tips_page():  # tips弹框 检查点
                                    self.detail.tips_title()
                                    self.detail.commit_button().click()
                        else:
                            print('★★★ Error- 无申请信息')
            print('------------------------------')

