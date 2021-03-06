# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.user_center.object_page.user_center_page import UserCenterPage, Setting, QuestionFeedback
from conf.decorator import setupclass, teardownclass, testcase
from utils.toast_find import Toast


class ProblemFeedback(unittest.TestCase):
    """问题反馈"""
    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.user_center = UserCenterPage()
        cls.setting = Setting()
        cls.question_feedback = QuestionFeedback()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_question_feedback(self):
        """问题反馈 -- 正常流程"""
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            self.home_page.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user_center.wait_check_page():  # 页面检查点
                self.user_center.click_setting()  # 进入设置页面
                if self.setting.wait_check_page():
                    self.setting.question_feedback()  # 进入问题反馈页面

                    if self.question_feedback.wait_check_page():
                        self.question_feedback.edit_text().send_keys("123vxc567")
                        self.question_feedback.submit_button()

                        if self.setting.wait_check_page():
                            print('submit question success')

                        else:
                            print(' failed to submit question ')

                        self.setting.back_up()  # 返回主界面
                    else:
                        print("未进入问题反馈页面")
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
