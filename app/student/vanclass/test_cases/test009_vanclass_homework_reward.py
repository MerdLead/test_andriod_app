#!/usr/bin/env python
# encoding:UTF-8
import unittest
import re

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.vanclass.object_page.vanclass_page import VanclassPage
from app.student.vanclass.test_data.vanclass_data import GetVariable as gv
from app.student.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class HwReward(unittest.TestCase):
    """本班作业 - 打卡"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = LoginPage()
        cls.home = HomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_homework_reward(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                for i in range(len(van)):
                    if van[i].text == gv.VAN_ANALY:
                        van[i].click()  # 进入班级详情页
                        break
                if self.van.wait_check_vanclass_page(gv.VAN_ANALY):  # 页面检查点

                    self.van.vanclass_hw()  # 点击 本班作业 tab
                    if self.detail.wait_check_page(gv.VAN_ANALY):  # 页面检查点
                        print('%s 本班作业:' % gv.VAN_ANALY)
                        if self.van.empty_tips():
                            print('暂无数据')
                        else:
                            all_hw = self.detail.all_finish_tab(1)  # 全部 tab
                            if self.detail.selected(all_hw) is False:
                                print('★★★ Error- 未默认在 全部页面')
                            else:
                                if self.van.empty_tips():
                                    print('暂无数据')
                                else:
                                    self.share_operate()  # 具体操作

                            self.home.back_up_button()  # 返回 本班作业页面
                            if self.detail.wait_check_page(gv.VAN_ANALY):  # 页面检查点
                                self.home.back_up_button()  # 返回 班级详情 页
                            else:
                                print('未返回 本班作业页面')
                    else:
                        print('未进入班级 -本班作业tab')
                        self.home.back_up_button()

                    if self.van.wait_check_page():  # 班级 页面检查点
                        self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def share_operate(self):
        """分享"""
        status = self.detail.finish_status()  # 已经有x人完成
        name = []
        for i in range(len(status)):
            count = re.sub("\D", "", status[i].text)
            if int(count) != 0:
                name = self.detail.hw_name()[i].text
                status[i].click()  # 进入作业
                break

        print(name, '\n',
              '----------------------------')
        if self.detail.wait_check_page(name):  # 页面检查点
            self.detail.reward_button()  # 打卡按钮
            if self.detail.wait_check_reward_page():
                if self.detail.reward_desc() != '您暂时无法打卡':
                    self.detail.reward_tips()  # 打卡说明
                    self.detail.reward_desc()  # 获取礼包提示
                    self.detail.get_reward_button()  # 礼包 按钮

                    if self.detail.wait_check_reward_result_page():
                        print('---------------------------')
                        if self.detail.reward_img():  # 打卡后 获得的图片
                            self.detail.reward_tips()  # 打卡说明
                            self.detail.reward_desc()  # 获取礼包提示

                            self.detail.check_complete_button()  # 查看完整卡片 按钮
                            if self.detail.wait_check_complete_page():
                                num = self.detail.img_num()
                                for i in range(len(num)):
                                    if num[i].text != 0:
                                        break

                                self.home.back_up_button()  # 返回
                        else:
                            print('★★★ Error- 无打卡图片')
                else:
                    self.detail.get_reward_button()  # 礼包 按钮
                    Toast().find_toast('暂时没有打卡机会了')
                    print(self.detail.reward_desc(), ',暂时没有打卡机会了')  # 打卡说明
                    self.detail.reward_tips()  # 获取礼包提示

                if self.detail.wait_check_reward_page():  # 页面检查点
                    self.home.back_up_button()  # 返回
                    if self.detail.wait_check_page(name):  # 页面检查点
                        self.home.back_up_button()  # 返回

        else:
            print('未进入作业 %s 页面' % name)
