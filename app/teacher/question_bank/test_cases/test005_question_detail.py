#!/usr/bin/env python
# encoding:UTF-8
import unittest
import time

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.question_bank.object_page.games_detail_page import GamesPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.question_bank.object_page.question_bank_page import QuestionBankPage
from app.teacher.question_bank.object_page.question_basket_page import QuestionBasketPage
from app.teacher.question_bank.object_page.question_detail_page import QuestionDetailPage
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
        cls.game = GamesPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_question_detail(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_tab_question()  # 进入首页后 点击 题库tab

            if self.question.wait_check_page('题单'):  # 页面检查点
                i = 0
                while i < 2:
                    self.detail.screen_swipe_up(0.5, 0.5, 0.1, 1000)
                    i += 1
                self.detail.screen_swipe_down(0.5, 0.1, 0.9, 1000)

                # 由于直接获取时取不到元素，故跳转一下页面
                self.home.click_tab_hw()
                if self.home.wait_check_page():  # 页面检查点
                    self.home.click_tab_question()

                    if self.question.wait_check_page('题单'):  # 页面检查点
                        print('---------------------')
                        print('题库:')
                        item = self.question.question_name()  # 获取
                        menu = item[1][3]  # 题单name
                        print('题单:', menu)

                        count = self.question.question_num(3)  # 该题单大题数
                        # num = re.sub("\D", "", count)  # 提取所选的题数

                        item[0][3].click()  # 点击第X道题单
                        if self.detail.wait_check_page():  # 页面检查点
                            # todo 题数验证
                            # count1 = self.game.game_info()
                            # num1 = re.findall(r'\d+(?#\D)', count1)[0]
                            self.question.question_count()
                            # if int(num) != int(num1):
                            #     print('★★★ Error- 题单大题数', num, num1)

                            item = self.question.question_name()  # 获取题目
                            ele = self.detail.check_button()  # 单选按钮

                            if len(item) < 10:
                                for i in range(len(item)):
                                    if self.detail.checked(ele[i]) is False:
                                        print('★★★ Error- 未默认全选')
                            else:
                                self.detail.swipe_up_ele()  # 滑屏一次
                                for i in range(4):
                                    if self.detail.checked(ele[i]) is False:
                                        print('★★★ Error- 未默认全选')

                            self.detail.recommend_button()  # 推荐按钮
                            Toast().find_toast('推荐成功')  # 获取toast

                            time.sleep(2)
                            self.detail.collect_button()  # 收藏按钮

                            time.sleep(2)
                            self.detail.all_check_button()  # 全不选 按钮

                            time.sleep(2)
                            ele = self.detail.check_button()  # 单选按钮
                            # if self.detail.checked(ele[2]) is False:  # 第三道题 单选按钮checked 属性
                            ele[2].click()  # 第三道题

                            print('---------------------')
                            print('单选:')
                            name = item[1][2]
                            print(name, len(item[1]), len(ele))

                            self.detail.put_to_basket_button()  # 加入题筐 按钮
                            Toast().find_toast('添加题筐成功')  # 获取toast

                            time.sleep(2)
                            self.detail.all_check_button()  # 全选 按钮

                            time.sleep(2)
                            ele = self.detail.check_button()  # 单选按钮
                            if self.detail.checked(ele[2]) is False:  # 第三道题 单选按钮checked 属性
                                print('★★★ Error- 单选按钮checked状态')
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
                item = self.question.question_name()  # 获取题目
                name1 = item[1][0]
                if name != name1:
                    print('★★★ Error- 加入题筐失败', name, name1)
                else:  # 为了保证脚本每次都可以运行，故将加入题筐的大题移出
                    print(name1)
                    button = self.detail.check_button()  # 单选 按钮
                    button[0].click()
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
                                item = self.question.question_name()  # 获取
                                menu1 = item[1][0]
                                if menu != menu1:
                                    print('★★★ Error- 加入收藏失败', menu, menu1)
                                else:
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
