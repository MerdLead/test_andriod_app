#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class QuestionBasketPage(BasePage):
    """题筐 页面"""

    @teststeps
    def wait_check_page(self):
        """以“title:题筐”的text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'题筐')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False
        
    @teststep
    def load_empty(self):
        """以“空白页”的id为依据"""
        try:
            self.driver \
                .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/load_empty')
            return True
        except Exception:
            return False

    @teststep
    def empty_text(self):
        """以“空白页”的id为依据"""
        ele = self.driver\
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/load_empty').text
        print(ele)
        print('=======================')

    @teststep
    def all_check_button(self):
        """以“全选按钮”的name为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/select_all") \
            .click()

    @teststep
    def check_button(self, index):
        """以“单选按钮”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/cb_add")[index]\
            .click()
        return ele

    @teststep
    def question_type(self, index):
        """以“类型”的id为依据"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/type")[index]. \
            text
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

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")

        count = []
        for i in range(2, len(ele)-2):
            if ele[i].get_attribute("resourceId") == "com.vanthink.vanthinkteacher.debug:id/type":
                count.append(i)
        count.append(len(ele)-2)  # 多余 为了最后一个

        for j in range(len(count)-1):
            for k in range(count[j], count[j+1]):
                print(ele[k].text)
            print('----------------')
        return len(count)-1

    @teststep
    def out_basket_button(self):
        """以“移出题筐 按钮”的name为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_first") \
            .click()

    @teststep
    def assign_button(self):
        """以“布置作业 按钮”的id为依据"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_second")
        return ele

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()
