#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.games_detail_page import GamesPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class HwAnalysis(unittest.TestCase):
    """本班作业 - 答题分析"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.v_detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.detail = HwDetailPage()
        cls.game = GamesPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_homework_analysis(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                for i in range(len(van)):
                    if van[i].text == gv.VAN_ANALY:
                        van[i].click()  # 进入班级详情页
                        break
                if self.van.wait_check_vanclass_page(gv.VAN_ANALY):  # 页面检查点

                    self.van.vanclass_hw()  # 点击 本班作业 tab
                    if self.v_detail.wait_check_page(gv.HW_ANALY):  # 页面检查点
                        print('%s 本班作业:' % gv.VAN_ANALY)
                        if self.van.empty_tips():
                            print('暂无数据')
                        else:
                            self.hw_operate()  # 具体操作

                            self.home.back_up_button()  # 返回 答题详情页面
                            if self.detail.wait_check_page():  # 页面检查点
                                self.home.back_up_button()  # 返回 本班作业页面
                            else:
                                print('未返回 答题详情页面')

                        if self.v_detail.wait_check_page(gv.HW_ANALY):  # 页面检查点
                            self.home.back_up_button()  # 返回 班级详情页面
                            if self.van.wait_check_vanclass_page(gv.VAN_ANALY):  # 班级详情 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_page():  # 班级 页面检查点
                                    self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入班级 -本班作业tab')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def hw_operate(self):
        """作业列表"""
        name = self.v_detail.hw_name()  # 作业name
        for i in range(len(name)):
            if name[i].text == gv.HW_ANALY_GAME:
                name[i].click()  # 进入作业
                break

        if self.detail.wait_check_page():  # 页面检查点
            # todo 获取toast 无需答题报告  or
            self.answer_detail([])
        else:
            print('未进入作业 %s 页面' % '测试作业2')
            self.home.back_up_button()

    @teststeps
    def answer_detail(self, content):
        """答题情况详情页"""
        print('---------------------------------------')
        mode = self.detail.game_type()  # 游戏类型
        name = self.detail.game_name()  # 游戏name
        average = self.detail.average_achievement()  # 全班首轮平均成绩
        cup = self.detail.cup_icon()  # 奖杯icon

        if len(mode) > 6 or len(content) == 0:
            index = []
            content = []
            for j in range(len(average)):  # 最多展示7道题, achievement的个数代表页面内能展示完全的题数
                print(mode[j].text,  name[j].text, average[j].text)
                if mode[j].text == '单项选择':
                    index.append(j)

                if j == len(average)-1:
                    content.append(name[j].text)
                    content.append(mode[j].text)

            if len(index) != 0:  # 有题
                name[index[0]].click()  # 点击game单项选择
                if self.game.wait_check_page():
                    self.game_detail_operate()

            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.answer_detail(content)

            return content
        else:  # <7 & 翻页
            if len(name) != len(cup) != len(name) != len(average):
                print('★★★ Error- 数目不等', len(name), len(cup), len(name), len(average))
            else:
                var = 0
                for k in range(len(average)):
                    if content[0] == name[k].text:
                        var = k+1
                        break
                index = []

                for j in range(var, len(average)):
                    print(mode[j].text, name[j].text, average[j].text)
                    if mode[j].text == '单项选择':
                        index.append(j)

                if len(index) != 0:  # 还有其他题
                    for i in range(len(index)):
                        text = name[index[i]].text

                        name[index[i]].click()  # 点击 单项选择
                        if self.detail.wait_check_page(text):
                            self.game_detail_operate()

    @teststeps
    def game_detail_operate(self):
        """游戏详情页"""
        print('------------------------------------------')
        print('游戏详情页:')
        self.game.game_title()  # title
        count = self.game.game_info()[1]  # info
        self.game.teacher_nickname()  # 老师昵称

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
