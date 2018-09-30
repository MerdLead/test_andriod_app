#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest

from app.student.homework.object_page.single_choice_page import SingleChoice
from app.student.login.object_page.login_page import LoginPage
from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from conf.decorator import setup, teardown, teststeps
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """单项选择"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.single_choe = SingleChoice()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    def test_single_choice(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("已进入主界面：")
            var = self.home_page.homework_count()
            if gv.SIN_CHO in var[0]:  # 该作业存在
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.SIN_CHO:
                        var[1][i].click()  # 进入作业
                        count = self.homework.games_count(0, '单项选择')  # 统计小游戏个数
                        self.game_exist(count[0])  # 具体操作

                        if count[1] == 10:  # 判断小游戏list是否需要滑屏
                            game_count = self.homework.swipe_screen('单项选择')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('no have该作业')
                game = self.home_page.swipe(var[0], gv.SIN_CHO, '单项选择')  # 作业list翻页
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
        """单项选择游戏具体操作 及 操作后的滑屏"""
        if len(count) != 0:
            print('有小游戏')
            for index in count:
                print('##########################################')
                self.homework.games_type()[index].click()  # 进入小游戏
                self.single_choe.single_choice_operate()  # 单项选择 - 游戏过程

                self.single_choe.detail_page()  # 结果页 查看答案
                self.single_choe.study_again()  # 结果页 错题再练

                print('##########################################')
                self.homework.back_up_button()
            self.homework.back_up_button()
        else:
            print('no have单项选择小游戏')
