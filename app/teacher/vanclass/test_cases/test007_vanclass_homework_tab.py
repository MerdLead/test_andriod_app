#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Homework(unittest.TestCase):
    """本班作业 - 答题分析& 完成情况tab"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = HwDetailPage()
        cls.van = VanclassPage()
        cls.v_detail = VanclassDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_answer_analysis_detail(self):
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
                            name = self.v_detail.hw_name()  # 作业name
                            var = name[1].text
                            name[1].click()  # 进入作业

                            if self.detail.wait_check_page():  # 页面检查点
                                print('作业:', var)
                                self.analysis_operate()  # 答题分析 tab
                                self.finish_situation_operate()  # 完成情况 tab
                                self.home.back_up_button()  # 返回 本班作业 页面

                        if self.detail.wait_check_page():  # 页面检查点
                            self.home.back_up_button()  # 返回 作业详情页面
                            if self.van.wait_check_vanclass_page(gv.HW_ANALY):  # 作业详情 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_vanclass_page(gv.VAN_ANALY):  # 班级详情 页面检查点
                                    self.home.back_up_button()
                                    if self.van.wait_check_page():  # 班级 页面检查点
                                        self.home.click_tab_hw()  # 返回主界面

            print('##########################################')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def analysis_operate(self):
        """答题分析tab 具体操作"""
        analysis = self.detail.analysis_finished_tab(0)  # 答题分析 tab
        if self.detail.selected(analysis) is False:
            print('★★★ Error- 未默认在 答题分析 tab页')
        else:
            print('--------------答题分析tab-------------------')
            self.answer_analysis_detail(['', ''])  # 答题分析页 作业list

    @teststeps
    def finish_situation_operate(self):
        """完成情况tab 具体操作"""
        complete = self.detail.analysis_finished_tab(1)  # 完成情况 tab
        if self.detail.selected(complete) is True:
            print('★★★ Error- 默认在 完成情况 tab页')
        else:
            complete.click()  # 进入 完成情况 tab页
            if self.detail.selected(complete) is False:
                print('★★★ Error- 进入 完成情况 tab页')
            else:
                print('--------------完成情况tab-------------------')
                if self.detail.load_empty():
                    print('暂无数据')
                else:
                    self.st_list_statistics()  # 未完成 学生列表信息统计

    @teststeps
    def answer_analysis_detail(self, content):
        """答题分析 详情页"""
        mode = self.detail.game_type()  # 游戏类型
        name = self.detail.game_name()  # 游戏name
        average = self.detail.average_achievement()  # 全班首轮平均成绩

        if len(mode) > 5 and content[0] == '':
            content = []
            for j in range(len(mode) - 1):
                print(mode[j].text, name[j].text, average[j].text)

            content.append(name[-1].text)  # 最后一个game的name
            content.append(mode[-1].text)  # 最后一个game的type
            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.answer_analysis_detail(content)

            return content
        else:
            mode = self.detail.game_type()  # 游戏类型
            name = self.detail.game_name()  # 游戏name
            average = self.detail.average_achievement()  # 全班首轮平均成绩

            var = 0
            for k in range(len(mode)):
                if content[0] == name[k].text and content[1] == mode[k].text:
                    var += k
                    break

            for j in range(var, len(mode)):
                print(mode[j].text, name[j].text, average[j].text)

    @teststeps
    def st_list_statistics(self):
        """已完成/未完成 学生列表信息统计"""

        name = self.detail.st_name()  # 学生name
        icon = self.detail.st_icon()  # 学生头像
        status = self.detail.st_finish_status()  # 学生完成与否 todo
        # arrow = self.detail.arrow_button()  # 转至按钮

        if len(name) == len(icon) == len(status):
            for i in range(len(name)):
                print('学生:', name[i].text, ' ', status[i].text)  # 打印所有学生信息
            print('--------------------')
            text = name[0].text
            name[0].click()  # 进入一个学生的答题情况页

            if self.v_detail.wait_check_page(text):  # 页面检查点
                print('学生 %s 答题情况:' % text)
                self.per_answer_detail(['', ''])  # 答题情况详情页 展示不全 滑屏
        else:
            print('★★★ Error-已完成/未完成 学生列表信息统计', len(icon), len(name))

    @teststeps
    def per_answer_detail(self, content):
        """个人 答题情况详情页"""
        mode = self.detail.game_type()  # 游戏类型
        name = self.detail.game_name()  # 游戏name
        num = self.detail.game_num()  # 游戏 小题数
        optimal = self.detail.optimal_achievement()  # 最优成绩
        first = self.detail.first_achievement()  # 首次成绩

        if len(mode) > 5 and content[0] == '':
            content = []
            for j in range(len(mode) - 1):
                print(mode[j].text, num[j].text, name[j].text, optimal[j].text, first[j].text)

            content.append(name[-2].text)  # 最后一个game的name
            content.append(mode[-2].text)  # 最后一个game的type
            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.per_answer_detail(content)

            return content
        else:
            if content[0] != name[-1].text and content[1] != mode[-1].text:
                var = 0
                for k in range(len(mode)):
                    if content[0] == name[k].text and content[1] == mode[k].text:
                        var += k + 1
                        break

                for j in range(var, len(mode)):
                    print(mode[j].text, num[j].text, name[j].text, optimal[j].text, first[j].text)
