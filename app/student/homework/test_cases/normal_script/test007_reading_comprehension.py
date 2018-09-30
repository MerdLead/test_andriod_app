#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest

from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.reading_comprehension_page import ReadCompre
from app.student.homework.object_page.result_page import ResultPage
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """阅读理解"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.read = ReadCompre()
        cls.result = ResultPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_reading_comprehension(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("已进入主界面：")
            self.home_page.click_homework_label()
            if self.homework.homework_page_check:
                var = self.home_page.homework_count()
                if gv.REA_COMPRE in var[0]:  # 该作业存在
                    for i in range(0, len(var[0])):
                        if var[0][i] == gv.REA_COMPRE:
                            var[1][i].click()  # 进入作业
                            count = self.homework.games_count(0, '阅读理解')  # 小游戏个数统计
                            self.game_exist(count[0])  # 具体操作

                            if count[1] == 10:  # 判断小游戏list是否需滑屏
                                game_count = self.homework.swipe_screen('阅读理解')
                                if len(game_count) != 0:
                                    self.game_exist(game_count)
                else:
                    print('当前页no have该作业')
                    game = self.home_page.swipe(var[0], gv.REA_COMPRE, '阅读理解')  # 作业list翻页
                    self.game_exist(game)
                print('Game Over')
            else:
                try:
                    Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
                except Exception:
                    print("未进入主界面")
                    raise

    @teststeps
    def game_exist(self, count):
        if len(count) != 0:
            print('有小游戏')
            for index in count:
                print('####################################################')
                self.homework.games_type()[index].click()
                self.read.reading_operate()  # 阅读理解 游戏过程

                print('####################################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have阅读理解小游戏')
