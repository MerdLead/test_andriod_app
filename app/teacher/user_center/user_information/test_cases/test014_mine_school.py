# coding=utf-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.user_Info_page import UserInfoPage
from app.teacher.user_center.user_information.test_data.school import school_data
from conf.decorator import setupclass, teardownclass, testcase
from utils.screen_shot import ScreenShot
from utils.toast_find import Toast


class School(unittest.TestCase):

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
    def test_edit_school(self):
        """修改我的学校 -- 正常流程"""
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮
            if self.user.wait_check_page():  # 页面检查点
                self.user.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作

                if self.user_info.wait_check_page():  # 页面检查点
                    for i in range(len(school_data)):
                        school1 = self.user_info.school()
                        self.user_info.click_school()  # 点击学校条目，进入设置页面

                        if Toast().find_toast('没有权限修改学校信息'):
                            print('在校老师 没有权限修改学校信息')
                            break
                        else:
                            text = self.user_info.input()  # 找到要修改的EditText元素
                            text.send_keys(school_data[i]['sch'])  # 输入
                            self.user_info.click_positive_button()

                            if self.user_info.wait_check_page():  # 页面检查点
                                school2 = self.user_info.school()
                                if school2 != school1:
                                    print('school is changed')
                                else:
                                    print('failed change school')
                            else:
                                print('未返回个人信息页面')
                        self.user_info.back_up()
                else:
                    print('未进入个人信息页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
