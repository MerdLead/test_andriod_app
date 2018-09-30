##!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.reset_phone_page import PhoneReset
from app.teacher.user_center.user_information.object_page.user_Info_page import UserInfoPage
from app.teacher.user_center.user_information.test_data.reset_phone import reset_phone_data
from conf.decorator import setupclass, teardownclass, testcase
from utils.reset_phone_findtoast import verify_find
from utils.toast_find import Toast


class ExchangePhone(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.user_info = UserInfoPage()
        cls.phone_reset = PhoneReset()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_exchange_phone(self):
        """更换手机号 -- 正常流程 """
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user.wait_check_page():  # 页面检查点
                self.user.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作
                if self.user_info.wait_check_page():  # 页面检查点
                    for i in range(len(reset_phone_data)):
                        phone1 = self.user_info.phone()  # 获取修改前手机号
                        self.user_info.click_phone_number()  # 点击手机号条目，进入设置页面

                        if self.user_info.wait_check_tips_page():
                            self.user_info.tips_title()
                            text = self.user_info.input()  # 验证之前密码
                            text.send_keys(reset_phone_data[i]['password'])
                            self.user_info.click_positive_button()

                            if self.phone_reset.wait_check_page():
                                phone = self.phone_reset.et_phone()
                                phone.send_keys(reset_phone_data[i]['reset'])
                                self.phone_reset.count_time()

                                value = verify_find(reset_phone_data[i]['reset'])  # 获取验证码
                                time.sleep(1)
                                self.phone_reset.verify().send_keys(value)
                                self.phone_reset.btn_certain()

                                if self.user_info.wait_check_page():
                                    phone2 = self.user_info.phone()   # 获取修改后的手机号
                                    if phone1 != phone2:
                                        print('exchange phone success')
                                    else:
                                        print('failed to exchange phone')
                                        self.home.back_up_button()
                            else:
                                print('未进入修改手机号页面')

                        else:
                            print('未进入 确认密码页面')
                    self.user_info.back_up()
                else:
                    print('未进入个人信息页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
