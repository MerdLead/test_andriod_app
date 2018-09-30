##!/usr/bin/env python
# encoding:UTF-8
import HTMLTestRunner
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.reset_password_page import PwdReset
from app.teacher.user_center.user_information.object_page.user_Info_page import UserInfoPage
from app.teacher.user_center.user_information.test_data.reset_password import reset_pwd
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class ExchangePhone(unittest.TestCase):
    """更改密码"""
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.user_info = UserInfoPage()
        cls.pwd_reset = PwdReset()

    @classmethod
    @teardown
    def tearDown(cls):
        """关闭应用"""
        pass

    @testcase
    def test_change_password(self):
        """修改密码 -- 正常流程"""
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮
            if self.user.wait_check_page():  # 页面检查点
                self.user.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作

                if self.user_info.wait_check_page():  # 页面检查点
                    self.user_info.click_password()  # 点击修改密码
                    for i in range(len(reset_pwd)):
                        print('修改密码为:', reset_pwd[i]['new'])
                        if self.pwd_reset.wait_check_page():  # 页面检查点
                            self.pwd_reset.pwd_checkbox()
                            old_pwd = self.pwd_reset.pwd_origin()
                            old_pwd.click()
                            old_pwd.send_keys(reset_pwd[i]['old'])

                            # 输入新的密码
                            new_pwd = self.pwd_reset.pwd_new()
                            new_pwd.click()
                            new_pwd.send_keys(reset_pwd[i]['new'])

                            # 再次输入密码
                            again_pwd = self.pwd_reset.pwd_confirm()
                            again_pwd.click()
                            again_pwd.send_keys(reset_pwd[i]['commit'])

                            self.pwd_reset.confirm_button()  # 点击完成按钮
                            if self.user_info.wait_check_page(10):  # 页面检查点
                                print('success to changed')
                                if i != len(reset_pwd)-1:
                                    self.user_info.click_password()  # 点击修改密码
                            else:
                                print('failed to submit question')
                            print('---------------------------------')
                else:
                    print('未进入个人信息页面')

                self.user_info.back_up()
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
