#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.homework.object_page.paper_detail_page import PaperDetailPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class VanclassPaper(unittest.TestCase):
    """本班试卷 -- tab"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.paper = PaperDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_paper_tab(self):
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
                            print('%s 本班试卷:' % gv.VAN_PAPER)
                            name = self.detail.hw_name()  # 试卷name
                            var = [name[0].text]
                            name[0].click()  # 进入试卷
                            # for i in range(len(name)):
                            #     text = name[i].text
                            #     if text == '仁爱版九年级下册 期末测试卷（引用2）':
                            #         var.append(text)
                            #         name[i].click()  # 进入试卷
                            #         break

                            if self.paper.wait_check_page():  # 页面检查点
                                print('试卷:', var)
                                self.analysis_operate()  # 答题分析tab
                                self.finish_situation_operate()  # 完成情况tab

                        self.home.back_up_button()
                        if self.van.wait_check_vanclass_page(gv.PAPER_ANALY):  # 本班卷子 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 班级详情 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_page():  # 班级 页面检查点
                                    self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 本班试卷页面')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def analysis_operate(self):
        """答题分析tab 具体操作"""
        analysis = self.paper.analysis_finished_tab(0)  # 答题分析 tab
        if self.detail.selected(analysis) is False:
            print('★★★ Error- 未默认在 答题分析 tab页')
        else:
            print('--------------答题分析tab-------------------')
            self.hw_list_operate()  # 答题分析页 作业list

    @teststeps
    def finish_situation_operate(self):
        """完成情况tab 具体操作"""
        complete = self.paper.analysis_finished_tab(1)  # 完成情况 tab
        if self.detail.selected(complete) is True:
            print('★★★ Error- 默认在 完成情况 tab页')
        else:
            complete.click()  # 进入 完成情况 tab页
            if self.detail.selected(complete) is False:
                print('★★★ Error- 进入 完成情况 tab页')
            else:
                print('--------------完成情况tab-------------------')
                self.st_list_statistics()  # 未完成 学生列表信息统计

    @teststeps
    def hw_list_operate(self):
        """试卷列表 具体操作"""
        self.paper_operate('')  # 试卷列表
        # while not self.detail.end_tips():  # 如果list多于一页
        #     self.homework.screen_swipe_up(0.5, 0.75, 0.1, 1000)
        #     self.paper_operate(ele)  # 试卷列表

    @teststeps
    def paper_operate(self, item):
        """试卷列表"""
        name = self.paper.game_name()  # 作业name
        mode = self.paper.game_type()  # 作业type
        num = self.paper.game_num()  # 作业小题数
        # level = self.paper.game_level()  # 作业 是否为提分版
        average = self.paper.van_average_achievement()  # 全班平均得分x分; 总分x分

        if len(average) > 6:  # 作业 多于一页
            for i in range(len(name)-1):
                print('------------------')
                print(name[i].text, '\n',
                      mode[i].text, '\n',
                      num[i].text, '\n',
                      average[i].text)

            return name[-1].text
        else:  # 作业一页 and 翻页以后
            if len(item) != 0:
                if name[-1].text != item:  # 翻页成功
                    var = 0
                    for j in range(len(average)):
                        if item == name[j].text:
                            var = j+1
                    for i in range(var, len(average)):
                        print('------------------')
                        print(name[i].text, '\n',
                              mode[i].text, '\n',
                              num[i].text, '\n',
                              average[i].text)
            else:
                for i in range(len(average)):
                    print('------------------')
                    print(name[i].text, '\n',
                          mode[i].text, '\n',
                          num[i].text, '\n',
                          average[i].text)

            return name[-1].text

    @teststeps
    def st_list_statistics(self):
        """已完成/未完成 学生列表信息统计"""
        name = self.paper.st_name()  # 学生name
        icon = self.paper.st_icon()  # 学生头像
        status = self.paper.st_score()  # 学生完成与否 todo
        # arrow = self.detail.arrow_button()  # 转至按钮

        if len(name) == len(icon) == len(status):
            for i in range(len(name)):
                print('学生:', name[i].text, ' ', status[i].text)  # 打印所有学生信息
            print('--------------------')
        else:
            print('★★★ Error-已完成/未完成 学生列表信息统计', len(icon), len(name))
