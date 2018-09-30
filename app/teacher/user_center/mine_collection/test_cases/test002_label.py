#!/usr/bin/env python
# encoding:UTF-8
import unittest

import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.question_bank.object_page.filter_page import FilterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.user_center.mine_collection.test_data.add_label import label_data
from app.teacher.user_center.mine_collection.object_page.mine_collect import CollectionPage
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast


class Collection(unittest.TestCase):
    """我的收藏 -- 标签"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.user = TuserCenterPage()
        cls.filter = FilterPage()
        cls.collect = CollectionPage()
        cls.question = QuestionBankPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_collection_label(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user.wait_check_page():  # 页面检查点
                self.user.click_mine_collect()  # 点击 我的收藏
                if self.collect.wait_check_page():  # 页面检查点
                    self.collect.menu_button(0)  # 右侧菜单按钮
                    time.sleep(1)
                    self.collect.recommend_to_school()  # 推荐到学校
                    print('推荐到学校')
                    Toast().find_toast('推荐成功')
                    print('----------------')

                    self.collect.menu_button(0)  # 右侧菜单按钮
                    time.sleep(1)
                    print('加入题筐')
                    self.collect.put_to_basket()  # 加入题筐
                    Toast().find_toast('添加成功')
                    print('----------------')

                    self.collect.menu_button(0)  # 右侧菜单按钮
                    time.sleep(1)
                    print('贴标签：')
                    self.collect.stick_label()  # 贴标签

                    if self.collect.wait_check_label_page():
                        self.collect.add_label()  # 创建标签

                        if self.collect.wait_check_tips_page():
                            self.collect.tips_title()
                            text = self.collect.input()
                            print(label_data[0]['label'])
                            text.send_keys(label_data[0]['label'])
                            if self.collect.positive_button():
                                self.collect.click_positive_button()  # 确定按钮

                                if self.collect.wait_check_label_page():
                                    self.collect.check_box(0)  # 选择标签
                                    self.collect.save_button()  # 保存按钮
                                    Toast().find_toast('贴标签成功')

                                    if self.collect.wait_check_page():  # 页面检查点
                                        self.collect.more_button()  # 更多 按钮
                                        time.sleep(2)
                                        self.collect.label_manage_button()  # 标签管理按钮

                                        if self.collect.wait_check_manage_page():
                                            # var = self.question.all_element()
                                            self.collect.add_label()  # 创建标签

                                            if self.collect.wait_check_tips_page():
                                                self.collect.tips_title()
                                                text = self.collect.input()
                                                print(label_data[1]['label'])
                                                text.send_keys(label_data[1]['label'])
                                                if self.collect.positive_button():
                                                    self.collect.click_positive_button()
                                                # var1 = self.question.all_element()
                                                # print(var, var1)

                                                if self.collect.wait_check_manage_page():
                                                    self.collect.back_up_button()  # 点击 返回按钮
                                                    if self.collect.wait_check_page():
                                                        self.home.back_up_button()
                                                        if self.user.wait_check_page():  # 页面检查点
                                                            self.home.click_tab_hw()  # 回首页
                                                            # todo 验证

                else:
                    print('未进入 我的收藏 页面')
            else:
                print('未进入个人中心页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")
