# coding=utf-8
import time
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from app.student.homework.object_page.listening_choice_page import Listening
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """听力选择"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.listening = Listening()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_listen_choice(self):
        self.login_page.app_status()  # 判断APP当前状态
        if self.home_page.wait_check_page():
            print("已进入主界面：")
            self.home_page.click_hk_tab(2)

            if self.homework.wait_check_page():  # 页面检查点
                var = self.home_page.homework_count()
                if gv.LIS_EXE in var[0]:
                    for i in range(0, len(var[0])):
                        if var[0][i] == gv.LIS_EXE:
                            var[1][i].click()
                            count = self.homework.games_count(0, '听力练习')  # 小游戏个数统计
                            self.game_exist(count[0])

                            if count[1] == 10:  # 判断小游戏list是否需滑屏
                                game_count = self.homework.swipe_screen('听力练习')
                                if len(game_count) != 0:
                                    self.game_exist(game_count)
                else:
                    print('当前页no have该作业')
                    game = self.home_page.swipe_operate(var[0], gv.LIS_EXE, '听力练习')  # 作业list翻页
                    self.game_exist(game[0])
                    print('Game Over')
            else:
                Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
                print("未进入主界面")

    @teststeps
    def game_exist(self, count):
        """词汇选择游戏具体操作 及 操作后的滑屏"""
        time.sleep(1)
        if len(count) != 0:
            for index in count:
                print('##########################################')
                print('有小游戏')
                if index == 1:
                    continue
                self.homework.games_type()[index].click()  # 进入小游戏
                self.listening.listen_choice()  # 听力练习游戏过程
                # self.homework.back_up_button()
                # time.sleep(1)
                # self.listening.play_again_button()
                print('##########################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have词汇选择小游戏')

