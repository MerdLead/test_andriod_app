#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.decorator import teststep, teststeps
from conf.basepage import BasePage


class PhoneReset(BasePage):
    """修改手机号页面所有控件信息"""

    @teststeps
    def wait_check_page(self):
        """以“title:修改手机号”的xpath @text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'修改手机号')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def et_phone(self):
        """以“手机号”的id为依据"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/et_phone")
        return ele

    @teststep
    def verify(self):
        """以“验证码”的id为依据"""

        ele = self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/verify_input")
        return ele

    @teststep
    def count_time(self):
        """以“获取验证码按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/count_time")\
            .click()

    @teststep
    def btn_certain(self):
        """以“确定按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/btn_certain")\
            .click()
