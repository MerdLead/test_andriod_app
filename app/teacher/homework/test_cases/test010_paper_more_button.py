#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.paper_detail_page import PaperDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class Homework(unittest.TestCase):
    """试卷 更多按钮"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.release = ReleasePage()
        cls.paper = PaperDetailPage()
  
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_paper_more_button(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            if self.home.wait_check_no_page():
                print('无最新动态 -- (用户指南) 欢迎使用在线助教,打开看看吧!')
            else:
                self.home.screen_swipe_up(0.5, 0.85, 0.1, 1000)
                name = self.home.get_type('试卷')
                var = name[0][name[1][1]].text  # 作业名称
                name[0][name[1][1]].click()  # 进入作业

                if self.paper.wait_check_page():  # 页面检查点
                    print('进入试卷:', var)
                    self.paper.more_button()  # 更多 按钮
                    time.sleep(2)
                    self.paper.edit_delete_button(0)  # 编辑按钮
                    if self.paper.wait_check_edit_page():  # 页面检查点
                        self.edit_hw_operate()  # 编辑 具体操作

                    if self.paper.wait_check_page():  # 页面检查点
                        self.paper.more_button()  # 更多 按钮
                        time.sleep(2)
                        self.paper.edit_delete_button(1)  # 删除按钮
                        self.tips_page_info()  # 删除提示框

                        if self.paper.wait_check_page():  # 页面检查点
                            self.home.back_up_button()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def edit_hw_operate(self):
        """编辑试卷 详情页"""
        if self.release.wait_check_tips_page():  # 温馨提示 页面
            self.release.tips_title()
            self.release.tips_content()
            self.release.commit_button()

        if self.paper.wait_check_edit_page():  # 页面检查点
            print('----------------------------')
            ele = self.home.all_element()
            print(ele[1].text, '\n',
                  ele[2].text)
            # title = self.release.hw_title()
            # name = self.release.hw_name_edit()
            # todo

    @teststeps
    def tips_page_info(self):
        """温馨提示 页面信息"""
        print('------------------------------------------')
        print('删除提示 页面:')

        if self.release.wait_check_tips_page():
            self.release.tips_title()
            self.release.tips_content()
            self.release.cancel_button()  # 取消按钮
        else:
            print('★★★ Error- 无删除提示框')
