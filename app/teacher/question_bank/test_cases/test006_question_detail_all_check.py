#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.question_bank.object_page.question_basket_page import QuestionBasketPage
from app.teacher.question_bank.object_page.question_detail_page import QuestionDetailPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.user_center.mine_collection.object_page.mine_collect import CollectionPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class QuestionDetail(unittest.TestCase):
    """题单详情"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.question = QuestionBankPage()
        cls.detail = QuestionDetailPage()
        cls.basket = QuestionBasketPage()
        cls.collect = CollectionPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_question_detail_all(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('题单'):  # 页面检查点
                self.detail.screen_swipe_up(0.5, 0.9, 0.1, 1000)

                # 由于直接获取时取不到元素，故跳转一下页面
                self.home.click_tab_hw()
                if self.home.wait_check_page():  # 页面检查点
                    self.home.click_tab_question()
                    print('---------------------')
                    print('题库:')
                    item = self.question.question_name()  # 获取
                    menu = item[1][1]
                    print(menu)
                    item[0][1].click()  # 点击第3道题
                    if self.detail.wait_check_page():  # 页面检查点
                        self.detail.recommend_button()  # 再次点击 推荐按钮
                        Toast().find_toast('推荐成功')  # 获取toast

                        time.sleep(2)
                        self.detail.collect_button()  # 取消收藏按钮

                        time.sleep(2)
                        self.detail.put_to_basket_button()  # 加入题筐 按钮
                        Toast().find_toast('添加题筐成功')  # 获取toast

                        time.sleep(2)
                        self.detail.put_to_basket_button()  # 再次点击 加入题筐 按钮
                        Toast().find_toast('已经全部加入题筐')  # 获取toast

                        time.sleep(2)
                        ele = self.detail.check_button()  # 单选按钮
                        for j in range(len(ele)):
                            if self.detail.enabled(ele[j]) is True:  # enabled 属性
                                print('★★★ Error- 单选按钮enabled状态')

                        self.detail.all_check_button()  # 全不选 按钮
                        time.sleep(2)
                        item = self.question.question_name()  # 获取题目
                        name = item[1][0]
                        self.question.back_up_button()  # 返回按钮

                        self.judge_result(menu, name)  # 验证结果
            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def judge_result(self, menu, name):
        """ 验证"""
        if self.question.wait_check_page('题单'):
            self.question.question_basket()  # 题筐
            if self.basket.wait_check_page():  # 页面检查点
                print('---------------------')
                print('题筐:')

                if len(name) == 1:
                    item = self.question.question_name()  # 获取题目
                    name1 = item[1][0]
                    print(name1)
                    if name != name1:
                        print('★★★ Error- 加入题筐失败', name, name1)
                elif 1 < len(name) < 10:
                    item = self.question.question_name()  # 获取题目
                    var = item[1].reverse()  # 执行reverse后,列表本身被反向
                    name1 = var[0]
                    if name != name1:
                        print('★★★ Error- 加入题筐失败', name, name1)

                self.judge_result_box(menu)

    @teststeps
    def judge_result_box(self, menu):
        """ 验证"""
        # if name != name1:
        #     print('★★★ Error- 加入题筐失败', name, name1)
        # else:  # 为了保证脚本每次都可以运行，故将加入题筐的大题移出
        self.basket.all_check_button()  # 全选 按钮
        time.sleep(2)
        self.basket.out_basket_button()  # 移出题筐 按钮

        if self.basket.wait_check_page():  # 页面检查点
            self.question.back_up_button()

            if self.question.wait_check_page('题单'):  # 页面检查点
                self.home.click_tab_profile()  # 个人中心
                if self.user.wait_check_page():  # 页面检查点
                    self.user.click_mine_collect()  # 我的收藏

                    if self.collect.wait_check_page():
                        print('---------------------')
                        print('我的收藏:')
                        item = self.question.question_name()  # 获取题目
                        if len(menu) == 1:
                            menu1 = item[1][0]
                            if menu != menu1:
                                print('★★★ Error- 加入题筐失败', menu, menu1)
                        elif 1 < len(menu) < 10:
                            var = item[1].reverse()  # 执行reverse后,列表本身被反向
                            menu1 = var[0]
                            if menu != menu1:
                                print('★★★ Error- 加入题筐失败', menu, menu1)

                        self.judge_result_collect(item)

    @teststeps
    def judge_result_collect(self, item):
        """ 验证"""
        for z in range(len(item[0])-1):
            if self.collect.wait_check_page():
                item = self.question.question_name()  # 获取
                print(item[1][0])
                self.collect.menu_button(0)  # 为了保证脚本每次都可以运行，故将加入收藏的题单取消收藏

                time.sleep(1)
                self.collect.cancel_collection()  # 取消收藏

        if self.collect.wait_check_page():
            self.question.back_up_button()  # 返回按钮
            if self.user.wait_check_page():  # 页面检查点
                self.home.click_tab_hw()  # 返回首页
