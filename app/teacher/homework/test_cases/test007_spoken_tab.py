#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.homework.object_page.spoken_detail_page import SpokenDetailPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Spoken(unittest.TestCase):
    """口语 按题查看&按学生查看 tab页详情"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = HwDetailPage()
        cls.speak = SpokenDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_spoken_analysis_detail(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            if self.home.wait_check_no_page():
                print('无最新动态 -- (用户指南) 欢迎使用在线助教,打开看看吧!')
            else:
                name = self.home.get_type('口语')
                var = name[0][name[1][1]].text  # 作业名称
                name[0][name[1][1]].click()  # 进入作业

                if self.speak.wait_check_spoken_page():  # 页面检查点
                    print('口语:', var)
                    mode = self.detail.game_type()  # 游戏类型
                    name = self.detail.game_name()  # 游戏name
                    print(mode[0].text, name[0].text)
                    name[0].click()  # 进入口语游戏

                    if self.speak.wait_check_spoken_detail_page():  # 页面检查点
                        self.question_analysis_operate()  # 按题查看 tab
                        self.st_analysis_operate()  # 按学生查看 tab

                        if self.speak.wait_check_spoken_detail_page():  # 页面检查点
                            self.home.back_up_button()  # 返回
                            if self.speak.wait_check_spoken_page():  # 页面检查点
                                self.home.back_up_button()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def question_analysis_operate(self):
        """按题查看tab 具体操作"""
        analysis = self.detail.analysis_finished_tab(1)  # 答题分析 tab
        if self.detail.selected(analysis) is False:
            print('★★★ Error- 未默认在 按题查看 tab页')
        else:
            print('--------------按题查看tab-------------------')
            if self.detail.load_empty():
                print('暂无数据')
            else:
                self.answer_analysis_detail(['', ''])  # 答题分析页 作业list

    @teststeps
    def st_analysis_operate(self):
        """按学生查看tab 具体操作"""
        complete = self.detail.analysis_finished_tab(2)  # 完成情况 tab
        if self.detail.selected(complete) is True:
            print('★★★ Error- 默认在 按学生查看 tab页')
        else:
            complete.click()  # 进入 按学生查看 tab页
            if self.detail.selected(complete) is False:
                print('★★★ Error- 进入 按学生查看 tab页')
            else:
                print('--------------按学生查看tab-------------------')
                if self.detail.load_empty():
                    print('暂无数据')
                else:
                    self.st_list_statistics()  # 未完成 学生列表信息统计

    @teststeps
    def answer_analysis_detail(self, content):
        """按题查看 详情页"""
        sentence = self.speak.sentence()  # 游戏题目
        finish = self.speak.finish_ratio()  # 游戏完成率
        voice = self.speak.spoken_speak()  # 发音按钮

        if len(voice) > 8 and content[0] == '':
            content = []
            for j in range(len(finish) - 1):
                print(sentence[j].text, finish[j].text)

            content.append(sentence[-1].text)  # 最后一个game的name
            content.append(finish[-1].text)  # 最后一个game的完成率
            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.answer_analysis_detail(content)

            return content
        else:
            var = 0
            for k in range(len(voice)):
                if content[0] == sentence[k].text and content[1] == finish[k].text:
                    var += k
                    break

            for j in range(var, len(voice)):
                print(sentence[j].text, finish[j].text)

    @teststeps
    def st_list_statistics(self):
        """按学生查看"""
        name = self.speak.st_name()  # 学生name
        icon = self.speak.st_icon()  # 学生头像
        status = self.speak.st_finish_status()  # 学生完成与否 todo
        # arrow = self.detail.arrow_button()  # 转至按钮

        if len(name) == len(icon) == len(status):
            for i in range(len(name)):
                print('学生:', name[i].text, ' ', status[i].text)  # 打印所有学生信息
            print('--------------------')
