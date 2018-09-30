# coding=utf-8
import time
import unittest
import HTMLTestRunner

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.matching_exercises_page import MatchingExercises
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type_yb import GetVariable as gv
from conf.base_page import BasePage
from utils.toast_find import Toast
from utils.yb_dict import yb_operate_yb
from conf.decorator import setup, teardown, testcase, teststeps


class Games(unittest.TestCase):
    """连连看 -yb字体"""

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
    def test_match_exercise_yb(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 页面检查点
            print("已进入主界面：")
            var = self.home_page.homework_count()
            if gv.MAT_EXE_YB in var[0]:  # 该作业存在
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.MAT_EXE_YB:
                        var[1][i].click()
                        time.sleep(3)
                        count = self.homework.games_count(0, '连连看')
                        self.game_exist(count[0])
                        if count[1] == 10:
                            game_count = self.homework.swipe_screen('连连看')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.MAT_EXE_YB, '连连看')  # 作业list翻页
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
            for index_1 in count:
                print('####################################################')
                print('有小游戏', index_1)
                self.homework.games_type()[index_1].click()  # 进入小游戏
                self.match_exercise_yb()  # 游戏过程

                # self.vocab_select.result_page()  # 结果页
                # self.vocab_select.result_detail_page()  # 结果页 查看答案 按钮
                # self.vocab_select.study_again(homework_type)  # 结果页 错题再练 按钮

                print('####################################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have词汇选择小游戏')

    @teststeps
    def match_exercise_yb(self):
        """《连连看》 游戏过程"""
        if self.match_up.wait_check_page():  # 页面检查点
            rate = self.match_up.rate()
            if int(rate) % 5 == 0:
                page = int(int(rate) / 5)
            else:
                page = int(int(rate) / 5) + 1
            print('页数:', page)
            for j in range(page):
                word = []  # 单词list
                word_index = []  # 单词在所有button中的索引
                explain = []  # 解释list
                explain_index = []  # 解释在所有button中的索引
                ele = self.match_up.word()  # 所有button
                for i in range(3, len(ele)):
                    if ele[i].text[0] != "/":
                        word.append(ele[i].text)
                        word_index.append(i)
                    else:
                        explain.append(ele[i].text)
                        explain_index.append(i)
                print(word_index, word, explain, explain_index)

                for k in range(len(word)):    # 具体操作
                    print('word:', word[k], len(word[k]))
                    if len(word[k]) <= 2:
                        value = yb_operate_yb(word[k])
                        ele[word_index[k]].click()
                        for z in range(len(explain)):
                            if explain[z] == value:
                                print('explain:', explain[z])
                                ele[explain_index[z]].click()
                                break
                time.sleep(2)


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
