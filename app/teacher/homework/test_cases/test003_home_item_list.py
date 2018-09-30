#!/usr/bin/env python
import unittest

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class HomeItem(unittest.TestCase):
    """首页列表"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.homework = ReleasePage()
        cls.detail = HwDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_home_item_list(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            if self.home.wait_check_no_page():
                print('无最新动态 -- (用户指南) 欢迎使用在线助教,打开看看吧!')
            else:
                var = self.home.hw_list_operate([])  # 作业列表
                while True:
                    self.detail.screen_swipe_up(0.5, 0.85, 0.5, 1000)
                    var = self.home.hw_list_operate(var[0])  # 作业列表
                    if int(var[1]) == 1:
                        break

                while True:
                    if self.home.wait_check_image_page():
                        break
                    else:
                        self.homework.screen_swipe_down(0.5, 0.1, 0.85, 1000)
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
