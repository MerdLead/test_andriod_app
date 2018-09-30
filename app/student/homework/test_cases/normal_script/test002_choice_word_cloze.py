#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest

from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.choice_word_cloze_page import ChoiceWordCloze
from app.student.homework.object_page.result_page import ResultPage
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from conf.decorator import setup, teardown
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """选词填空"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.cho_word_clo = ChoiceWordCloze()
        cls.result = ResultPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    def test_choice_word_cloze(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("已进入主界面：")
            self.home_page.click_homework_label()
            if self.homework.homework_page_check:
                var = self.home_page.homework_count()
                if gv.CHO_WOR_CL in var[0]:  # 该作业存在
                    for i in range(0, len(var[0])):
                        if var[0][i] == gv.CHO_WOR_CL:
                            var[1][i].click()  # 点击进入该作业
                            count = self.homework.games_count(0, '选词填空')
                            self.game_exist(count[0], gv.CHO_WOR_CL)

                            if count[1] == 10:  # 小游戏list需翻页
                                game_count = self.homework.swipe_screen('选词填空')
                                if len(game_count) != 0:
                                    self.game_exist(game_count, gv.CHO_WOR_CL)
                else:
                    print('当前页no have该作业')
                    game = self.home_page.swipe(var[0], gv.CHO_WOR_CL, '选词填空')  # 作业list翻页
                    self.game_exist(game, gv.CHO_WOR_CL)
                print('Game Over')
            else:
                try:
                    Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
                except Exception as e:
                    print("未进入主界面")
                    raise e

    def game_exist(self, count, homework_title):
        """选词填空游戏具体操作 及 操作后的滑屏"""
        if len(count) != 0:
            print('有小游戏')
            for index in count:
                print('####################################################')
                game_title = self.homework.games_title()[index].text
                # game_status = self.homework.status()[index_1].text
                self.homework.games_type()[index].click()
                rate = self.cho_word_clo.choice_word_filling()  # 选词填空 游戏过程
                self.cho_word_clo.detail_page(rate, homework_title, game_title)

                print('####################################################')
                self.homework.back_up_button()  # 返回小游戏界面
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have闪卡练习小游戏')
