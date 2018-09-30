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
    """题库 -- 搜索 -资源"""

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
    def test_search_resource(self):
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
                        name = self.question.question_name()  # 搜索到的资源 - 题目名称
                        box = self.question.search_box()  # 搜索框
                        box.click()

                        if self.question.wait_check_page('资源'):
                            ele = self.question.drop_down_button()  # 下拉按钮
                            ele[0].click()

                            time.sleep(2)
                            var = self.question.search_criteria_menu()  # 搜索条件菜单
                            self.question.choose_condition(var)
                            var[0].click()  # 选择 资源
                            time.sleep(2)

                            box = self.question.search_box()  # 搜索框
                            box.click()
                            ele1 = self.question.drop_down_button()  # 下拉按钮

                            print('搜索内容：', search_data[0]['resource'])
                            print('---------------------')
                            box.send_keys(search_data[0]['resource'])  # 输入搜索内容
                            self.question.search_button()  # 搜索按钮

                            if self.question.wait_check_game_type_page():  # 页面检查点
                                name1 = self.question.question_name()  # 搜索到的资源 - 题目名称

                                box = self.question.search_box()  # 搜索框
                                box.click()
                                if self.question.wait_check_page('资源'):
                                    ele2 = self.question.drop_down_button()  # 下拉按钮

                                    content = self.question.history_search()  # 历史搜索词
                                    if search_data[0]['resource'] not in content[1]:
                                        self.question.screen_swipe_up(0.5, 0.5, 0.15)  # 滑屏

                                    word = self.question.history_search()  # 历史搜索词
                                    for i in range(len(word[1])):
                                        if word[1][i] == search_data[0]['resource']:
                                            word[0][i].click()  # 点击该历史搜索词
                                            break

                                    if self.question.wait_check_game_type_page():
                                        name2 = self.question.question_name()  # 搜索到的资源 - 题目名称

                                        if ele1[1] != ele2[1]:
                                            print('★★★ Error-搜索条件不一致', ele1[1], ele2[1])

                                        if name[1] != name1[1] != name2[1]:
                                            print('★★★ Error-两次搜索内容不一致', name[1], name1[1], name2[1])
                    else:
                        print('未进入 搜索结果 页面')
                else:
                    print('未进入 搜索 界面')
                    self.home.back_up_button()  # 返回
            else:
                print('未进入题库页面')

            self.home.click_tab_hw()  # 返回首页
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print('未进入主界面')
