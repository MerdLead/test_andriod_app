#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class GroupDetailPage(BasePage):
    """ 小组管理 详情页面"""

    @teststeps
    def wait_check_page(self, var):
        """以“title: ”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % var)
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
    def group_name(self):
        """小组title"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/group_name")
        return item

    @teststep
    def st_count(self):
        """学生 人数"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/count")
        return ele

    # 小组 详情页面
    @teststep
    def edit_button(self):
        """编辑 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/edit")\
            .click()

    @teststep
    def delete_button(self):
        """删除 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/delete") \
            .click()

    @teststep
    def cancel_button(self):
        """取消 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultNegative") \
            .click()

    @teststep
    def commit_button(self):
        """确定 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultPositive") \
            .click()

    @teststeps
    def wait_check_detail_page(self):
        """以“title: ”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,com.vanthink.vanthinkteacher.debug:id/add_group)]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False