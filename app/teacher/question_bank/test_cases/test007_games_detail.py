#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.filter_page import FilterPage
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.question_bank.object_page.question_detail_page import QuestionDetailPage
from app.teacher.question_bank.object_page.games_detail_page import GamesPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class GameDetail(unittest.TestCase):
    """游戏详情"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.question = QuestionBankPage()
        cls.detail = QuestionDetailPage()
        cls.game = GamesPage()
        cls.filter = FilterPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_game_detail(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('题单'):  # 页面检查点
                self.question.filter_button()  # 筛选按钮

                if self.filter.wait_check_page():  # 页面检查点
                    menu = self.filter.game_list()
                    if self.filter.selected(menu) == 'false':  # 大题
                        self.filter.click_game_list()  # 点击 大题
                        time.sleep(2)
                        name = self.filter.label_name()  # 所有标签
                        var = name[9].text
                        print(var)
                        name[9].click()  # 选择一个标签  词汇选择
                        self.filter.commit_button()  # 确定按钮

                        if self.question.wait_check_page('搜索'):  # 页面检查点
                            name = self.question.question_name()
                            name[0][0].click()

                            if self.game.wait_check_page():  # 页面检查点
                                self.game_detail_operate()  # 游戏详情页 具体操作

                                self.detail.recommend_button()  # 推荐按钮
                                Toast().find_toast('推荐成功')  # 获取toast

                                time.sleep(2)
                                self.detail.collect_button()  # 收藏按钮

                                time.sleep(2)
                                self.detail.put_to_basket_button()  # 加入题筐 按钮
                                Toast().find_toast('添加题筐成功')  # 获取toast

                                time.sleep(2)
                                self.question.back_up_button()  # 返回 题单详情页

                                if self.detail.wait_check_page():  # 页面检查点
                                    self.question.back_up_button()  # 返回题库页面
                                    if self.question.wait_check_page('题单'):
                                        self.home.click_tab_hw()
                                #     self.question.verify_basket_result(title)
                                #     self.question.verify_collect_result(title, '大题')
            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def game_detail_operate(self):
        """游戏详情页"""
        print('------------------------------------------')
        print('游戏详情页:')
        # todo 传参var[0] 题数
        title = self.game.game_title()  # title
        count = self.game.game_info()[1:3]  # info
        self.game.teacher_nickname()  # 老师昵称

        if self.game.verify_question_index():  # 单词类
            index = self.game.question_index()  # 题号
            word = self.game.word()  # 单词
            explain = self.game.explain()  # 解释
            for k in range(len(explain)):
                print(index[k].text, word[k].text, explain[k].text)
                if self.game.verify_speak_button():
                    self.game.speak_button(k)
            last = index[len(explain)-1].text

            if int(len(index)) > 6:
                self.game.screen_swipe_up(0.5, 0.95, 0.15)
                index = self.game.question_index()  # 题号
                word = self.game.word()  # 单词
                explain = self.game.explain()  # 解释
                for z in range(len(explain)):
                    num = index[z].text
                    if int(num[:-1]) > int(last[:-1]):
                        print(index[z].text, word[z].text, explain[z].text)
                        if self.game.verify_speak_button():
                            self.game.speak_button(z)
        elif self.game.verify_options():  # 有选项
            self.game.swipe_operate(int(count))  # 单选题滑屏及具体操作
        else:  # 句子类
            last = []
            sentence = self.game.sentence()  # 句子
            hint = self.game.hint()  # 解释
            for k in range(len(hint)):
                print(sentence[k].text, hint[k].text)
                last.append(hint[k].text)

            if int(len(sentence)) > 3:
                self.game.screen_swipe_up(0.5, 0.95, 0.15)
                sentence = self.game.sentence()  # 句子
                hint = self.game.hint()  # 解释
                for z in range(len(hint)):
                    num = hint[z].text
                    if num not in last:
                        print(sentence[z].text, hint[z].text)

        print('------------------------------------------')
        return title
