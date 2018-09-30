#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.decorator import teststep, teststeps
from conf.basepage import BasePage


class ThomePage(BasePage):
    """app主页面元素信息"""

    @teststeps
    def wait_check_page(self):
        """以“最新动态”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'最新动态')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def wait_check_no_page(self):
        """以“无 最新动态”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'(用户指南) 欢迎使用在线助教,打开看看吧!')]")
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def wait_check_image_page(self):
        """以“无 轮播图”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.vanthinkteacher.debug:id/scroll')]")
        try:
            WebDriverWait(self.driver, 3, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        # print('===========')
        # for i in range(len(ele)):
        #     print(ele[i].text)
        # print('==========')
        return ele

    @teststep
    def scroll_info(self):
        """顶部 滚动信息"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/scroll").text
        return item

    @teststep
    def item_detail(self):
        """首页 条目名称"""
        ele = self.driver.find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/detail")
        return ele

    @teststep
    def item_type(self, var):
        """首页 条目类型"""
        m = re.match(".*\((.*)\).*", var)  # title中第一个括号
        return m.group(1)

    @teststep
    def vanclass_name(self):
        """布置到的班级"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/class_name")
        return ele

    @teststep
    def create_time(self):
        """作业创建时间"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/create_time")
        return ele

    @teststep
    def draft_box_button(self):
        """以“草稿箱 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/draft") \
            .click()

    @teststep
    def assign_hw_button(self):
        """右下角“布置作业 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/add_hw") \
            .click()

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

    @teststep
    def back_up_button(self):
        """返回按钮"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststeps
    def text(self, index1):
        """元素：到底啦 下拉刷新试试"""
        try:
            item = self.driver \
                .find_elements_by_xpath("//android.widget.TextView[contains(@index,0)]")[index1 + 3]
            if item.text == '到底啦 下拉刷新试试':
                return True
            else:
                return False
        except Exception as e:  # 元素没有，会报错.如果元素存在则说明也不会发生
            print(e)
            pass

    # 公共元素- 底部四个tab元素：作业、题库、班级、个人中心
    @teststep
    def click_tab_hw(self):
        """以“作业tab”的text为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/tab_hw_tv')\
            .click()

    @teststep
    def click_tab_question(self):
        """以“题库tab”的text为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/tab_bank_tv') \
            .click()

    @teststep
    def click_test_vanclass(self):
        """以“班级tab”的text为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/tab_class_tv')\
            .click()

    @teststep
    def click_tab_profile(self):
        """以“个人中心tab”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.vanthinkteacher.debug:id/tab_profile_tv')\
            .click()

    # 草稿箱
    @teststeps
    def wait_check_drat_page(self):
        """以“title:草稿”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'草稿')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def empty_tips(self):
        """暂时没有数据"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/load_empty")
            return True
        except Exception:
            return False

    @teststep
    def draft_name(self):
        """草稿名称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/name")
        return ele

    @teststep
    def draft_time(self):
        """草稿创建时间"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/time")
        return ele

    @teststep
    def draft_count(self):
        """草稿 小题数"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/count")
        return ele

    @teststep
    def unread_point(self):
        """未读 小红点"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/unread_point")
        return ele

    @teststeps
    def get_type(self, var):
        """获取条目的类型：习题/试卷/口语"""
        name = self.item_detail()  # 条目title
        k = []
        for i in range(len(name)):
            item = self.item_type(name[i].text)
            if item == var:
                k.append(i)

        if len(k) == 0:
            self.screen_swipe_up(0.5, 0.85, 0.5, 1000)
            return self.get_type(var)
        else:
            return name, k

    @teststeps
    def hw_list_operate(self, item):
        """首页 - 作业列表"""
        name = self.item_detail()  # 作业name
        van = self.vanclass_name()  # 布置到的班级
        create = self.create_time()  # 作业创建时间

        content = []
        if len(item) == 0:  # 有作业  且 第一页
            print('---------------------------------')
            print('提示信息：', self.scroll_info())
            print('最新动态列表:')
            if len(create) == len(name) - 1:
                for i in range(len(create)):
                    print(name[i + 1].text, '\n',
                          van[i].text, '\n',
                          create[i].text)
                    print('------------------')
                    if i == len(create) - 1:
                        content.append(name[i + 1].text)
                        content.append(van[i].text)
                        content.append(create[i].text)
            else:
                for i in range(len(name)):
                    print(name[i].text, '\n',
                          van[i].text, '\n',
                          create[i].text)
                    print('------------------')
                    if i == len(name) - 1:
                        content.append(name[i].text)
                        content.append(van[i].text)
                        content.append(create[i].text)

            k = 0  # 用于跳出while循环的返回值
            return content, k
        else:  # 翻页以后
            if name[-1].text != item[0]:  # 翻页成功
                print('翻页：')
                var = []
                for i in range(len(name)):
                    if item[0] == name[i].text:
                        if item[1] == van[i].text:
                            if item[2] == create[i].text:
                                var.append(i + 1)
                                break
                if len(var) == 0:
                    var.append(0)

                if len(create) == len(name) - 1:
                    for j in range(var[0], len(create)):
                        print(name[j + 1].text, '\n',
                              van[j].text, '\n',
                              create[j].text)
                        print('------------------')
                        if j == len(create) - 1:
                            content.append(name[j + 1].text)
                            content.append(van[j].text)
                            content.append(create[j].text)
                else:
                    for j in range(var[0], len(name)):
                        print(name[j].text, '\n',
                              van[j].text, '\n',
                              create[j].text)
                        print('------------------')
                        if j == len(name) - 1:
                            content.append(name[j].text)
                            content.append(van[j].text)
                            content.append(create[j].text)

                k = 0
            else:
                k = 1
            return content, k
