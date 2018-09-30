# coding=utf-8
import unittest
import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.user_Info_page import UserInfoPage
from app.teacher.user_center.user_information.test_data.nickname import nickname_data
from conf.decorator import setupclass, teardownclass, testcase
from utils.screen_shot import ScreenShot
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
        cls.screen_shot = ScreenShot()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_nickname(self):
        """修改昵称 -- 正常流程"""
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮
            if self.user.wait_check_page():  # 页面检查点

                self.user.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作
                if self.user_info.wait_check_page():  # 页面检查点
                    for i in range(len(nickname_data)):
                        if self.user_info.wait_check_page():  # 页面检查点
                            name1 = self.user_info.nickname()

                            self.user_info.click_nickname()  # 点击昵称条目，进入设置页面
                            if self.user_info.wait_check_tips_page():
                                self.user_info.tips_title()
                                print('修改为：', nickname_data[i]['nickname'])
                                text = self.user_info.input()  # 找到要修改的文本 EditText元素

                                text.send_keys(nickname_data[i]['nickname'])  # 输入昵称

                                if self.user_info.positive_button() == 'true':
                                    self.user_info.click_positive_button()

                                    if self.user_info.wait_check_page():  # 页面检查点
                                        if len(nickname_data[i]) == 2:
                                            # print('toast:', Toast().find_toast(nickname_data[i]['assert']))
                                            # todo 获取toast
                                            name2 = self.user_info.nickname()
                                            if name2 == name1:
                                                print('not change nickname')
                                            else:
                                                print('★★★ Error- nickname is changed', nickname_data[i]['nickname'], name2)
                                        else:
                                            time.sleep(2)
                                            name2 = self.user_info.nickname()
                                            if name2 != name1:
                                                print('nickname is changed')
                                            else:
                                                print('★★★ Error- failed change nickname', nickname_data[i]['nickname'], name2)
                                    else:
                                        print('未返回个人信息页面')
                                else:
                                    self.user_info.click_negative_button()

                                    if self.user_info.wait_check_page():  # 页面检查点
                                        name2 = self.user_info.nickname()
                                        if name2 == name1:
                                            print('not change nickname')
                                        else:
                                            print('★★★ Error- nickname is changed', nickname_data[i]['nickname'], name2)
                                    else:
                                        print('未返回个人信息页面')

                        print('-----------------------------------')
                else:
                    print('未进入个人信息页面')
                self.user_info.back_up()  # 返回
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
