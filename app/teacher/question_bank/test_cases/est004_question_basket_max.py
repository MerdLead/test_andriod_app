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
                self.question.page_source()
                item = self.question.question_name()  # 获取
                item[0][1].click()  # 点击第一道题

                if self.detail.wait_check_page():  # 页面检查点
                    self.detail.put_to_basket_button()  # 点击加入题筐按钮

                    if Toast().find_toast('已经加入题筐成功'):
                        self.already_add_operate()
                    elif Toast().find_toast('添加题筐成功'):
                        print('添加题筐成功')
                    elif Toast().find_toast('题筐最多还能加入0题'):
                        self.question.back_up_button()  # 返回按钮
                        self.judge_full_operate()  # 验证题筐已满 具体操作
                    else:
                        num = self.else_operate()  # 具体操作

                        if self.detail.wait_check_page():  # 页面检查点
                            self.basket.all_check_button()  # 全选按钮
                            for i in range(int(num)):
                                self.basket.check_button(i)  # 单选按钮
                            self.detail.put_to_basket_button()  # 点击加入题筐按钮

                    self.basket.back_up_button()  # 返回按钮
                    if self.question.wait_check_page('题单'):  # 页面检查点
                        self.home.click_tab_hw()  # 返回首页
            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def else_operate(self):
        """"""
        self.basket.back_up_button()  # 返回按钮
        if self.question.wait_check_page('题单'):  # 页面检查点
            self.question.question_basket()  # 题筐按钮
            if self.basket.wait_check_page():  # 页面检查点

                num = 50
                if self.basket.load_empty():  # 如果存在空白页元素
                    print('题筐无题')
                else:  # 题筐有题
                    self.basket.all_check_button()  # 全选按钮
                    ele = self.basket.assign_button()  # 布置作业 按钮
                    num = 50 - int(re.sub("\D", "", ele.text))  # 提取所选的题数

                self.basket.back_up_button()  # 返回按钮
                if self.question.wait_check_page('题单'):  # 页面检查点
                    item = self.question.question_name()  # 获取
                    item[0][0].click()  # 点击第一道题

                return num

    @teststeps
    def judge_full_operate(self):
        """题筐 验证已满 具体操作"""
        if self.question.wait_check_page():  # 页面检查点
            self.question.question_basket()  # 题筐按钮

            if self.basket.wait_check_page():  # 页面检查点
                if self.basket.load_empty():  # 如果存在空白页元素
                    print('★★★ Error- 加入题筐失败,空白页')
                else:  # 题筐不为空
                    self.basket.all_check_button()  # 全选按钮
                    ele = self.basket.assign_button()  # 布置作业 按钮
                    num = re.sub("\D", "", ele.text)  # 提取所选的题数
                    print(num)
                    if int(num) == 50:
                        print('题筐已满')
                    elif int(num) < 50:
                        print('★★★ Error- 加入题筐失败')   # todo 判断添加成功还是fail

                self.question.back_up_button()  # 返回按钮

    @teststeps
    def already_add_operate(self):
        """toast为: 已经加入题筐成功 时的具体操作"""
        self.question.back_up_button()
        self.basket.swipe_up_ele()  # 滑屏
        item = self.question.question_name()  # 获取
        item[0][0].click()  # 点击第一道题
        if self.detail.wait_check_page():  # 页面检查点
            self.detail.put_to_basket_button()  # 点击加入题筐按钮
