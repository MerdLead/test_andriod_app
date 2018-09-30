# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class AppTask(unittest.TestCase):

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()

    @classmethod
    @teardown
    def tearDown(cls):
        """"""
        pass

    @testcase
    def test_login_failed(self):
        """判断登录状态，若failed则获取toast"""
        print('登录啦')
        self.login_page.login()
        activity = self.login_page.wait_activity()

        # self.assertEqual(self.home_page.wait_check_page(), u"试卷")

        if activity == 'com.vanthink.vanthinkstudent.v2.ui.home.HomeActivity':
            print('登录成功!!!')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print(' fail login ')
