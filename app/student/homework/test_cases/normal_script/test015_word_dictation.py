# coding=utf-8
import time
import unittest

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.word_dictation_page import WordDictation
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from conf.base_config import GetVariable as gev
from utils.excel_read_write import ExcelUtil
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """单词听写"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.word_dict = WordDictation()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_word_dictation(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():
            print("已进入主界面：")
            self.home_page.click_homework_label()
            if self.homework.homework_page_check:
                var = self.home_page.homework_count()
                if gv.WOR_DIC in var[0]:
                    for i in range(0, len(var[0])):
                        if var[0][i] == gv.WOR_SPE:
                            var[1][i].click()  # 点击进入该作业
                            count = self.homework.games_count(0, '单词听写')  # 小游戏个数统计
                            self.game_exist(count[0])  # 具体操作

                            if count[1] == 10:  # 判断小游戏list是否需滑屏
                                game_count = self.homework.swipe_screen('单词听写')
                                if len(game_count) != 0:
                                    self.game_exist(game_count)
                else:
                    print('当前页no have该作业')
                    game = self.home_page.swipe(var[0], gv.WOR_DIC, '单词听写')  # 作业list翻页
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
        """词汇选择游戏具体操作 及 操作后的滑屏"""
        time.sleep(1)
        if len(count) != 0:
            for index in count:
                print('##########################################')
                print('有小游戏')
                # game_title = self.homework.games_title()[index_1].text
                # game_status = self.homework.status()[index_1].text

                self.homework.games_type()[index].click()  # 进入小游戏
                result = self.word_dict.word_dictation()  # 小游戏的 游戏过程
                self.word_dict.result_detail_page(result[0])  # 结果页 查看答案 按钮
                self.word_dict.study_again()  # 结果页 错题再练 按钮

                # if game_status == '未开始':
                #     for i in range(len(answer[1])):
                #         ExcelUtil(gev.EXCEL_PATH).data_write(answer[0], homework_title, game_title, answer[1][i])

                print('##########################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have词汇选择小游戏')
