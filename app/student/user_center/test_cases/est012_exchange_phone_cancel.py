# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.user_center.object_page.user_Info_page import UserInfoPage, PhoneReset
from app.student.user_center.object_page.user_center_page import UserCenterPage
from app.student.user_center.test_data.reset_phone import VALID_RESETPHONE
from conf.decorator import setupclass, teardownclass, testcase
from utils.reset_phone_findtoast import verify_find
from utils.toast_find import Toast


class ExchangePhone(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.user_center = UserCenterPage()
        cls.user_info = UserInfoPage()
        cls.phone_reset = PhoneReset()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_exchange_phone(self):
        """更换手机号 -- 验证码验证失败"""
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():
            self.home_page.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user_center.wait_check_page():  # 页面检查点
                self.user_center.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作

                if self.user_info.wait_check_page():
                    phone1 = self.user_info.phone()
                    # 点击手机号条目，进入设置页面
                    self.user_info.click_phone_number()
                    text = self.user_info.input()  # 验证密码
                    text.send_keys(VALID_RESETPHONE.password())
                    self.user_info.click_positive_button()

                    if self.phone_reset.wait_check_page():
                        phone = self.phone_reset.et_phone()
                        phone.send_keys(VALID_RESETPHONE.reset())
                        self.phone_reset.count_time()
                        value = verify_find(VALID_RESETPHONE.reset())
                        verify = self.phone_reset.verify()
                        verify.send_keys('1234')
                        self.phone_reset.btn_certain()
                        t = Toast().find_toast('验证码验证失败')
                        if t:
                            verify.clear()
                            self.phone_reset.verify().send_keys(value)
                            self.phone_reset.btn_certain()
                            if self.user_info.wait_check_page():
                                phone2 = self.user_info.phone()
                                if phone1 == phone2:
                                    print('exchange success')
                                else:
                                    print('failed')

                                self.user_info.back_up()
                            else:
                                print('未返回个人信息页面')
                    else:
                        print('未进入手机修改页面')
                else:
                    print('未进入个人信息页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
