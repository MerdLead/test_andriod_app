#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.question_bank.object_page.filter_page import FilterPage
from app.teacher.question_bank.object_page.question_basket_page import QuestionBasketPage
from app.teacher.user_center.mine_collection.object_page.mine_collect import CollectionPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class QuestionBankPage(BasePage):
    """题库 页面"""

    @teststeps
    def wait_check_page(self, var):
        """以“搜索框中灰字:搜索”的text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % var)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def search_box(self):
        """以“输入框”的id为依据"""
        ele = self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/input')
        return ele

    @teststep
    def question_basket(self):
        """以 题筐 按钮的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/fab_pool") \
            .click()

    @teststep
    def filter_button(self):
        """以“筛选 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/filter") \
            .click()

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        content = []
        for i in range(len(ele)):
            # print(ele[i].text)
            content.append(ele[i].text)
        return ele, content

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    # 搜索框
    @teststeps
    def wait_check_game_type_page(self):
        """以“大题”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.vanthinkteacher.debug:id/type')]")
        try:
            WebDriverWait(self.driver, 3, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def drop_down_button(self):
        """以“下拉 按钮”的id为依据"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/choose_menu")
        print('选定的搜索条件：', ele.text)
        print('-------------------')
        return ele, ele.text

    @teststep
    def search_criteria_menu(self):
        """以“下拉 菜单”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/title")
        return ele

    @teststep
    def input_clear_button(self):
        """以“清空 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/input_clear") \
            .click()

    @teststep
    def search_button(self):
        """以“搜索 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/search") \
            .click()

    @teststep
    def search_icon(self):
        """以“历史搜索词 的icon”的class name为依据"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.ImageView")
        return ele

    @teststep
    def history_search(self):
        """以“历史搜索词”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/text")
        content = []
        print('历史搜索词:')
        for i in range(len(ele)-1):
            print(ele[i].text)
            content.append(ele[i].text)
        print('---------------------')
        return ele, content

    @teststep
    def delete_button(self, index):
        """以“删除 按钮”的id为依据"""
        self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/delete")[index] \
            .click()

    # 题单
    @teststep
    def question_type(self, index):
        """以“类型”的id为依据"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/type")[index].\
            text
        return item

    @teststep
    def question_perfect(self, index):
        """以 加“精”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/perfect")[index]
        return ele

    @teststep
    def question_num(self, index):
        """以“数量”的id为依据"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/exercise_num")[index].text
        return item

    @teststep
    def question_author(self, index):
        """以“作者”的id为依据"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/author")[index].text
        return item

    @teststep
    def question_author_index(self):
        """以“作者”的id为依据"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/author")
        return item

    @teststep
    def question_name(self):
        """以“题目名称”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/test_bank_name")
        content = []
        for i in range(len(ele)):
            content.append(ele[i].text)
            # print(ele[i].text)
        # print('---------------------')
        return ele, content

    # 大题
    @teststep
    def question_level(self, index):
        """以“题目等级”的id为依据"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/level")[index]
        return item

    @teststep
    def judge_question_lock(self):
        """判断页面内是否存在 lock 标识"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/lock")
            return True
        except:
            return False

    @teststep
    def question_lock(self):
        """以“题目是否锁定”的id为依据"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/lock") \
            .text
        return item

    @teststeps
    def choose_condition(self, var):
        """选择搜索条件"""
        print('搜索条件：')
        for i in range(len(var)):
            print(var[i].text)
        print('-------------------')

    @teststeps
    def swipe_operate(self):
        """加入题筐的大题"""
        i = 0
        while i < 7:
            item = self.question_info()  # 滑动前页面内大题情况
            self.screen_swipe_up(0.5, 0.85, 0.2)

            item1 = self.question_info()  # 滑动后页面内大题情况
            if item[2] == item1[2]:  # 滑到底部
                print('滑动前到底部')
                break
            else:
                self.screen_swipe_up(0.5, 0.85, 0.2)
                i += 1

    @teststeps
    def question_count(self, count=0):
        """统计题单内大题数"""
        item = self.question_info()  # 滑动前页面内大题情况
        self.screen_swipe_up(0.5, 0.85, 0.2, 1000)

        item1 = self.question_info()  # 滑动后页面内大题情况
        if item[2] == item1[2]:  # 滑到底部
            print('滑动前到底部', count)
            count = len(item[0])
        else:
            if item[2] in item1[2]:  # 滑动后到底
                print('滑动后到底部')
                index = []
                for j in range(len(item1[0])-1, 0):
                    if item1[0][j] == item[2]:
                        index.append(j)

                if len(index) != 0:
                    count = len(item1[0])-1 - index[0] + count
                else:
                    count = len(item1[0]) - 1 + count
            else:  # 滑动后未到底
                print('滑动后未到底部')
                index = []
                for j in range(len(item1[0]) - 1, 0):
                    if item1[0][j] == item[2]:
                        index.append(j)

                if len(index) != 0:
                    count = len(item1[0])-1 - index[0] + count
                else:
                    count = len(item1[0]) - 1 + count
                self.question_count(count)

        return count

    @teststeps
    def question_info(self):
        """获取页面内所有大题数量 及 页面内第一个/最后一个大题的title """
        question_title = self.question_name()  # 获取大题title列表
        first_one = question_title[1][0]  # 第一个大题的title
        last_one = question_title[1][-1]  # 最后一个大题的title

        return question_title[1], first_one, last_one

    @teststeps
    def verify_collect_result(self, menu, var):
        """验证 添加收藏 结果"""
        if self.wait_check_page(var):
            ThomePage().click_tab_profile()  # 个人中心
            if TuserCenterPage().wait_check_page():

                TuserCenterPage().click_mine_collect()  # 我的收藏
                if CollectionPage().wait_check_page():
                    print('------------------------------------------')
                    print('我的收藏:')
                    FilterPage().all_element()
                    if var == '大题':
                        self.filter_button()  # 筛选按钮
                        if FilterPage().wait_check_page():
                            FilterPage().click_game_list()  # 点击大题
                            FilterPage().commit_button()  # 确定按钮
                    elif var == '试卷':
                        self.filter_button()  # 筛选按钮
                        if FilterPage().wait_check_page():
                            CollectionPage().click_test_paper()  # 点击试卷
                            FilterPage().commit_button()  # 确定按钮

                    if CollectionPage().wait_check_page():
                        item = self.question_name()  # 获取
                        menu1 = item[1][0]
                        if '提分' in menu:
                            menu = menu[:-2]
                        if menu != menu1:
                            print('★★★ Error- 加入收藏失败', menu, menu1)
                        else:
                            for z in range(len(item[0])):
                                print(item[1][z])
                                if CollectionPage().wait_check_page():
                                    CollectionPage().menu_button(0)  # 为了保证脚本每次都可以运行，故将加入收藏的题单取消收藏

                                    time.sleep(1)
                                    CollectionPage().cancel_collection()  # 取消收藏

    @teststeps
    def verify_basket_result(self, name):
        """验证 加入题筐 结果"""
        if self.wait_check_page():
            self.question_basket()  # 题筐
            print('------------------------------------------')
            print('题筐:')
            item = self.question_name()  # 获取题目
            name1 = item[1][0]
            if '提分' in name:  #
                name = name[:-2]
            if name != name1:
                print('★★★ Error- 加入题筐失败', name, name1)
            else:  # 为了保证脚本每次都可以运行，故将加入题筐的大题移出
                button = QuestionBasketPage().check_button(0)  # 单选 按钮
                button.click()
                QuestionBasketPage().out_basket_button()  # 移出题筐 按钮
            self.back_up_button()
