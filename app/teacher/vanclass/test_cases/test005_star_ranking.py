#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class StarRanking(unittest.TestCase):
    """星星排行榜"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_star_ranking(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                text = van[1].text
                van[1].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):  # 页面检查点

                    self.van.star_ranking()  # 进入 星星排行榜
                    if self.detail.wait_check_star_page():  # 页面检查点
                        print('星星排行榜:')
                        self.this_week_operate()  # 本周
                        self.last_week_operate()  # 上周
                        self.this_month_operate()  # 本月
                        self.all_score_operate()  # 全部

                        self.home.back_up_button()
                        if self.van.wait_check_vanclass_page(text):  # 班级详情 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_page():  # 班级 页面检查点
                                self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 星星排行榜页面')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def this_week_operate(self):
        """本周tab 具体操作"""
        this_week = self.detail.score_all_tab(1)
        if self.detail.selected(this_week) is False:
            print('★★★ Error- 默认在 本周页面')
        else:
            if self.van.empty_tips():
                print('暂无数据')
            else:
                print('本周学生列表:')
                self.score_operate()

    @teststeps
    def last_week_operate(self):
        """上周tab 具体操作"""
        last = self.detail.score_all_tab(2)  # 上周
        if self.detail.selected(last) is True:
            print('★★★ Error- 默认在 上周页面')
        else:
            last.click()  # 进入 上周 页面
            if self.detail.selected(last) is False:
                print('★★★ Error- 未进入 上周页面')
            else:
                print('----------------------------------------')
                if self.van.empty_tips():
                    print('暂无数据')
                else:
                    print('上周学生列表:')
                    self.score_operate()

    @teststeps
    def this_month_operate(self):
        """本月tab 具体操作"""
        this_month = self.detail.score_all_tab(3)  # 本月
        if self.detail.selected(this_month) is True:
            print('★★★ Error- 默认在 本月页面')
        else:
            this_month.click()  # 进入 本月 页面
            if self.detail.selected(this_month) is False:
                print('★★★ Error- 未进入 本月页面')
            else:
                print('----------------------------------------')
                if self.van.empty_tips():
                    print('暂无数据')
                else:
                    print('本月学生列表:')
                    self.score_operate()

    @teststeps
    def all_score_operate(self):
        """全部tab 具体操作"""
        all_score = self.detail.score_all_tab(4)  # 全部
        if self.detail.selected(all_score) is True:
            print('★★★ Error- 默认在 全部页面')
        else:
            all_score.click()  # 进入 全部 页面
            if self.detail.selected(all_score) is False:
                print('★★★ Error- 未进入 全部页面')
            else:
                print('----------------------------------------')
                if self.van.empty_tips():
                    print('暂无数据')
                else:
                    print('全部学生列表:')
                    self.score_operate()

    @teststeps
    def score_operate(self):
        """星星排行榜页面 具体操作"""
        order = self.detail.st_order()  # 编号
        icon = self.detail.st_icon()  # 头像
        name = self.detail.st_name()  # 昵称
        num = self.detail.num()  # 积分数
        if len(order) < 11:  # 少于8个
            if len(order) != len(icon) != len(name) != len(num):
                print('★★★ Error- 学生 编号、头像、昵称、积分的个数不等')
            else:
                for i in range(len(order)):
                    print('------------------')
                    print(order[i].text, name[i].text, num[i].text)
        else:  # 多于8个 todo
            print(len(order))
            for i in range(10):
                print('------------------')
                print(order[i].text, name[i].text, num[i].text)
