#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.teacher.login.object_page.home_page import ThomePage
from app.teacher.login.object_page.login_page import TloginPage
from app.teacher.user_center.user_information.object_page.user_center_page import TuserCenterPage
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class SettingPage(BasePage):
    """设置页面"""
    @teststeps
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
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/help") \
            .click()

    @teststep
    def question_feedback(self):
        """以“问题反馈”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/feed")\
            .click()

    @teststep
    def privacy_clause(self):
        """以“隐私条款”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/right") \
            .click()

    @teststep
    def regist_protocol(self):
        """以“注册协议”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/protocol") \
            .click()

    @teststep
    def version_check(self):
        """以“版本号”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/version_check") \
            .click()

    @teststep
    def version(self):
        """以“版本号”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/version") \
            .click()

    @teststep
    def logout_button(self):
        """以“退出登录按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/logout") \
            .click()

    @teststep
    def back_up_button(self):
        """以“返回按钮”的id为依据"""
        self.driver\
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststep
    def logout(self):
        """退出登录"""
        self.driver.implicitly_wait(2)
        ThomePage().click_tab_profile()    # 进入首页后点击‘个人中心’按钮
        TuserCenterPage().click_setting()  # 点击设置按钮
        self.logout_button()

        self.driver.implicitly_wait(2)
        if TloginPage().wait_check_page():
            print('退出登录成功!!!')
        else:
            print(' 退出登录失败 ')
