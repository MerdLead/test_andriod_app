# coding=utf-8
import time
import unittest
import HTMLTestRunner

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.word_spelling_page import WordSpelling
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type_yb import GetVariable as gv
from conf.base_page import BasePage
from utils.games_keyboard import games_keyboard
from utils.toast_find import Toast
from utils.yb_dict import yb_operate_word
from conf.decorator import setup, teardown, testcase, teststeps


class Games(unittest.TestCase):
    """单词拼写 -yb字体"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.word_spelling = WordSpelling()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_word_spelling_yb(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("已进入主界面：")
            var = self.home_page.homework_count()
            if gv.WOR_SPE_YB in var[0]:  # 该作业存在
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.WOR_SPE_YB:
                        var[1][i].click()
                        time.sleep(3)
                        count = self.homework.games_count(0, '单词拼写')
                        self.game_exist(count[0])
                        if count[1] == 10:
                            game_count = self.homework.swipe_screen('单词拼写')
                            self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.WOR_SPE_YB, '单词拼写')  # 作业list翻页
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
        if len(count) != 0:
            for index_1 in count:
                print('####################################################')
                print('有小游戏', index_1)
                homework_type = self.homework.tv_testbank_name(index_1)  # 获取小游戏模式
                self.homework.games_type()[index_1].click()  # 进入小游戏
                self.diff_type(homework_type)  # 不同模式小游戏的 游戏过程

                # self.word_spelling.result_page()  # 结果页
                # self.word_spelling.result_detail_page()  # 结果页 查看答案 按钮
                # self.word_spelling.study_again(homework_type)  # 结果页 错题再练 按钮

                print('####################################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have词汇选择小游戏')

    @teststeps
    def diff_type(self, tpe):
        """选择 不同模式小游戏的 游戏方法"""
        print(tpe)
        if tpe == '默写模式':
            self.dictation_pattern_yb()
        elif tpe == '自定义':
            self.custom_pattern_yb()
        else:  # 随机模式
            self.random_pattern_yb()

    @teststeps
    def random_pattern_yb(self):
        """《单词拼写 随机模式》 游戏过程"""
        if self.word_spelling.wait_check_page():  # 页面检查点
            rate = self.word_spelling.rate()
            for i in range(int(rate)):
                explain = self.word_spelling.explain()  # 展示的解释
                if len(explain) == 3:
                    value = yb_operate_word(explain)
                    if len(value) == 1:
                        games_keyboard(value)  # 点击键盘对应字母
                    else:
                        word = self.word_spelling.word()
                        for k in range(len(value)):
                            if value[k] not in word:
                                games_keyboard(value[k])  # 点击键盘对应字母
                                break

                self.homework.next_button()
                self.word_spelling.click_voice()
                self.homework.next_button()

    @teststeps
    def custom_pattern_yb(self):
        """《单词拼写 自定义模式》 游戏过程"""
        if self.word_spelling.wait_check_page():  # 页面检查点
            rate = self.word_spelling.rate()
            for i in range(int(rate)):
                explain = self.word_spelling.explain()  # 展示的解释
                if len(explain) == 3:
                    value = yb_operate_word(explain)
                    if len(value) == 1:
                        games_keyboard(value)  # 点击键盘对应字母
                    else:
                        word = self.word_spelling.word()
                        for k in range(len(value)):
                            if value[k] not in word:
                                games_keyboard(value[k])  # 点击键盘对应字母
                                break

                self.homework.next_button()
                self.word_spelling.click_voice()
                self.homework.next_button()

    @teststeps
    def dictation_pattern_yb(self):
        """《单词拼写 默写模式》 游戏过程"""
        if self.word_spelling.wait_check_page():  # 页面检查点
            rate = self.word_spelling.rate()
            for i in range(int(rate)):
                explain = self.word_spelling.explain()  # 展示的解释
                if len(explain) == 3:
                    value = yb_operate_word(explain)
                    if len(value) == 1:
                        games_keyboard(value)  # 点击键盘对应字母
                    else:
                        for k in range(len(value)):
                            games_keyboard(value[k])  # 点击键盘对应字母

                self.homework.next_button()
                self.word_spelling.click_voice()
                self.homework.next_button()


if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(Games('test_word_spelling'))

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
