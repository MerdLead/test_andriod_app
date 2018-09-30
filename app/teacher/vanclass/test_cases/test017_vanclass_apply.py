#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.object_page.vanclass_student_info_page import StDetailPage
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class VanclassApply(unittest.TestCase):
    """入班申请"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.st = StDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_apply(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                text = van[1].text
                van[1].click()  # 进入班级详情页
                if self.van.wait_check_vanclass_page(text):  # class two

                    self.van.vanclass_application()  # 进入 入班申请
                    if self.detail.wait_check_page(text):  # 页面检查点
                        print('入班申请页面:')
                        if self.home.empty_tips():
                            print('暂时没有数据')
                            self.home.back_up_button()
                        else:
                            self.apply_operate(text)  # 同意 入班申请 具体操作
                            self.refuse_apply_operate()  # 拒绝 入班申请
                            if self.van.wait_check_vanclass_page(text):  # 入班申请 页面检查点
                                self.home.back_up_button()

                        if self.van.wait_check_vanclass_page(text):  # 班级详情 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_page():  # 班级 页面检查点
                                self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 入班申请页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def apply_operate(self, text):
        """入班申请 页面具体操作"""
        icon = self.detail.icon()  # icon
        st = self.detail.st_title()  # 名字
        nick = self.detail.st_nick()  # 昵称
        agree = self.detail.agree_button()  # 同意按钮

        item = []  # 同意入班的学生name及备注名
        if len(nick) < 8:  # 少于8个
            if len(icon) != len(st) != len(nick) != len(agree):
                print('★★★ Error- 学生icon、name、昵称、同意按钮个数不等')
            else:
                for i in range(len(st)):
                    if self.detail.wait_check_page(text):  # 页面检查点
                        print(' 学生:', st[i].text, '\n', "昵称:", nick[i].text)
                        print('-----------------------')
                        if i == 0:
                            item.append(st[i].text)
                            item.append(nick[i].text)
                            agree[i].click()
        else:  # todo 多于7个翻页
            print('todo 多于7个翻页:', len(nick))
            for i in range(7):
                if self.detail.wait_check_page(text):  # 页面检查点
                    print(' 学生:', st[i].text, '\n', "昵称:", nick[i].text)
                    print('-----------------------')
                    if i == 0:
                        item.append(st[i].text)
                        item.append(nick[i].text)
                        agree[i].click()
        print('---------------------------------')
        return len(st), item

    @teststeps
    def refuse_apply_operate(self):
        """拒绝入班申请 页面具体操作"""
        st = self.detail.st_title()  # 名字
        self.detail.open_menu(st[0])  # 申请学生条目 左键长按
        self.detail.menu_item(0)  # 拒绝 入班申请

    @teststeps
    def verification_result(self, var, item, van):
        """验证"""
        if self.home.empty_tips():
            if var != 1:
                print('★★★ Error- 原申请数为:', var)
        else:
            title = self.detail.st_title()  # 名字
            if len(title) != var-1:
                print('★★★ Error- 申请数未减一', len(title), var)
            else:
                if title[0].text == item[0]:
                    print('★★★ Error- 申请列表还存在该申请信息', item)

        self.home.back_up_button()  # 返回
        if self.van.wait_check_vanclass_page(van):
            self.van.vanclass_member()
            if self.detail.wait_check_page(van):  # 页面检查点
                self.detail.tips_operate(5)  # tips弹框
                if self.home.empty_tips():
                    print('★★★ Error- 同意入班失败，班级成员页面无数据')
                else:
                    st = self.detail.st_title()
                    st[0].click()  # 进入学生 具体信息页面
                    if self.st.wait_check_page():
                        name = self.st.st_name()  # 学生备注名
                        nick = self.st.st_nickname()  # 昵称
                        if item[0] != name and item[1] != nick:
                            print('★★★ Error- 同意入班失败，班级成员页面无该学生', item)
