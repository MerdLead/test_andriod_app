#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class TuserCenterPage(BasePage):
    """个人中心"""

    @teststep
    def wait_check_page(self):
        """以“消息”业务的text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'消息')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_avatar_profile(self):
        """以“头像”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/name') \
            .click()

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        content = []
        for i in range(len(ele)):
            print(ele[i].text)
            content.append(ele[i].text)
        return ele, content

    @teststep
    def click_mine_collect(self):
        """以“我的收藏”的id为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/star')\
            .click()

    @teststep
    def click_mine_recommend(self):
        """以“我的推荐”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/recommend') \
            .click()

    @teststep
    def click_message(self):
        """以“消息”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/message') \
            .click()

    @teststep
    def click_setting(self):
        """以“设置”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/setting') \
            .click()


class QuestionFeedback(BasePage):
    """二级页面：问题反馈页面"""

    @teststep
    def wait_check_page(self):
        """以“title:问题反馈”的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'问题反馈')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def edit_text(self):
        """以“编辑框”的id为依据"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/et_feedback")
        return ele

    @teststep
    def submit_button(self):
        """以“提交按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/bt_submit") \
            .click()


class PrivacyPage(BasePage):
    """隐私条款"""
    @teststep
    def wait_check_page(self):
        """以“title:隐私条款”的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'隐私条款')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False


class ProtocolPage(BasePage):
    """注册协议"""
    @teststep
    def wait_check_page(self):
        """以“title:注册协议”的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'注册协议')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False
