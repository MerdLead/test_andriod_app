# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.user_center.object_page.user_Info_page import UserInfoPage
from app.student.user_center.object_page.user_center_page import UserCenterPage
from conf.decorator import setupclass, teardownclass, testcase
from utils.edit_text import DelEditText
from utils.toast_find import Toast


class NickName(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.user_center = UserCenterPage()
        cls.user_info = UserInfoPage()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_nickname(self):
        """修改昵称 -- 修改后不保存"""
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():
            self.home_page.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user_center.wait_check_page():  # 页面检查点
                self.user_center.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作
                if self.user_info.wait_check_page():  # 页面检查点
                    name1 = self.user_info.nickname()
                    # 点击昵称条目，进入设置页面
                    self.user_info.click_nickname()
                    text = self.user_info.input()  # 找到要删除文本的EditText元素
                    # 删除文本框中内容
                    DelEditText().del_text(text)
                    text.send_keys("HelloWorld")
                    self.user_info.click_negative_button()

                    if self.user_info.wait_check_page():
                        name2 = self.user_info.nickname()
                        if name2 == name1:
                            print('cancel change nickname success')
                        else:
                            print('cancel change nickname failed')

                        self.user_info.back_up()
                    else:
                        print('未返回个人信息页面')
                else:
                    print('未进入个人信息页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
