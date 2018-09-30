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
    def test_paper_detail_album(self):
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
                item[0][2].click()  # 点击第X个试卷

                if self.paper.wait_check_page():  # 页面检查点
                    self.paper.share_button()  # 分享 按钮
                    if self.paper.wait_check_share_page():
                        self.paper.share_page_info()  # 分享页面 信息

                        self.paper.school_upload_img()  # 学校徽标
                        if self.paper.wait_check_change_page():
                            print('学校徽标- 上传照片')
                            self.upload_img_operate()  # 学校徽标 上传图片操作
                            time.sleep(2)

                            self.paper.qr_upload_img()  # 二维码
                            if self.paper.wait_check_exchange_page():
                                print('二维码- 上传照片')
                                self.upload_img_operate()  # 二维码 上传图片操作
                                time.sleep(2)

                                self.question.back_up_button()  # 返回 试卷详情页
                                if self.paper.wait_check_page():  # 页面检查点
                                    self.question.back_up_button()  # 返回题库页面
                                    if self.question.wait_check_page('试卷'):
                                        self.home.click_tab_hw()

            else:
                print('未进入题库页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def upload_img_operate(self):
        """上传照片"""
        self.paper.click_album()  # 相册上传
        time.sleep(2)
        # if self.change_image.wait_check_page_album():  # 页面检查点
        # self.change_image.click_album()  # 切换到相册tab
        # time.sleep(1)
        self.change_image.choose_album()   # 选择相册
        time.sleep(1)
        self.change_image.choose_image()
        # time.sleep(1)
        # self.change_image.commit_button()
        time.sleep(2)
        self.change_image.click_save_button()

        if self.paper.wait_check_share_page():  # 页面检查点
            print('choose success')
        # else:
        #     print('choose failed')
