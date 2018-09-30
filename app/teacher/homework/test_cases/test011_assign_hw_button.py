#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.question_bank.object_page.question_basket_page import QuestionBasketPage
from app.teacher.question_bank.object_page.question_detail_page import QuestionDetailPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class AssignHw(unittest.TestCase):
    """布置作业按钮"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.release = ReleasePage()
        cls.question = QuestionBankPage()
        cls.basket = QuestionBasketPage()
        cls.detail = QuestionDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_assign_button(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            name = self.draft_operate()  # 获取 草稿箱目前草稿数

            if self.home.wait_check_page():  # 页面检查点
                self.home.assign_hw_button()  # 布置作业 按钮
                if self.basket.wait_check_page():  # 页面检查点
                    self.add_to_basket()  # 若题筐为空，加题进题筐

                    self.question_bank_operate()  # 题筐内具体操作
                    name1 = self.draft_operate()  # 验证布置结果
                    if name1 != name + 1:
                        print('★★★ Error-', name, name1)
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def add_to_basket(self):
        """加入题筐"""
        if self.basket.load_empty():  # 如果存在空白页元素
            self.basket.empty_text()  # 空白文案
            self.basket.back_up_button()  # 返回按钮

            if self.home.wait_check_page():  # 页面检查点
                self.home.click_tab_question()  # 进入题库tab

                if self.question.wait_check_page():
                    item = self.question.question_name()  # 获取
                    item[0][0].click()  # 点击第一道题

                    if self.detail.wait_check_page():  # 页面检查点
                        self.detail.put_to_basket_button()  # 点击加入题筐按钮
                        self.question.back_up_button()  # 返回按钮

                        if self.question.wait_check_page():  # 页面检查点
                            self.question.question_basket()  # 题筐按钮

                            if self.basket.wait_check_page():  # 页面检查点
                                if self.basket.load_empty():  # 如果存在空白页元素
                                    print('★★★ Error- 加入题筐失败')

    @teststeps
    def question_bank_operate(self):
        """获取题筐所有题"""
        print('---------------------')
        print('题筐页面:')
        var = self.basket.all_element()
        self.assgin_operate(var)  # 布置作业

    @teststeps
    def assgin_operate(self, var):
        """布置作业"""
        if var > 1:
            for i in range(2):
                self.basket.check_button(i)  # 单选按钮

        assign = self.basket.assign_button()  # 点击布置作业 按钮
        assign.click()
        if self.release.wait_check_tips_page():  # 温馨提示 页面
            self.release.tips_title()
            self.release.tips_content()
            self.release.commit_button()

        if self.release.wait_check_release_page():  # 页面检查点
            button = self.release.put_into_button()  # 存入草稿 按钮
            button.click()

    @teststeps
    def draft_operate(self):
        """草稿箱 具体操作"""
        if self.home.wait_check_page():
            self.home.draft_box_button()  # 草稿箱 按钮

            if self.home.wait_check_drat_page():  # 页面检查点
                name = self.home.draft_name()
                create = self.home.draft_time()
                count = self.home.draft_count()
                print('---------------------')
                print('草稿箱')

                for i in range(len(count)):
                    print(name[i].text, '\n',
                          create[i].text, '\n',
                          count[i].text)
                    print('------------------')

                self.home.back_up_button()
                return len(name)
