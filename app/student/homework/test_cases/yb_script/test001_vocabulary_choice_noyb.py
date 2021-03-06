# coding=utf-8
import random
import time
import unittest
import HTMLTestRunner

from app.student.homework.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.vocabulary_choice_page import VocabularyChoice
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.homework.test_data.homework_title_type_yb import GetVariable as gv
from conf.base_page import BasePage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast
from utils.yb_dict import no_yb_operate_word, no_yb_operate_yb


class Games(unittest.TestCase):
    """词汇选择- yb字体"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.vocab_select = VocabularyChoice()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vocabulary_selection_noyb(self):
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():  # 主界面检查点
            print("已进入主界面：")
            BasePage().screen_swipe_up(0.5, 0.75, 0.25, 1000)
            var = self.home_page.homework_count()
            if gv.VOC_CHO in var[0]:  # 该作业存在
                for i in range(0, len(var[0])):
                    if var[0][i] == gv.VOC_CHO:
                        var[1][i].click()
                        time.sleep(3)
                        count = self.homework.games_count(0, '词汇选择')
                        self.game_exist(count[0])

                        if count[1] == 10:  # 判断小游戏list是否需滑屏
                            game_count = self.homework.swipe_screen('词汇选择')
                            if len(game_count) != 0:
                                self.game_exist(game_count)
            else:
                print('当前页no have该作业')
                game = self.home_page.swipe(var[0], gv.VOC_CHO, '词汇选择')  # 作业list翻页
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
                self.diff_type_no(homework_type)  # 不同模式小游戏的 游戏过程

                # self.vocab_select.result_page()  # 结果页
                # self.vocab_select.result_detail_page()  # 结果页 查看答案 按钮
                # self.vocab_select.study_again(homework_type)  # 结果页 错题再练 按钮

                print('####################################################')
                self.homework.back_up_button()
            self.homework.back_up_button()  # 返回主界面
        else:
            print('no have词汇选择小游戏')

    @teststeps
    def diff_type_no(self, tpe):
        """选择 不同模式小游戏的 游戏方法"""
        print(tpe)
        if tpe == '选单词':
            self.vocab_select_choice_word_no()
        elif tpe == '选解释':
            self.vocab_select_choice_explain_no()
        elif tpe == '听音选词':  # 听音选词模式
            print('听音选词模式')
            # self.vocab_select_listen_choice_no()

    @teststeps
    def vocab_select_choice_explain_no(self):
        """《词汇选择》 - 选解释模式 游戏过程--普通单词一般做法，符合yb字体规范的特殊处理"""
        if self.vocab_select.wait_check_page():  # 页面检查点
            rate = self.vocab_select.rate()
            for i in range(int(rate)):
                self.vocab_select.click_voice()
                word = self.vocab_select.word()
                options = self.vocab_select.option_button()
                if len(word) > 2:
                    options[random.randint(0, len(options) - 1)].click()  # 随机点击选项
                else:
                    value = no_yb_operate_yb(word)
                    for j in range(4):
                        if options[j].text == value:
                            options[j].click()
                            break
                self.homework.next_button()

    @teststeps
    def vocab_select_choice_word_no(self):
        """《词汇选择》 - 选单词模式 游戏过程"""
        if self.vocab_select.wait_check_page():  # 页面检查点
            rate = self.vocab_select.rate()
            for i in range(int(rate)):
                word = self.vocab_select.word()
                options = self.vocab_select.option_button()
                if len(word) != 3:
                    options[random.randint(0, len(options) - 1)].click()  # 随机点击选项
                else:
                    value = no_yb_operate_word(word)
                    for j in range(4):
                        if options[j].text.lower() == value:
                            options[j].click()
                            break
                self.homework.next_button()

    @teststeps
    def vocab_select_listen_choice_no(self):
        """《词汇选择》 - 听音选词模式 游戏过程"""
        if self.vocab_select.wait_check_page() == '词汇选择':
            rate = self.vocab_select.rate()
            for i in range(int(rate)):
                self.vocab_select.voice()
                self.vocab_select.click_voice()

                options = self.vocab_select.option_button()
                options[random.randint(0, len(options) - 1)].click()  # 随机点击选项
                self.homework.next_button()


if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(Games('test_vocabulary_selection_noyb'))

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
