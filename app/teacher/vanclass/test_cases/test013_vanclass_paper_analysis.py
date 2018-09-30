#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.question_bank.object_page.games_detail_page import GamesPage
from app.teacher.homework.object_page.paper_detail_page import PaperDetailPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class PaperAnalysis(unittest.TestCase):
    """本班试卷 - 答题分析"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.paper = PaperDetailPage()
        cls.game = GamesPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_paper_analysis(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                for i in range(len(van)):
                    if van[i].text == gv.VAN_PAPER:
                        van[i].click()  # 进入班级详情页
                        break
                if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 页面检查点

                    self.van.vanclass_paper()  # 进入 本班卷子
                    if self.detail.wait_check_page(gv.PAPER_ANALY):  # 页面检查点
                        if self.detail.judge_to_pool():  # 无卷子时
                            print('暂无卷子，去题库看看吧')
                            # self.detail.goto_paper_pool()  # 点击 去题库 按钮
                        else:  # 有卷子
                            print('本班试卷:')
                            self.paper_list_operate()

                            if self.paper.wait_check_page():  # 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_vanclass_page(gv.PAPER_ANALY):  # 本班卷子 页面检查点
                                    self.home.back_up_button()
                    else:
                        print('未进入 本班卷子页面')

                    if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 班级详情 页面检查点
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def paper_list_operate(self):
        """卷子列表 具体操作"""
        var = []
        name = self.detail.hw_name()  # 试卷name
        var.append(name[0].text)
        name[0].click()  # 进入试卷

        # k = 0
        # while k == 1:
        #     name = self.detail.hw_name()  # 试卷name
        #     for i in range(len(name)):
        #         text = name[i].text
        #         if text == '仁爱版九年级下册 期末测试卷（引用2）':
        #             var.append(text)
        #             name[i].click()  # 进入试卷
        #             k += 1
        #             break
        #         else:
        #             self.home.screen_swipe_up(0.5, 0.7, 0.2, 1000)

        if self.paper.wait_check_page():  # 页面检查点
            print('试卷:', var[0])
            self.answer_analysis_detail(['', ''])  # 答题分析页 作业list
        else:
            print('未进入试卷 %s 页面' % var[0])
            self.home.back_up_button()

    @teststeps
    def answer_analysis_detail(self, content):
        """答题分析 详情页"""
        name = self.paper.game_name()  # 作业name
        mode = self.paper.game_type()  # 作业type
        # level = self.detail.game_level()  # 作业 是否为提分版
        average = self.paper.van_average_achievement()  # 全班平均得分x分; 总分x分

        if len(mode) > 7 or len(content) == 0:
            index = []
            content = []
            for j in range(len(average)):  # 最多展示7道题, achievement的个数代表页面内能展示完全的题数
                print(mode[j].text, name[j].text, average[j].text)
                if mode[j].text == '强化炼句':
                    index.append(j)

                if j == len(average) - 1:
                    content.append(name[j].text)
                    content.append(mode[j].text)

            if len(index) != 0:  # 有题
                for i in range(len(index)):
                    if self.paper.wait_check_page():
                        name[index[i]].click()  # 点击 强化炼句
                        if self.game.wait_check_page():
                            self.game_detail_operate()
                        self.home.back_up_button()

            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.answer_analysis_detail(content)

            return content
        else:  # <=7 & 翻页
            if len(name) != len(name) != len(average):
                print('★★★ Error- 数目不等', len(name), len(name), len(average))
            else:
                var = 0
                for k in range(len(average)):
                    if content[0] == name[k].text:
                        var = k + 1
                        break
                index = []

                for j in range(var, len(average)):
                    print(mode[j].text, name[j].text, average[j].text)
                    if mode[j].text == '强化炼句':
                        index.append(j)

                if len(index) != 0:  # 还有其他题
                    for i in range(len(index)):
                        if self.paper.wait_check_page():
                            name[index[i]].click()  # 点击 强化炼句
                            if self.game.wait_check_page():
                                self.game_detail_operate()
                            self.home.back_up_button()

    @teststeps
    def game_detail_operate(self):
        """游戏详情页"""
        print('------------------------------------------')
        print('游戏详情页:')
        self.game.game_title()  # title
        count = self.game.game_info()[1:3]  # info
        self.game.teacher_nickname()  # 老师昵称
        print('------------------------')

        if self.game.verify_question_index():  # 单词类
            index = self.game.question_index()  # 题号
            word = self.game.word()  # 单词
            explain = self.game.explain()  # 解释
            for k in range(len(index)):
                print(index[k].text, word[k].text, explain[k].text)
                if self.game.verify_speak_button():
                    self.game.speak_button(k)
            last = index[-1].text

            if int(len(index)) > 6:
                self.game.screen_swipe_up(0.5, 0.95, 0.15, 1000)
                index = self.game.question_index()  # 题号
                word = self.game.word()  # 单词
                explain = self.game.explain()  # 解释
                for z in range(len(index)):
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
            for k in range(len(sentence)):
                print(sentence[k].text, hint[k].text)
                last.append(hint[k].text)

            if int(len(sentence)) > 3:
                self.game.screen_swipe_up(0.5, 0.95, 0.15, 1000)
                sentence = self.game.sentence()  # 句子
                hint = self.game.hint()  # 解释
                for z in range(len(sentence)):
                    num = hint[z].text
                    if num not in last:
                        print(sentence[z].text, hint[z].text)

        print('------------------------------------------')
