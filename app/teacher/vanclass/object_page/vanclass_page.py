#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from pip.utils import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class VanclassPage(BasePage):
    """ 班级 页面"""

    @teststeps
    def wait_check_page(self):
        """以“title:班级”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'班级')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def empty_tips(self):
        """暂时没有数据"""
        try:
            self.driver\
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/load_empty")
            return True
        except Exception:
            return False

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        return ele

    @teststep
    def vanclass_name(self):
        """班级名称"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/class_name")
        return item

    @teststep
    def vanclass_no(self):
        """班号"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/class_no")
        return item

    @teststep
    def st_count(self):
        """学生人数"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/count")
        return item

    @teststep
    def add_class_button(self):
        """以“创建班级 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/add_class") \
            .click()

    # 班级 详情页
    @teststeps
    def wait_check_vanclass_page(self, var):
        """以“title: 班级名称”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % var)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def class_name(self):
        """班级名称"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/class_name") \
            .click()

    @teststep
    def class_name_modify(self):
        """班级名称 编辑"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/class_name_modify")
        return ele

    @teststep
    def school_name(self):
        """学校名称"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/school_name") \
            .click()

    @teststep
    def school_name_modify(self):
        """学校名称 编辑"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/school_name_modify")
        return ele

    @teststep
    def score_ranking(self):
        """积分排行榜"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/bill_board_integral") \
            .click()

    @teststep
    def star_ranking(self):
        """星星排行榜"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/bill_board_star") \
            .click()

    @teststep
    def vanclass_hw(self):
        """本班作业"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/homework") \
            .click()

    @teststep
    def vanclass_spoken(self):
        """本班口语"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/oral") \
            .click()

    @teststep
    def vanclass_paper(self):
        """本班卷子"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/paper") \
            .click()

    @teststep
    def vanclass_member(self):
        """班级成员"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/class_member") \
            .click()

    @teststep
    def vanclass_application(self):
        """入班申请"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/class_apply") \
            .click()

    @teststep
    def group_manage(self):
        """小组管理"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/group_member") \
            .click()

    @teststep
    def invite_st_button(self):
        """以“邀请学生 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/invite") \
            .click()

    # 邀请学生 提示页面
    @teststeps
    def wait_check_tips_page(self):
        """以“icon”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.vanthinkteacher.debug:id/md_title')]")
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def tips_title(self):
        """温馨提示title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_title").text
        print(item)
        return item

    @teststep
    def tips_content(self):
        """温馨提示 具体内容"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/invite_class_no").text
        print(item)
        return item

    @teststep
    def share_button(self):
        """分享按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultNeutral") \
            .click()

    @teststep
    def copy_link_button(self):
        """复制链接 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultNegative") \
            .click()

    @teststep
    def copy_no_button(self):
        """复制班号 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultPositive") \
            .click()

    # 分享界面
    @teststeps
    def wait_check_share_tips_page(self):
        """以“title”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'android:id/alertTitle')]")
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def share_title(self):
        """title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_title").text
        print(item)
        return item

    @teststep
    def share_content(self):
        """分享 """
        item = self.driver \
            .find_elements_by_id("android:id/text1")
        return item
