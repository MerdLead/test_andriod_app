# coding=utf-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class AppTask(unittest.TestCase):

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()

    @classmethod
    @teardown
    def tearDown(cls):
        """"""
        pass

    @testcase
    def test_login_failed(self):
        """判断登录状态，若failed则获取toast"""
        self.login.login()

        if self.home.wait_check_page():
            print('登录成功!!!')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print(' fail login ')
