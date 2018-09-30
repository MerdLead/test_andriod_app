#!/usr/bin/env python
# encoding:UTF-8
import random
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.question_bank.object_page.filter_page import FilterPage
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class QuestionFilter(unittest.TestCase):
    """题库 -- 筛选"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.question = QuestionBankPage()
        cls.filter = FilterPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_filter_choose(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('搜索'):  # 页面检查点
                self.question.filter_button()  # 筛选按钮

                if self.filter.wait_check_page():  # 页面检查点
                    if self.filter.selected(self.filter.game_list()) == 'false':  # 大题
                        self.filter.click_game_list()  # 选择大题

                        if self.filter.wait_check_page():  # 页面检查点
                            ele = self.filter.filter_all_element()  # 所有元素
                            title = self.filter.label_title()  # 标签title
                            name = self.filter.label_name()  # 所有标签
                            self.filter.source_type_selected(ele, title)
                            var = name[9].text
                            name[9].click()  # 选择一个标签  词汇选择
                            self.filter.commit_button()  # 确定按钮

                            if self.question.wait_check_page('搜索'):  # 页面检查点
                                name = self.question.question_name()
                                mode = self.question.question_type(random.randint(0, len(name)-1))  # 大题类型
                                if mode != var:
                                    print('★★★ Error- 筛选出的大题类型')

                                self.home.click_tab_hw()  # 返回首页
            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
