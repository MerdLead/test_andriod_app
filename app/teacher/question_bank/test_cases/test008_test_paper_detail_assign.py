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
from app.teacher.question_bank.object_page.games_detail_page import GamesPage
from app.teacher.question_bank.object_page.test_paper_detail_page import PaperDetailPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class AssignPaper(unittest.TestCase):
    """布置试卷"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.question = QuestionBankPage()
        cls.paper = PaperDetailPage()
        cls.game = GamesPage()
        cls.filter = FilterPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_assign_paper(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('题单'):  # 页面检查点
                self.question.filter_button()  # 筛选按钮

                if FilterPage().wait_check_page():
                    paper = self.filter.test_paper()
                    if self.filter.selected(paper) == 'false':
                        self.filter.click_test_paper()  # 点击 试卷
                        self.filter.commit_button()  # 确定按钮
                    else:
                        self.filter.commit_button()  # 确定按钮

            if self.question.wait_check_page('试卷'):  # 页面检查点
                print('试卷:')
                item = self.question.question_name()  # 获取name

                if self.question.judge_question_lock():
                    lock = self.question.question_lock()  # 锁定的试卷数
                    item[0][len(lock)+2].click()  # 点击第X个试卷  todo 根据lock数点击未lock的
                else:
                    item[0][2].click()  # 点击第X个试卷

                if self.paper.wait_check_page():  # 页面检查点
                    title = self.paper_detail_operate()  # 试卷详情页 具体操作

                    self.paper.recommend_button()  # 推荐按钮
                    Toast().find_toast('操作成功')  # 获取toast

                    time.sleep(2)
                    self.paper.collect_button()  # 收藏按钮
                    Toast().find_toast('成功加入收藏')  # 获取toast

                    time.sleep(2)
                    self.assign_paper_operate()  # 布置试卷 具体操作

                    self.question.verify_collect_result(title, '试卷')  # 我的收藏 验证收藏结果
                    self.question.back_up_button()  # 返回按钮
                    if TuserCenterPage().wait_check_page():
                        self.home.click_tab_hw()  # 返回首页
            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def paper_detail_operate(self):
        """试卷 详情页"""
        print('------------------------------------------')
        content = self.paper.all_element()

        if content[1][4] != '试卷':
            print('★★★ Error- 试卷详情页的试卷类型')
        title = content[1][5]  # 返回值
        print('试卷详情页:', '\n',
              title, '\n',
              content[1][6], '\n',
              '----------------', '\n',
              content[1][9], content[1][7], content[1][8], '\n',
              content[1][12], content[1][10], content[1][11], '\n',
              content[1][15], content[1][14], content[1][13])
        if content[1][16] == '不限制':
            print('', content[1][17], content[1][16], '\n',
                  '----------------', '\n',
                  content[1][18], ':')
            k = 19
        else:
            print('', content[1][18], content[1][17], content[1][16], '\n',
                  '----------------', '\n',
                  content[1][19], ':')
            k = 20

        count = 0  # 代表有几个game
        for i in range(k, len(content[1]) - 2, 2):
            print('   ', content[1][i], content[1][i+1])
            count += 1

        return title

    @teststeps
    def assign_paper_operate(self):
        """布置试卷 具体操作 """
        self.paper.assign_button()  # 布置试卷
        self.paper.assign_page_info()
        self.paper.assign_button()  # 布置试卷 按钮
        Toast().find_toast('布置学生不能为空')

        ele = self.paper.choose_button()  # 班级 单选框
        ele[1].click()

        self.paper.assign_button()  # 布置试卷 按钮
        self.paper.tips_page_info()
