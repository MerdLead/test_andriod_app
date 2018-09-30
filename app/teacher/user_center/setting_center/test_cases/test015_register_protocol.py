# coding=utf-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage, ProtocolPage
from app.teacher.user_center.setting_center.object_page.setting_page import SettingPage
from conf.basepage import BasePage
from conf.decorator import setupclass, teardownclass, testcase
from utils.toast_find import Toast


class RegisterProtocol(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.setting = SettingPage()
        cls.protocol = ProtocolPage()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_register_protocol(self):
        """注册协议 -- 正常流程"""
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()   # 进入首页后点击‘个人中心’按钮

            if self.user.wait_check_page():  # 页面检查点
                self.user.click_setting()  # 进入设置页面

                if self.setting.wait_check_page():
                    self.setting.regist_protocol()  # 进入注册协议页面

                    if self.protocol.wait_check_page():  # 页面检查点
                        for i in range(4):
                            print('翻页%s次' % (i + 1))
                            BasePage().screen_swipe_up(0.5, 0.5, 0.25, 1000)
                        print('下拉一次')
                        BasePage().screen_swipe_down(0.5, 0.05, 0.9, 1000)
                        self.setting.back_up_button()

                        if self.setting.wait_check_page():  # 页面检查点
                            print('success')
                        else:
                            print(' failed  ')
                        self.home.back_up_button()  # 点击 返回按钮
                    else:
                        print('未进入注册协议页面')

                    if self.user.wait_check_page():  # 页面检查点
                        self.home.click_tab_hw()  # 回首页
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
