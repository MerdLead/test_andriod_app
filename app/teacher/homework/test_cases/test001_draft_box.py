#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class DraftBox(unittest.TestCase):
    """作业 - 草稿箱"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.release = ReleasePage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_draft_box(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.draft_box_button()  # 草稿箱 按钮
            if self.home.wait_check_drat_page():  # 页面检查点
                if self.home.empty_tips():
                    print('暂无数据')
                    self.home.back_up_button()  # 返回按钮
                    self.home.click_tab_hw()  # 返回首页
                else:
                    print('----------------------------------------')
                    print('所有草稿:')

                    content = []
                    name = []
                    ele = self.home.all_element()
                    for i in range(1, len(ele) - 2, 4):
                        print(ele[i].text, '\n',
                              ele[i + 1].text, '\n',
                              ele[i + 2].text)
                        print('------------------')
                        content.append(ele[i + 3])
                        name.append(ele[i].text)

                    self.draft_box_operate(content)  # 草稿箱 草稿详情页具体操作

                    if self.home.wait_check_page():  # 主页面检查点
                        # todo 作业list第一个
                        self.home.draft_box_button()  # 草稿箱 按钮
                        if self.home.wait_check_drat_page():  # 页面检查点
                            content1 = []
                            name1 = []
                            ele = self.home.all_element()
                            for i in range(1, len(ele) - 2, 4):
                                content1.append(ele[i + 3])
                                name1.append(ele[i].text)

                            if name[0] == name1[0]:
                                print('★★★ Error- 布置作业失败')

                            time.sleep(2)
                            self.home.back_up_button()  # 返回按钮
                            if self.home.wait_check_page():  # 主页面检查点
                                self.home.click_tab_hw()  # 返回首页
                        else:
                            print('未进入草稿箱')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def draft_box_operate(self, content):
        """草稿 详情页"""
        content[0].click()  # 进去第一个草稿
        self.release.tips_operate()  # 温馨提示 页面

        if self.release.wait_check_release_page():  # 页面检查点
            print('----------------------------')
            ele = self.home.all_element()
            title = self.release.hw_title()
            name = self.release.hw_name_edit()
            print(title, ":", name.text)  # 打印元素 作业名称

            # name.send_keys('345综合测试')
            print(ele[2].text, ":", ele[3].text)  # 打印元素 题目列表

            mode = self.release.hw_mode_operate(ele)  # 作业模式 操作
            mode[0].click()  # 选择 自由模式
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
                    button = self.release.put_into_button()  # 存入草稿 按钮
                    if self.release.enabled(button) is True:
                        print('★★★ Error- 存入草稿 按钮未置灰')
                    else:
                        self.release.now_assign_button()  # 立即布置 按钮
                        self.release.tips_page_info()
                else:
                    print('未返回 发布作业 页面')
            else:
                print('未返回 发布作业 页面')
        else:
            print('未进入 发布作业 页面')

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
