# coding=utf-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.user_Info_page import UserInfoPage
from conf.decorator import setupclass, teardownclass, testcase
from utils.edit_text import DelEditText
from utils.toast_find import Toast


class NickName(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.user_info = UserInfoPage()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_nickname(self):
        """修改昵称 -- 修改后不保存"""
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮
            if self.user.wait_check_page():  # 页面检查点
                self.user.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作

                if self.user_info.wait_check_page():  # 页面检查点
                    name1 = self.user_info.nickname()

                    self.user_info.click_nickname()  # 点击昵称条目，进入设置页面
                    if self.user_info.wait_check_tips_page():
                        self.user_info.tips_title()
                        text = self.user_info.input()  # 找到要删除文本的EditText元素
                        DelEditText().del_text(text)   # 删除文本框中内容
                        text.send_keys("HelloWorld")  # 输入
                        self.user_info.click_negative_button()

                        if self.user_info.wait_check_page():  # 页面检查点
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
