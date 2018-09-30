#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.teacher.question_bank.test_data.games_name import games
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class QuestionDetailPage(BasePage):
    """题单详情 页面"""

    @teststeps
    def wait_check_page(self):
        """以“title:题单详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'题单详情')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def recommend_button(self):
        """推荐到学校 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/recommend") \
            .click()
        time.sleep(2)

    @teststep
    def collect_button(self):
        """收藏/取消收藏 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/collect") \
            .click()
        time.sleep(1)

    @teststep
    def put_to_basket_button(self):
        """加入题筐 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/add_pool") \
            .click()

    @teststep
    def all_check_button(self):
        """全选/全不选 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/all_check") \
            .click()

    @teststep
    def check_button(self):
        """单选 按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/cb_add")
        return ele

    @teststep
    def enabled(self, var):
        """元素 enabled属性值"""
        value = var.get_attribute('enabled')
        return value

    @teststep
    def checked(self, var):
        """元素 checked属性值"""
        value = var.get_attribute('checked')
        return value

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

    @teststeps
    def question_detail_operate(self):
        """题单详情页"""
        time.sleep(1)
        content = self.all_element()

        count = []
        for i in range(3, len(content[1])):
            if content[1][i] in games:
                count.append(i)

        print('------------------------------------------')
        for j in range(len(count)):  # len(count)代表game数
            if j == len(count) - 1:
                if len(count) - 1 - count[-1] > 3:
                    print(content[1][count[-1]:])
            else:
                print(content[1][count[j]:count[j + 1]])
            print('------------------------------------------')
