#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.homework.object_page.release_hw_page import ReleasePage
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
    def test_assign_button_draft(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.assign_hw_button()  # 布置作业 按钮
            if self.basket.wait_check_page():  # 页面检查点
                self.add_to_basket()  # 加题进题筐
                self.question_bank_operate()  # 获取题筐所有题

                self.question.back_up_button()  # 返回按钮
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

        ele = self.basket.assign_button()  # 点击布置作业 按钮
        ele.click()  # 点击

        if self.release.wait_check_tips_page():  # 温馨提示 页面
            self.release.tips_title()
            self.release.tips_content()
            self.release.commit_button()

        if self.release.wait_check_release_page():  # 页面检查点
            self.release.now_assign_button()  # 立即布置 按钮
            self.release.tips_page_info()  # 提示框
            try:
                Toast().find_toast('请输入作业名称')
            except Exception:
                raise

            self.release.screen_swipe_down(0.5, 0.4, 0.7, 1000)
            self.release_hw_operate()  # 发布作业 详情页
            self.release.now_assign_button()  # 立即布置 按钮
            self.release.tips_page_info()  # 提示框

    @teststeps
    def release_hw_operate(self):
        """发布作业 详情页"""
        if self.release.wait_check_release_page():  # 页面检查点
            print('----------------------------')
            ele = self.home.all_element()
            title = self.release.hw_title()
            name = self.release.hw_name_edit()

            name.send_keys('567')  # 修改name
            print(title, ":", name.text)  # 打印元素 作业名称
            print(ele[2].text, ":", ele[3].text)  # 打印元素 题目列表

            self.release.hw_mode_operate(ele)  # 作业模式 操作
            print(ele[6].text)  # 打印元素 发布作业到

            #self.release.screen_swipe_up(0.5, 0.8, 0.2, 1000)

            van = self.release.van_name()  # 班级名
            button = self.release.choose_button()  # 单选
            count = self.release.choose_count()  # 班级描述

            vanclass = []
            if len(button) != len(van):
                print('★★★ Error- 单选框的个数与班级个数不同', len(button), len(van))
            else:
                for i in range(len(count)):
                    print(van[i].text, '\n',
                          count[i].text)
                    print('-------')
                    vanclass.append(van[i].text)

            self.release.hw_adjust_order()  # 调整题目顺序
            self.release.confirm_button()  # 确定按钮

            if self.release.wait_check_release_page():  # 页面检查点
                self.choose_class_operate(van, vanclass)  # 选择班级 学生

                if self.release.wait_check_release_page():  # 页面检查点
                    button = self.release.put_into_button()  # 存入草稿 按钮
                    if self.release.enabled(button) is True:
                        print('★★★ Error- 存入草稿 按钮未置灰')
                else:
                    print('未返回 发布作业 页面')
            else:
                print('未返回 发布作业 页面')
        else:
            print('未进入 发布作业 页面')

    @teststeps
    def choose_class_operate(self, van, vanclass):
        """选择班级 学生"""
        print('----------------------------')
        button = self.release.choose_button()
        print('所选择的班级:', '\n',
              vanclass[0])
        button[0].click()  # 选择一个班

        van[1].click()  # 进入第二个班级
        print('-----------------', '\n',
              vanclass[1])
        if self.release.wait_check_class_page(vanclass[1]):
            st = self.release.st_title()  # 学生
            phone = self.release.st_phone()  # 手机号
            for i in range(len(phone)):
                print('  ', st[i].text, phone[i].text)
            print('------------------')

            button = self.release.choose_button()
            if len(button) > 3:
                for i in range(3):
                    button = self.release.choose_button()
                    button[i].click()  # 依次选择前三个学生
            else:
                button[0].click()
            self.release.confirm_button()  # 确定按钮

    @teststeps
    def judge_result_operate(self):
        """验证布置结果 具体操作"""
        if self.home.wait_check_page():  # 页面检查点
            name = self.home.item_detail()  # 条目名称
            vanclass = self.home.vanclass_name()  # 班级名称

            if name[0] != '567':
                print('★★★ Error- 布置失败', name[0])
            else:
                if vanclass[0] != '自动化测试2':
                    print('★★★ Error- 布置失败', vanclass[0])
