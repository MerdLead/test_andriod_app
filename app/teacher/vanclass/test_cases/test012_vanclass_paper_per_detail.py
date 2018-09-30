#!/usr/bin/env python
# encoding:UTF-8
import unittest

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.homework.object_page.paper_detail_page import PaperDetailPage
from app.teacher.vanclass.object_page.vanclass_detail_page import VanclassDetailPage
from app.teacher.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.vanclass.object_page.vanclass_page import VanclassPage
from app.teacher.vanclass.test_data.vanclass_data import GetVariable as gv
from conf.decorator import setup, teardown, testcase, teststeps
from utils.toast_find import Toast


class VanclassPaper(unittest.TestCase):
    """本班试卷 每个学生答题情况"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login = TloginPage()
        cls.home = ThomePage()
        cls.detail = VanclassDetailPage()
        cls.van = VanclassPage()
        cls.paper = PaperDetailPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_vanclass_paper_tab(self):
        self.login.app_status()  # 判断APP当前状态

        if self.home.wait_check_page():  # 页面检查点
            self.home.click_test_vanclass()  # 班级tab
            if self.van.wait_check_page():  # 页面检查点

                van = self.van.vanclass_name()  # 班级名称
                for i in range(len(van)):
                    if van[i].text == gv.VAN_PAPER:
                        van[i].click()  # 进入班级详情页
                        break
                if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 页面检查点

                    self.van.vanclass_paper()  # 进入 本班卷子
                    if self.detail.wait_check_page(gv.PAPER_ANALY):  # 页面检查点
                        if self.detail.judge_to_pool():  # 无卷子时
                            print('暂无卷子，去题库看看吧')
                            # self.detail.goto_paper_pool()  # 点击 去题库 按钮
                        else:  # 有卷子
                            print('%s 本班试卷:' % gv.VAN_PAPER)
                            name = self.detail.hw_name()  # 试卷name
                            var = [name[0].text]
                            name[0].click()  # 进入试卷

                            # for i in range(len(name)):
                            #     text = name[i].text
                            #     if text == '仁爱版九年级下册 期末测试卷（引用2）':
                            #         var.append(text)
                            #         name[i].click()  # 进入试卷
                            #         break

                            if self.paper.wait_check_page():  # 页面检查点
                                print('试卷:', var[0])
                                self.finish_situation_operate()  # 具体操作

                        self.home.back_up_button()
                        if self.paper.wait_check_page():  # 页面检查点
                            self.home.back_up_button()
                            if self.van.wait_check_vanclass_page(gv.PAPER_ANALY):  # 本班卷子 页面检查点
                                self.home.back_up_button()
                                if self.van.wait_check_vanclass_page(gv.VAN_PAPER):  # 班级详情 页面检查点
                                    self.home.back_up_button()
                                    if self.van.wait_check_page():  # 班级 页面检查点
                                        self.home.click_tab_hw()  # 返回主界面
                    else:
                        print('未进入 本班试卷页面')
                        self.home.back_up_button()
                        if self.van.wait_check_page():  # 班级 页面检查点
                            self.home.click_tab_hw()  # 返回主界面
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")

    @teststeps
    def finish_situation_operate(self):
        """完成情况tab 具体操作"""
        complete = self.paper.analysis_finished_tab(1)  # 完成情况 tab
        complete.click()  # 进入 完成情况 tab页
        name = self.paper.st_name()  # 学生name
        status = self.paper.st_score()  # 学生完成与否 todo
        print('得分情况:', status[0].text)
        text = name[0].text
        name[0].click()  # 进入一个学生的答题情况页

        if self.detail.wait_check_page(text[:-3]):  # 页面检查点
            print('学生 %s 答题情况:' % text[:-3])
            var = self.paper_detail_operate()  # 试卷 详情页
            self.operate(text[:-3], var)  # todo

    @teststeps
    def paper_detail_operate(self):
        """试卷 详情页"""
        print('------------------------------------------')
        content = self.paper.all_element()
        var = self.paper.paper_type()  # 类型

        if var.text != '试卷':
            print('★★★ Error- 试卷详情页的试卷类型')
        title = self.paper.paper_name()  # 试卷title
        print('试卷详情页:', '\n',
              title.text, '\n',
              '----------------', '\n',
              content[1][5], ':', content[1][3], content[1][4], '\n',
              content[1][8], ':', content[1][6], content[1][7], '\n',
              content[1][11], ':', content[1][9], content[1][10], '\n',
              content[1][14], ':', content[1][12], content[1][13], '\n',
              '----------------'
              )
        mode = self.paper.game_title()
        score = self.paper.game_score()
        info = self.paper.game_desc()

        print(content[1][15])
        item = []
        for i in range(len(info)):
            item.append(mode[i])
            print(mode[i].text, info[i].text, '    ', score[i+1].text)
        print('------------------------------')

        return item

    @teststeps
    def operate(self, st, item):
        """游戏 具体页面"""
        # todo 游戏 具体页面
        for i in range(len(item)):
            if self.detail.wait_check_page(st):  # 页面检查点
                text = item[i].text
                item[i].click()
                if self.detail.wait_check_page(text[:-3]):
                    self.paper.first_report()
                    self.home.back_up_button()
                    if self.detail.wait_check_page(text[:-3]) is False:  # 页面检查点
                        print('★★★ Error- 未返回 试卷详情页')
