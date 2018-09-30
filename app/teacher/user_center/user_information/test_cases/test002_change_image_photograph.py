#!/usr/bin/env python
# encoding:UTF-8
import unittest

import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.user_center.user_information.object_page.change_image_page import ChangeImage
from app.teacher.user_center.user_information.object_page.user_Info_page import UserInfoPage
from conf.basepage import BasePage
from conf.decorator import setupclass, teardownclass, testcase
from utils.screen_shot import ScreenShot
from utils.toast_find import Toast


class ImageChange(unittest.TestCase):
    """拍照修改头像 -- 正常流程"""

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.user_info = UserInfoPage()
        cls.change_image = ChangeImage()
        cls.screen_shot = ScreenShot()
        cls.base_page = BasePage()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_change_image_photo(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮
            if self.user.wait_check_page():  # 页面检查点
                self.user.click_avatar_profile()  # 点击登录头像按钮，进行个人信息操作

                if self.user_info.wait_check_page():  # 页面检查点
                    # 获取登录后的头像截图
                    # image1 = self.user_info.image()
                    # t = self.screen_shot.screenshot(image1)
                    # self.assertTrue(t)

                    self.user_info.click_image()  # 点击头像条目，进入设置页面
                    if self.user_info.wait_check_tips_page():
                        self.user_info.tips_title()  # 弹框信息
                        self.user_info.click_photograph()  # 拍照

                        if self.change_image.wait_check_page_camera():  # 页面检查点
                            self.change_image.click_camera_button()
                            time.sleep(2)
                            self.change_image.click_done_button()
                            time.sleep(2)
                            self.change_image.click_save_button()

                            if self.user_info.wait_check_page():
                                print('change success')
                            else:
                                print('change failed')
                                # 获取修改后的头像截图
                                # image2 = self.user_info.image()
                                # result = self.screen_shot.same_as_screenshot(image2, t)
                                # self.assertTrue(result)

                            if self.user_info.wait_check_page():  # 页面检查点
                                self.user_info.back_up_button()  # 返回按钮
                        else:
                            print('未进入拍照页面')

                    if self.user.wait_check_page():  # 页面检查点
                        self.home.click_tab_hw()  # 回首页
                else:
                    print('未进入个人信息页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
