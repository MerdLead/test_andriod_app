#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
import time
from app.student.homework.object_page.homework_page import Homework
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class HomePage(BasePage):
    """app主页面元素信息"""

    @teststeps
    def wait_check_word_title(self):
        """将'单词本?'作为 单词本首页 页面检查点"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'单词本')]")
        try:
            WebDriverWait (self.driver, 3, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False


    @teststep
    def wait_check_page(self):
        """以“试卷label”的class_name为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'做试卷')]")
        try:
            WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_check_head_img(self):
        """以个人中心头像的Id作为依据 """
        locator = (By.ID, "com.vanthink.student.debug:id/avatar")
        try:
            WebDriverWait (self.driver, 5, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False

    @teststep
    def wait_check_person_msg(self):
        """以个人信息的text作为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'个人信息')]")
        try:
            WebDriverWait (self.driver, 5, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False

    @teststeps
    def wait_check_tips_page(self):
        """以“icon”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.student.debug:id/md_title')]")
        try:
            WebDriverWait (self.driver, 2, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False

    @teststep
    def commit_button(self):
        """确定 按钮"""
        self.driver \
            .find_element_by_id ("com.vanthink.student.debug:id/md_buttonDefaultPositive") \
            .click ()
        time.sleep (2)

    @teststep
    def click_homework_label(self):
        """以做习题label 的resource id为依据"""
        self.driver.find_elements_by_id("com.vanthink.student.debug:id/type_img2")[2].click()

    @teststep
    def click_hk_tab(self,index):
        """以背单词label 的resource id为依据"""
        self.driver.find_elements_by_id("com.vanthink.student.debug:id/notice")[index].click()

    @teststep
    def back_up_button(self):
        self.driver.\
            find_element_by_accessibility_id('转到上一层级').click()

    @teststep
    def back_up(self):
        """以“返回按钮”的class name为依据"""
        time.sleep (1)
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()

    @teststep
    def homework(self):
        """以“作业或者试卷列表内条目”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_homework_name")
        return ele

    @teststep
    def finish_rate(self):
        """该作业包的完成度 """
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/roundProgressBar")
        return item

    @teststep
    def finish_num(self):
        """该作业包 已有X人完成 """
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_homework_desc").text
        return item

    @teststeps
    def text(self, index1):
        """元素：到底啦 下拉刷新试试"""
        try:
            item = self.driver \
                .find_element_by_xpath("//android.widget.TextView[contains(@index,0)]")
            if item.text == '到底啦 下拉刷新试试':
                return True
            else:
                return False
        except Exception as e:  # 元素没有，会报错.如果元素存在则说明也不会发生
            print(e)
            pass

    # 公共元素- 底部三个tab元素：作业、试卷、个人中心
    @teststep
    def click_testpaper_label(self):
        """以“试卷label”的class_name为依据"""
        self.driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")[1]\
            .click()

    @teststep
    def click_tab_hw(self):
        """以“作业tab”的id为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.student.debug:id/tab_hw')\
            .click()
        time.sleep(2)

    @teststep
    def click_tab_home(self):
        """底部学习按钮"""
        self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/tab_home")\
            .click()

    @teststep
    def click_test_class(self):
        """以“班级tab”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.student.debug:id/tab_class')\
            .click()

    @teststep
    def click_tab_profile(self):
        """以“个人中心tab”的id为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.student.debug:id/tab_profile')\
            .click()

    #个人中心 的元素
    @teststep
    def click_avatar_profile(self):
        """点击头像昵称 一栏"""
        self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/avatar_profile")\
            .click()

    @teststep
    def user_phone(self):
        """用户的手机号"""
        ele = self.driver.find_element_by_id("com.vanthink.student.debug:id/phone").text
        return ele


    @teststep
    def wait_activity(self):
        """获取当前页面activity"""
        self.driver.implicitly_wait(2)
        activity = self.driver.current_activity
        return activity

    @teststep
    def back_to_home(self):
        self.back_up_button ()
        if self.wait_check_tips_page():
            self.commit_button()
        if self.wait_check_word_title ():
            self.back_up_button ()
            if self.wait_check_page ():  # 页面检查点
                print ('返回主界面')

    @teststeps
    def homework_count(self):
        """获取作业title列表第一个页面的作业 """
        homework_title = []
        homework_list = self.homework()
        for i in range(0, len(homework_list)):
            homework_title.append(homework_list[i].text)  # 获取作业title列表
        return homework_title, homework_list

    @teststeps
    def homework_count_2(self):
        """获取作业title列表非第一页的作业 及 页面内最后一个作业的title 以及 元素 '到底啦 下拉刷新试试' """
        homework_title = []
        homework_list = self.homework()
        for i in range(0, len(homework_list)):
            homework_title.append(homework_list[i].text)  # 获取作业title列表
        print(len(homework_title), len(homework_list))
        item = homework_list[len(homework_list) - 1].text  # 最后一个作业的title
        tips = self.text(len(homework_title))  # 判断元素 '到底啦 下拉刷新试试' 是否存在
        print('tips:', tips)

        return tips, item, homework_title, homework_list

    @teststeps
    def swipe(self, var, homework, game):
        last_one = var[len(var) - 1]  # 滑动前页面内最后一个作业title
        BasePage().screen_swipe_up(0.5, 0.75, 0.25, 1000)

        item = self.homework_count_2()
        print("!!!!!!!!!!!!!",item[0])
        if item[0] is True:  # 滑到底部
            print('滑动后到底部')
            index = []
            for i in range(0, len(item[2])):
                if item[2][i] == last_one:
                    index.append(i)
                    break
            count = self.homework_exist(index[0] + 1, item[2], item[3], homework, game)
        else:
            print('滑动后未到底部')
            if last_one in item[2]:
                index_2 = []
                for j in range(0, len(item[2])):
                    if item[2][j] == last_one:
                        index_2.append(j)
                count = self.homework_exist(index_2[0] + 1, item[2], item[3], homework, game)
            else:
                count = self.homework_exist(0, item[2], item[3], homework, game)
            # self.swipe(item[2], homework, game)
        return count

    @teststeps
    def homework_exist(self, index, title, homework, item, game):
        homework_count = []
        result = []
        for ind in range(index, len(title)):
            if title[ind] == item:
                homework_count.append(ind)
        print('homework_count:', homework_count)
        if len(homework_count) != 0:
            for i in homework_count:
                homework[i].click()
                result.append(Homework().games_count(0, game)[0])
        else:
            print('no have该作业')
        return result
