#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class StDetailPage(BasePage):
    """ 班级成员- 学生信息 详情页面"""
    @teststeps
    def wait_check_page(self):
        """以“title: 学生详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'学生详情')]")
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

    @teststep
    def st_name(self):
        """name"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/name")
        return ele.text

    @teststep
    def st_nickname(self):
        """nickname"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/nick_name")
        return ele.text

    @teststep
    def st_phone(self):
        """手机号"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/phone")
        return ele

    @teststep
    def st_tags(self):
        """提分"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/name")
        return ele.text

    @teststep
    def judge_st_tags(self):
        """判断元素 '提分' 存在与否"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tags")
            return True
        except:
            return False

    @teststep
    def data_statistic(self):
        """数据统计"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/count")\
            .click()

    @teststep
    def picture_count(self):
        """拼图 个数"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/puzzle_count")\
            .click()

    @teststep
    def hw_count(self):
        """作业个数"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/hw_count")\
            .click()

    # 数据统计
    @teststeps
    def wait_check_data_page(self):
        """以“title: 数据统计”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'数据统计')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def st_commit_button(self):
        """数据统计 - 该学生不存在"""
        self.driver \
            .find_element_by_id("android:id/button1") \
            .click()

    # 拼图/作业列表
    @teststeps
    def wait_check_picture_hw_page(self, var):
        """以“拼图/作业列表”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,%s)]" % var)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def picture_report(self):
        """拼图 报告"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_report")
        return ele.text

    @teststep
    def judge_picture(self):
        """判断拼图页面 - 图片存在"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/iv_puzzle")
            return True
        except:
            return False

    @teststep
    def picture_num(self):
        """拼图 数量 """
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_puzzle_num")
        return ele

    # 作业列表
    @teststeps
    def hw_title(self):
        """作业title"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_homework_name")
        return ele

    @teststeps
    def hw_finish(self):
        """作业 完成情况"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_finish_status")
        return ele

    # detail
    @teststeps
    def wait_check_detail_page(self):
        """以“title: 详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'详情')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def sentence(self):
        """句子"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/sentence")
        return ele

    @teststep
    def finish_ratio(self):
        """完成率"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/finish_ratio")
        return ele

    @teststep
    def spoken_speak(self):
        """播音按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_speak")
        return ele

    @teststep
    def all_pass_button(self):
        """全部过关 按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/all_pass")
        return ele

    @teststep
    def pass_button(self):
        """过关按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/is_pass")
        return ele

    @teststep
    def result_name(self):
        """结果"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/result_name")
        return ele

    @teststep
    def enabled(self, var):
        """元素 enabled属性值"""
        value = var.get_attribute('enabled')
        return value

    # 结果页
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

    # 题型list
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
