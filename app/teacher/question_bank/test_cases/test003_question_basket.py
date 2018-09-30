#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import re
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.question_bank.object_page.question_basket_page import QuestionBasketPage
from app.teacher.question_bank.object_page.question_detail_page import QuestionDetailPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class QuestionBasket(unittest.TestCase):
    """题库 -- 题筐"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.question = QuestionBankPage()
        cls.basket = QuestionBasketPage()
        cls.detail = QuestionDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_question_basket(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('题单'):  # 页面检查点
                self.question.question_basket()  # 题筐按钮

                if self.basket.wait_check_page():  # 页面检查点
                    if self.basket.load_empty():  # 如果存在空白页元素
                        self.basket.empty_text()
                        self.basket.back_up_button()  # 返回按钮

                        self.add_to_basket()  # 加题进题筐
                        if self.question.wait_check_page('题单'):
                            self.home.click_tab_hw()  # 返回首页
                    else:  # 题筐有题
                        self.basket.all_check_button()  # 全选按钮
                        ele = self.basket.assign_button()  # 布置作业 按钮
                        num = re.sub("\D", "", ele.text)  # 提取所选的题数
                        print(num)
                        if int(num) == 50:
                            print('题筐已满')

                        if int(num) > 10:
                            ele = self.basket.assign_button()  # 布置作业 按钮
                            ele.click()
                            Toast().find_toast('布置作业一次不能超过10道题')  # 获取toast

                            self.question.back_up_button()  # 返回按钮
                            self.add_to_basket()  # 加题进题筐
                            if self.question.wait_check_page('题单'):
                                self.home.click_tab_hw()  # 返回首页
            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def add_to_basket(self):
        """加入题筐"""
        if self.question.wait_check_page('题单'):  # 页面检查点
            item = self.question.question_name()  # 获取
            item[0][6].click()  # 点击第一道题

            if self.detail.wait_check_page():  # 页面检查点
                item = self.question.question_name()  # 获取
                for i in range(len(item[1])):
                    print(item[1][i])
                print('---------------------')
                self.detail.put_to_basket_button()  # 点击加入题筐按钮
                self.question.back_up_button()  # 返回按钮

                if self.question.wait_check_page('题单'):  # 页面检查点
                    self.question.question_basket()  # 题筐按钮

                    if self.basket.wait_check_page():  # 页面检查点
                        if self.basket.load_empty():  # 如果存在空白页元素
                            print('★★★ Error- 加入题筐失败')
                        else:
                            self.basket_operate(item[1])  # 题筐具体操作

    @teststeps
    def basket_operate(self, var):
        """题筐具体操作"""
        name = var[-1]
        print('---------------------')
        print('题筐:')
        item = self.question.question_name()  # 获取题目
        name1 = item[1][0]
        print(name1)
        if name != name1:
            print('★★★ Error- 加入题筐失败', name, name1)
        else:
            self.basket.out_basket_button()  # 移出题筐按钮
            Toast().find_toast('请选择要移除的题目')

            for i in range(len(var)):
                self.basket.check_button(i)  # 单选按钮

            self.basket.screen_swipe_up(0.5, 0.75, 0.25, 1000)  # 滑屏一次
            for i in range(len(item[1])-1):
                self.basket.check_button(i)  # 单选按钮
            self.basket.out_basket_button()  # 移出题筐按钮

        if self.basket.wait_check_page():  # 页面检查点
            self.question.back_up_button()  # 返回按钮
