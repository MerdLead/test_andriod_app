#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class HwDetailPage(BasePage):
    """ 作业详情 页面"""

    @teststeps
    def wait_check_page(self):
        """以“title: 答题分析”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'答题分析')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widgetFen.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        # for i in range(len(ele)):
        #     print(ele[i].text)
        return ele

    @teststep
    def load_empty(self):
        """暂时没有数据"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/load_empty")
            return True
        except Exception:
            return False

    @teststep
    def analysis_finished_tab(self, index):
        """答题分析 & 完成情况 index = 0/1"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView")[index]
        return ele

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

    @teststep
    def answer_detail_button(self):
        """答题详情 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/details") \
            .click()

    @teststep
    def more_button(self):
        """更多 按钮"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageView")\
            .click()

    @teststep
    def edit_delete_button(self, index):
        """编辑& 删除 按钮"""
        self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/title")[index] \
            .click()

    # 已完成/未完成 学生列表
    @teststep
    def st_type(self):
        """基础班/提分版学生"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/type")
        return ele

    @teststep
    def st_icon(self):
        """学生 头像"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_student_icon")
        return ele

    @teststep
    def st_finish_status(self):
        """学生 完成与否"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_finish_status")
        return ele

    @teststep
    def st_name(self):
        """学生 昵称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_student_name")
        return ele

    # 班级 答题详情 页面
    @teststeps
    def wait_check_detail_page(self):
        """以“title:答题详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'答题详情')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def game_type(self):
        """游戏类型"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/type")
        return ele

    @teststep
    def game_level(self):
        """提分"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/level")
        return ele

    @teststep
    def game_num(self):
        """共x题"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/exercise_num")
        return ele

    @teststep
    def game_name(self):
        """游戏 名称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/test_bank_name")
        return ele

    @teststep
    def average_achievement(self):
        """全班首轮平均成绩x%"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_testbank_status")
        return ele

    @teststep
    def cup_icon(self):
        """奖杯 icon"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_cup")
        return ele

    # 点击学生 个人答题情况页 特有元素
    @teststep
    def optimal_achievement(self):
        """最优成绩-"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_testbank_status")
        return ele

    @teststep
    def first_achievement(self):
        """首次成绩-"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_spend_time")
        return ele

    # 每个game 的答题详情页（点击奖杯icon 进入）
    @teststep
    def achievement_button(self):
        """最优成绩 & 首次成绩"""
        ele = self.driver \
            .find_elements_by_xpath("android.support.v7.app.ActionBar$Tab/following-sibling::android.widget.TextView")
        return ele

    # 编辑作业 页面
    @teststeps
    def wait_check_edit_page(self):
        """以“title:编辑作业”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'编辑作业')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def cancel_button(self):
        """取消 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_first")\
            .click()

    @teststep
    def confirm_button(self):
        """确定 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_second") \
            .click()

    # 删除tips 页面
    @teststeps
    def wait_check_tips_page(self):
        """以“title:删除作业”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'删除作业')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def answer_analysis_detail(self, content):
        """答题分析 详情页"""
        mode = self.game_type()  # 游戏类型
        name = self.game_name()  # 游戏name
        num = self.game_num()  # 游戏 小题数
        average = self.average_achievement()  # 全班首轮平均成绩

        if len(mode) > 5 and content[0] == '':
            content = []
            for j in range(len(mode) - 1):
                print(mode[j].text, num[j].text, name[j].text, average[j].text)

            content.append(name[-1].text)  # 最后一个game的name
            content.append(mode[-1].text)  # 最后一个game的type
            self.screen_swipe_up(0.5, 0.85, 0.1)
            self.answer_analysis_detail(content)

            return content
        else:
            mode = self.game_type()  # 游戏类型
            name = self.game_name()  # 游戏name
            num = self.game_num()  # 游戏 小题数
            average = self.average_achievement()  # 全班首轮平均成绩

            var = 0
            for k in range(len(mode)):
                if content[0] == name[k].text and content[1] == mode[k].text:
                    var += k
                    break

            for j in range(var, len(mode)):
                print(mode[j].text, num[j].text, name[j].text, average[j].text)
