#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.student.login.object_page.home_page import HomePage
from conf.base_page import BasePage
from conf.decorator import teststep, teststeps


class UserCenterPage(BasePage):
    @teststep
    def wait_check_page(self):
        """以“设置”业务的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'设置')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_avatar_profile(self):
        """以“头像”的id为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.student.debug:id/avatar_profile')\
            .click()

    @teststep
    def click_cards(self):
        """以“卡片”的id为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.student.debug:id/cards')\
            .click()

    @teststep
    def click_statistics(self):
        """以“统计”的id为依据"""
        self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/statistics") \
            .click()

    @teststep
    def click_message(self):
        """以“消息”的id为依据"""
        self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/message") \
            .click()

    @teststep
    def click_setting(self):
        """以“设置”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/setting") \
            .click()

    def back_up(self):
        """从个人信息页 返回主界面"""
        HomePage().click_tab_hw()


class MessageCenter(BasePage):
    """消息中心页面"""

    @teststep
    def wait_check_page(self):
        """以“title:消息中心”的xpath @text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'消息中心')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def iv_read_count(self):
        """以“未读消息数”的id为依据"""
        count = self.driver.find_elements_by_id("com.vanthink.student.debug:id/iv_read")
        return len(count)

    @teststep
    def message_count(self):
        """以“消息总数”的class_name为依据"""
        message = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
        return message

    @teststep
    def click_message(self):
        """以“消息”的class_name为依据"""
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout").click()

    @teststep
    def del_message(self, size, rollsize=1):
        """以“删除消息”的class_name为依据"""
        # # 设定系数
        # a = 554.0 / 1080
        # b = 1625.0 / 1794
        elements = self.message_count()
        print('len(elements):', len(elements))
        # for i in range(len(elements))

    @teststep
    def click_negative_button(self):
        """以“取消按钮”的id为依据"""
        self.driver.find_element_by_id('com.vanthink.student.debug:id/md_buttonDefaultNegative').click()

    @teststep
    def click_positive_button(self):
        """以“确认按钮”的id为依据"""
        self.driver.find_element_by_id('com.vanthink.student.debug:id/md_buttonDefaultPositive').click()

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class_name为依据"""
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()


class Setting(BasePage):
    """设置页面"""

    @teststep
    def wait_check_page(self):
        """以“title:设置”的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'设置')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def help_center(self):
        """以“帮助中心”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/help") \
            .click()

    @teststep
    def question_feedback(self):
        """以“问题反馈”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/feed")\
            .click()

    def privacy_clause(self):
        """以“隐私条款”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/right") \
            .click()

    @teststep
    def regist_protocol(self):
        """以“注册协议”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/protocol") \
            .click()

    @teststep
    def version_check(self):
        """以“版本检测”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/version_check") \
            .click()

    @teststep
    def logout_button(self):
        """以“退出登录按钮”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/logout") \
            .click()

    @teststeps
    def back_up(self):
        """从个人信息页 返回主界面"""
        if self.wait_check_page():
            HomePage().back_up_button()  # 返回按钮
            if UserCenterPage().wait_check_page():  # 页面检查点
                HomePage().click_tab_hw()

    @teststep
    def logout(self):
        """退出登录"""
        self.driver.implicitly_wait(2)
        HomePage().click_tab_profile()    # 进入首页后点击‘个人中心’按钮
        UserCenterPage().click_setting()  # 点击设置按钮
        self.logout_button()

        self.driver.implicitly_wait(2)
        if BasePage().wait_activity == "com.vanthink.vanthinkstudent.v2.ui.user.login.LoginActivity":
            print('退出登录成功!!!')
        else:
            print(' 退出登录失败 ')


class QuestionFeedback(BasePage):
    """二级页面：问题反馈页面"""

    @teststep
    def wait_check_page(self):
        """以“title:问题反馈”的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@index,1)]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def edit_text(self):
        """以“编辑框”的id为依据"""
        ele = self.driver.find_element_by_id("com.vanthink.student.debug:id/et_feedback")
        return ele

    @teststep
    def submit_button(self):
        """以“提交按钮”的id为依据"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/bt_submit") \
            .click()


class Privacy(BasePage):
    """隐私条款"""

    @teststep
    def wait_check_page(self):
        """以“title:隐私条款”的xpath @index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@index,1)]")
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

