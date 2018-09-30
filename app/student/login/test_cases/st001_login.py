# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.user_center.object_page.user_center_page import Setting
from conf.decorator import teardown, testcase, setup
from utils.toast_find import Toast


class Login(unittest.TestCase):

    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动Appium服务，则需要在该方法内启动Appium服务。
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.setting = Setting()

    # tearDown（）方法用于测试用例执行之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后才执行
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    # 具体的测试用例，必须要以test开头
    @testcase
    def test_login(self):
        """判断登录状态，若failed则获取toast"""
        self.login_page.app_status()
        if self.home_page.wait_check_page() == "试卷":
            self.setting.logout()
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print('login failed ')
