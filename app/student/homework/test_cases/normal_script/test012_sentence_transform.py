# coding=utf-8
import time
import unittest

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.result_page import ResultPage
from app.student.homework.object_page.sentence_transform_page import SentenceTrans
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from conf.base_config import GetVariable as gev
from utils.excel_read_write import ExcelUtil
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """句型转换"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.sentence = SentenceTrans()
        cls.result = ResultPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_strengthen_sentence(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():
            print("已进入主界面：")
            var = self.home_page.homework_count()

            if gv.SENT_TRANS in var[0]:
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.SENT_TRANS:
                        var[1][i].click()  # 点击进入该作业
                        count = self.homework.games_count(0, '句型转换')  # 小游戏个数统计
                        self.game_exist(count[0])  # 具体操作

                        if count[1] == 10:  # 判断小游戏list是否需滑屏
                            game_count = self.homework.swipe_screen('句型转换')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.SENT_TRANS, '句型转换')  # 作业list翻页
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
        """句型转换游戏具体操作 及 操作后的滑屏"""
        time.sleep(1)
        if len(count) != 0:
            for index in count:
                print('####################################################')
                print('有小游戏', index)
                # game_title = self.homework.games_title()[index_1].text
                # game_status = self.homework.status()[index_1].text

                self.homework.games_type()[index].click()  # 进入小游戏
                answer = self.sentence.sentence_transform()  # 游戏过程
                self.sentence.check_detail_page(answer[0], answer[1])  # 查看答案
                self.sentence.study_again()  # 再练一遍

                print('####################################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have句型转换小游戏')
