#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.mine_recommend.object_page.mine_recommend import RecommendPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.question_bank.object_page.filter_page import FilterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class Recommend(unittest.TestCase):
    """我的推荐 -- 推荐列表"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.question = QuestionBankPage()
        cls.filter = FilterPage()
        cls.recommend = RecommendPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_recommend_list(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user.wait_check_page():  # 页面检查点
                self.user.click_mine_recommend()  # 点击 我的推荐
                if self.recommend.wait_check_page():  # 页面检查点
                    self.recommend.filter_button()  # 筛选按钮

                    if self.filter.wait_check_page():
                        name = self.filter.label_name()  # 所有标签
                        name[1].click()

                        ele = self.filter.filter_all_element()  # 所有元素
                        title = self.filter.label_title()  # 标签title
                        self.recommend.source_type_selected(ele, title)

                        self.filter.reset_button()  # 重置按钮
                        self.filter.commit_button()  # 确定按钮

                        if self.recommend.wait_check_page():
                            self.recommend.back_up_button()  # 点击 返回按钮
                else:
                    print('未进入 我的收藏 页面')
                if self.user.wait_check_page():  # 页面检查点
                    self.home.click_tab_hw()  # 回首页
            else:
                print('未进入个人中心页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
