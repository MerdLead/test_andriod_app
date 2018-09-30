# coding=utf-8
import time
import unittest
import HTMLTestRunner

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.restore_word_page import RestoreWord
from app.student.homework.object_page.result_page import ResultPage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type import GetVariable as gv
from conf.base_page import BasePage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Games(unittest.TestCase):
    """还原单词"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.res_word = RestoreWord()
        cls.base_page = BasePage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_restore_word(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("登录成功")
            var = self.home_page.homework_count()
            if gv.RES_WORD in var[0]:
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.RES_WORD:
                        var[1][i].click()  # 点击进入该作业
                        count = self.homework.games_count(0, '还原单词')  # 小游戏个数统计
                        self.game_exist(count[0])  # 具体操作

                        if count[1] == 10:  # 判断小游戏list是否需滑屏
                            game_count = self.homework.swipe_screen('还原单词')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.RES_WORD, '还原单词')  # 作业list翻页
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
        """还原单词游戏具体操作 及 操作后的滑屏"""
        if len(count) != 0:
            print('有小游戏')
            for index in count:
                print('##########################################')
                self.homework.games_type()[index].click()  # 进入小游戏
                answer = self.res_word.restore_word()  # 小游戏的 游戏过程
                # self.word_spelling.result()  # 结果页
                self.res_word.check_detail_page(answer[0], answer[1])  # 结果页 查看答案 按钮
                # self.word_spelling.study_again(homework_type)  # 结果页 错题再练 按钮

                print('##########################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have还原单词小游戏')


if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(Games('test_restore_word'))

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
