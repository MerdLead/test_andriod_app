# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.user_center.object_page.user_center_page import UserCenterPage, Setting, ProtocolPage
from conf.base_page import BasePage
from conf.decorator import setupclass, teardownclass, testcase
from utils.toast_find import Toast


class RegisterProtocol(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.user_center = UserCenterPage()
        cls.setting = Setting()
        cls.protocol = ProtocolPage()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_register_protocol(self):
        """注册协议 -- 正常流程"""
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():
            self.home_page.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user_center.wait_check_page():  # 页面检查点
                self.user_center.click_setting()  # 进入设置页面
                if self.setting.wait_check_page():

                    self.setting.regist_protocol()  # 进入注册协议页面

                    if self.protocol.wait_check_page():  # 页面检查点
                        for i in range(4):
                            print('翻页%s次' % (i + 1))
                            BasePage().screen_swipe_up(0.5, 0.5, 0.25, 1000)
                        print('下拉一次')
                        BasePage().screen_swipe_down(0.5, 0.05, 0.9, 1000)
                        self.home_page.back_up_button()

                        if self.setting.wait_check_page():  # 页面检查点
                            print('success')
                        else:
                            print(' failed  ')
                        self.setting.back_up()  # 返回主界面
                    else:
                        print('未进入注册协议页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
