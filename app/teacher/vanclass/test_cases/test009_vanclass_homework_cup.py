#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.homework.object_page.homework_detail_page import HwDetailPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class HwCup(unittest.TestCase):
    """本班作业 - 奖杯"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.v_detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.detail = HwDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_homework_cup(self):
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
                            item = self.into_cup_operate()  # 进入 奖杯详情 页面
                            print(item)
                            if self.van.wait_check_vanclass_page(item):  # 作业 页面检查点
                                self.best_accurency()  # 奖杯页面 最优成绩tab
                                self.first_accurency()  # 奖杯页面 首次成绩tab
                            else:
                                print('未返回 本班作业页面')

                            self.home.back_up_button()  # 返回 答题详情页面
                            if self.detail.wait_check_page():  # 页面检查点
                                self.home.back_up_button()  # 返回 作业详情页面
                            else:
                                print('未返回 答题详情页面')

                        if self.van.wait_check_vanclass_page(gv.HW_ANALY):  # 本班作业 页面检查点
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
                            print('未返回班级页面')
                else:
                    print('未进入班级详情页')
            else:
                print('未进入班级页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def into_cup_operate(self):
        """进入 奖杯详情 页面"""
        name = self.v_detail.hw_name()  # 作业name
        for i in range(len(name)):
            if name[i].text == '测试作业2':
                name[i].click()  # 进入作业
                break

        if self.detail.wait_check_page():  # 页面检查点
            self.home.screen_swipe_up(0.5, 0.8, 0.2, 1000)
            mode = self.detail.game_type()  # 游戏类型
            name = self.detail.game_name()  # 游戏name
            cup = self.detail.cup_icon()  # 奖杯icon
            var = 0
            for j in range(len(cup)):
                if mode[j].text == '单项选择':
                    var = j
                    break

            item = name[var].text
            cup[var].click()  # 点击奖杯 icon

            return item

    @teststeps
    def best_accurency(self):
        """单个题目 答题详情 操作"""
        all_hw = self.v_detail.all_finish_tab(1)  # 全部 tab
        if self.v_detail.selected(all_hw) is False:
            print('★★★ Error- 未默认在 最优成绩页面')
        else:
            print('--------------最优成绩tab-------------------')
            if self.van.empty_tips():
                print('暂无数据')
            else:
                self.per_question_detail([''])

    @teststeps
    def first_accurency(self):
        """未完成tab 具体操作"""
        incomplete = self.v_detail.all_finish_tab(2)  # 未完成 tab
        if self.v_detail.selected(incomplete) is True:
            print('★★★ Error- 默认在 首次成绩 tab页')
        else:
            incomplete.click()  # 进入 首次成绩 tab页
            if self.v_detail.selected(incomplete) is False:
                print('★★★ Error- 进入 首次成绩 tab页')
            else:
                print('--------------首次成绩tab-------------------')
                if self.van.empty_tips():
                    print('暂无数据')
                else:
                    self.per_question_detail([''])

    @teststeps
    def per_question_detail(self, content):
        """单个题目 答题详情"""
        order = self.v_detail.st_order()  # 编号
        icon = self.v_detail.st_icon()  # 头像
        name = self.v_detail.st_name()  # 昵称
        accurency = self.v_detail.accurency()  # 正答率
        spend = self.v_detail.spend_time()  # 用时

        if len(order) > 5:
            content = []
            for j in range(len(order) - 1):
                print(order[j].text, name[j].text, accurency[j].text, spend[j].text)

            content.append(name[-1].text)  # 最后一个game的name
            self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
            self.per_question_detail(content)

            return content
        else:
            var = 0
            for k in range(len(icon)):
                if content[0] == name[k].text:
                    var += k
                    break

            for j in range(var, len(icon)):
                print(order[j].text, name[j].text, accurency[j].text, spend[j].text)
