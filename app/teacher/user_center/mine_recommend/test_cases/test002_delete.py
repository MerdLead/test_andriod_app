#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time
from app.teacher.homework.object_page.release_hw_page import ReleasePage
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
    """我的推荐 -- 删除"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.filter = FilterPage()
        cls.question = QuestionBankPage()
        cls.recommend = RecommendPage()
        cls.release = ReleasePage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_recommend_delete(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user.wait_check_page():  # 页面检查点
                self.user.click_mine_recommend()  # 点击 我的推荐
                if self.recommend.wait_check_page():  # 页面检查点
                    self.recommend.menu_button(0)  # 右侧菜单按钮
                    time.sleep(1)
                    print('删除推荐:')
                    self.release.tips_operate()

                    if self.recommend.wait_check_page():
                        self.home.back_up_button()
                        if self.user.wait_check_page():  # 页面检查点
                            self.home.click_tab_hw()  # 回首页
                            # todo 验证
                else:
                    print('未进入 我的推荐 页面')
            else:
                print('未进入个人中心页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
