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
from app.teacher.user_center.user_information.object_page.change_image_page import ChangeImage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.edit_text import DelEditText
from utils.toast_find import Toast


class PaperDetail(unittest.TestCase):
    """试卷详情- 分享"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.question = QuestionBankPage()
        cls.paper = PaperDetailPage()
        cls.game = GamesPage()
        cls.change_image = ChangeImage()
        cls.filter = FilterPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_paper_share_edittext(self):
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
                print('------------------')
                item = self.question.question_name()  # 获取name
                item[0][2].click()  # 点击第X个试卷
                if self.paper.wait_check_page():  # 页面检查点
                    self.paper.share_button()  # 分享 按钮

                    if self.paper.wait_check_share_page():
                        self.paper.share_name()  # 页面名称
                        name = self.paper.share_name_edit()  # 编辑框
                        DelEditText().del_text(name)
                        name.send_keys('123')
                        print('修改为:', '123')
                        print('------------------')

                        time.sleep(1)
                        self.paper.share_school()
                        school = self.paper.share_school_edit()
                        DelEditText().del_text(school)
                        school.send_keys('school')
                        print('修改为:', 'school')
                        print('------------------')

                        time.sleep(1)
                        self.paper.share_contact()
                        contact = self.paper.share_contact_edit()
                        DelEditText().del_text(contact)
                        contact.send_keys('1234')
                        print('修改为:', '1234')
                        print('------------------')

                        time.sleep(1)
                        # self.share_control_operate()  # 分享控件

                        self.question.back_up_button()  # 返回 试卷详情页
                        if self.paper.wait_check_page():  # 页面检查点
                            self.question.back_up_button()  # 返回题库页面
                            if self.question.wait_check_page('试卷'):
                                self.question.filter_button()  # 筛选按钮
                                if FilterPage().wait_check_page():  # 页面检查点
                                    FilterPage().question_menu()  # 点击 题单
                                    FilterPage().commit_button()  # 确定按钮
                                    if self.question.wait_check_page('题单'):
                                        self.home.click_tab_hw()

            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def share_control_operate(self):
        """分享控件 选择操作"""
        self.paper.wechat_circle()
        if self.paper.wait_check_toast_page():  # 该校分享额度已用完 or 非合作校
            print('------------------------------------------')
            self.paper.tips_title()  # 提示
            self.paper.tips_content()  # 提示的内容
            self.paper.commit_button()  # 确定按钮
        # else:  # 可分享
        #

