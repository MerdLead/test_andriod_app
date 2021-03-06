# coding=utf-8
import time
import unittest
import HTMLTestRunner

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.guess_word_page import GuessWord
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from utils.toast_find import Toast
from conf.decorator import setup, teardown, testcase, teststeps


class Games(unittest.TestCase):
    """猜词游戏"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.guess_word = GuessWord()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_guess_word(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("登录成功")
            var = self.home_page.homework_count()
            if gv.GUE_WORD in var[0]:
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.GUE_WORD:
                        var[1][i].click()  # 点击进入该作业
                        count = self.homework.games_count(0, '猜词游戏')  # 小游戏个数统计
                        self.game_exist(count[0])  # 具体操作

                        if count[1] == 10:  # 判断小游戏list是否需滑屏
                            game_count = self.homework.swipe_screen('猜词游戏')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.GUE_WORD, '猜词游戏')  # 作业list翻页
                self.game_exist(game)
            print('Game Over')
        else:
            try:
                Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            except Exception as e:
                print("未进入主界面")
                raise e

    @teststeps
    def game_exist(self, count):
        """猜词游戏游戏具体操作 及 操作后的滑屏"""
        if len(count) != 0:
            for index in count:
                print('##########################################')
                print('有小游戏')
                homework_type = self.homework.tv_testbank_name(index)  # 获取小游戏模式
                self.homework.games_type()[index].click()  # 进入小游戏
                self.guess_word.diff_type(homework_type)  # 不同模式小游戏的 游戏过程

                print('##########################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have猜词游戏 小游戏')


if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(Games('test_guess_word'))

        report_title = u'自动化测试执行报告'
        desc = '用于展示修改样式后的HTMLTestRunner'
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        filename = r'C:/Users/V/Desktop/Testreport/Result_' + timestr + '.html'

        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=report_title,
            description=desc)
        runner.run(suite)
        fp.close()
