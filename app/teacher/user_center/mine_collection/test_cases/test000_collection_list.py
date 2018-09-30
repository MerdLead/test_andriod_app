#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.question_bank.object_page.question_basket_page import QuestionBasketPage
from app.teacher.question_bank.object_page.question_detail_page import QuestionDetailPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.question_bank.object_page.filter_page import FilterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.user_center.mine_collection.object_page.mine_collect import CollectionPage
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class Collection(unittest.TestCase):
    """我的收藏 -- 列表"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.filter = FilterPage()
        cls.collect = CollectionPage()
        cls.question = QuestionBankPage()
        cls.basket = QuestionBasketPage()
        cls.detail = QuestionDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_collection_list(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user.wait_check_page():  # 页面检查点
                self.user.click_mine_collect()  # 点击 我的收藏
                if self.collect.wait_check_page():  # 页面检查点
                    name = self.question.question_name()
                    author = self.question.question_author_index()
                    for i in range(len(author)):
                        mode = self.question.question_type(i)
                        num = self.question.question_num(i)
                        print(mode, '\n', name[1][i], '\n', num, '\n', author[i].text)
                        print('------------------------------------')

                    self.question.question_basket()
                    if self.basket.wait_check_page():  # 页面检查点
                        self.home.back_up_button()

                    if self.collect.wait_check_page():  # 页面检查点
                        name[0][0].click()
                        if self.detail.wait_check_page():  # 页面检查点
                            self.home.back_up_button()
                            if self.collect.wait_check_page():  # 页面检查点
                                self.home.back_up_button()  # 点击 返回按钮
                else:
                    print('未进入 我的收藏 页面')

                if self.user.wait_check_page():  # 页面检查点
                    self.home.click_tab_hw()  # 回首页
            else:
                print('未进入个人中心页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
