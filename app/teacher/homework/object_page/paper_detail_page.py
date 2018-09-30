#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class PaperDetailPage(BasePage):
    """ 试卷详情 页面"""

    @teststeps
    def wait_check_page(self):
        """以“title: 答卷分析”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'答卷分析')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        content = []
        for i in range(len(ele)):
            # print(ele[i].text)
            content.append(ele[i].text)
        # print('++++++++++++++++')
        return ele, content

    # 本班试卷 -- 试卷list
    @teststep
    def hw_name(self):
        """作业name"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/name")
        return ele

    @teststep
    def progress(self):
        """完成进度 - 已完成x/x"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/progress")
        return ele

    @teststep
    def create_time(self):
        """作业创建时间"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_create_date")
        return ele

    @teststep
    def remind(self):
        """提醒 按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/remind")
        return ele

    # 单个试卷
    @teststep
    def analysis_finished_tab(self, index):
        """答卷分析 & 完成情况 index = 0/1"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView")[index]
        return ele

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

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

    # 答卷分析 tab
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
    def van_average_achievement(self):
        """全班平均得分x分; 总分x分"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_desc")
        return ele

    # 答卷分析tab -- 答题详情页 元素 见games_detail_page.py

    # 完成情况tab
    @teststep
    def st_icon(self):
        """学生 头像"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_icon")
        return ele

    @teststep
    def st_name(self):
        """学生 昵称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_name")
        return ele

    @teststep
    def st_score(self):
        """学生 完成与否"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_score")
        return ele

    # 完成情况tab -- 个人答题结果页
    @teststeps
    def wait_check_per_detail_page(self, var):
        """以“title:详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % var)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def paper_type(self):
        """ 类型"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_paper")
        return ele

    def paper_name(self):
        """ 名称"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_paper_name")
        return ele

    # 个人答题结果页 -- 题型list
    def game_title(self):
        """ 名称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_name")
        return ele

    def game_desc(self):
        """ 共x题 xx分"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_desc")
        return ele

    def game_score(self):
        """ 得分"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_score")
        return ele

    def first_report(self):
        """首次正答"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/first_report").text
        print(ele)

    # 编辑试卷 页面
    @teststeps
    def wait_check_edit_page(self):
        """以“title:编辑试卷”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'编辑试卷')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def cancel_button(self):
        """取消 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_first") \
            .click()

    @teststep
    def confirm_button(self):
        """确定 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_second") \
            .click()
