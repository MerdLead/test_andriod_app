#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.test_data.search_content import search_data
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class BankSearch(unittest.TestCase):
    """题库 -搜索 -历史搜索词最多15条"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.question = QuestionBankPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_search_history(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('题单'):  # 页面检查点
                box = self.question.search_box()  # 搜索框
                box.click()

                if self.question.wait_check_page('资源'):
                    print('搜索内容：', search_data[0]['resource'])
                    box = self.question.search_box()  # 搜索框
                    box.send_keys(search_data[0]['resource'])  # 输入搜索内容
                    self.question.search_button()  # 搜索按钮

                    if self.question.wait_check_game_type_page():  # 页面检查点
                        box = self.question.search_box()  # 搜索框
                        box.click()

                        if self.question.wait_check_page('资源'):
                            self.home.back_up_button()  # 由于一次不能展示在历史搜索词列表里，故切换一次页面
                            if self.question.wait_check_page('资源'):
                                word = self.question.history_search()  # 历史搜索词
                                print('历史搜索条数:', len(word[1]))

                                box = self.question.search_box()  # 搜索框
                                box.click()

                                print('搜索内容：', search_data[1]['resource'])
                                print('---------------------')
                                box.send_keys(search_data[0]['resource'])  # 输入搜索内容
                                self.question.search_button()  # 搜索按钮

                                if self.question.wait_check_game_type_page():  # 页面检查点
                                    if self.home.empty_tips():
                                        print('暂无数据 再次刷新')

                                    box = self.question.search_box()  # 搜索框
                                    box.click()
                                    if self.question.wait_check_page('资源'):
                                        self.home.back_up_button()  # 由于一次不能展示在历史搜索词列表里，故切换一次页面
                                        if self.question.wait_check_page('资源'):

                                            word = self.question.history_search()  # 历史搜索词
                                            if len(word[1]) != 15:
                                                print('历史搜索最多15条')

                                            self.home.back_up_button()  # 返回 题库 界面
                    else:
                        print('未进入 搜索结果 页面')
                else:
                    print('未进入 搜索 界面')
                    self.home.back_up_button()  # 返回 题库 界面
            else:
                print('未进入题库页面')

            self.home.click_tab_hw()  # 返回首页
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print('未进入主界面')
