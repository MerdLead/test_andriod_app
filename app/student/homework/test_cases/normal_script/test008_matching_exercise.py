# coding=utf-8
import time
import unittest

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.matching_exercises_page import MatchingExercises
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from utils.toast_find import Toast
from conf.decorator import setup, teardown, testcase, teststeps


class Games(unittest.TestCase):
    """连连看"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.match_up = MatchingExercises()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_match_exercise(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("登录成功")
            var = self.home_page.homework_count()
            if gv.MAT_EXE in var[0]:
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.MAT_EXE:
                        var[1][i].click()  # 点击进入该作业
                        count = self.homework.games_count(0, '连连看')  # 小游戏个数统计
                        self.game_exist(count[0])  # 具体操作

                        if count[1] == 10:  # 判断小游戏list是否需滑屏
                            game_count = self.homework.swipe_screen('连连看')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.MAT_EXE, '连连看')  # 作业list翻页
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
        """游戏具体操作 及 操作后的滑屏"""
        if len(count) != 0:
            for index in count:
                print('####################################################')
                print('有小游戏', index)
                self.homework.games_type()[index].click()  # 进入小游戏
                result = self.match_up.match_exercise()  # 游戏过程
                self.match_up.result_detail_page(result[0])  # 结果页 查看答案 按钮
                self.match_up.study_again()  # 结果页 再练一遍 按钮

                print('####################################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have词汇选择小游戏')
