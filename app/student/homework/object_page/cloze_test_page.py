#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import random
import re
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.result_page import ResultPage
from conf.decorator import teststeps, teststep
from conf.base_page import BasePage


class Cloze(BasePage):
    """完形填空"""
    @teststeps
    def wait_check_page(self):
        """以“title:完形填空”的xpath-index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'完形填空')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def rate(self):
        """获取作业数量"""
        rate = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/rate").text
        return rate

    @teststep
    def font_middle(self):
        """第一个Aa"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/font_middle")

        return ele

    @teststep
    def font_large(self):
        """第二个Aa"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/font_large")
        return ele

    @teststep
    def font_great(self):
        """第三个Aa"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/font_great")
        return ele

    @teststep
    def textview(self):
        """整个页面view -- 为了获取其content_desc属性 # .find_element_by_id("com.vanthink.student.debug:id/tb_content")"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView[contains(@index,1)]")[0]
        return ele

    @teststep
    def dragger(self):
        """拖动按钮"""
        num = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/dragger")
        return num

    @teststep
    def question_num(self):
        """题号"""
        num = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/question").text
        print(num)
        return num

    def swipe_duration(self):
        """获取元素大小"""
        num = self.driver.find_elements_by_xpath("//android.widget.ScrollView[contains(@index,2)]/child::android.widget.LinearLayout/android.widget.LinearLayout")
        ele_size = num.size
        print(ele_size)

    @teststep
    def option_button(self, var):
        """选项"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView[@text=  '%s']/following-sibling::android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView" % (str(var)+'.'))
        item = []
        for i in range(0, len(ele), 2):
            item.append(ele[i])
        print('选项个数:', len(item))
        return item

    @teststep
    def time(self):
        """获取作业时间"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/time").text
        return ele

    @teststeps
    def content_desc(self):
        """点击输入框，激活小键盘"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/cl_content")
        content = ele.get_attribute('contentDescription')
        item_x = re.match(".*\[(.*)\].*\[", content)  # x值
        item_y = re.match(".*\[(.*)\].*", content)  # y值
        x = item_x.group(1).split(',')  # 所有输入框y值的列表
        y = item_y.group(1).split(',')  # 所有输入框x值的列表
        size = ele.size
        return x, y, size

    @teststeps
    def get_result(self):
        """点击输入框，激活小键盘"""
        content = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/cl_content").get_attribute('contentDescription')
        value = re.match("\\[(.+?)\\]", content)  # answer
        answer = value.group(1).split(',')  # 所有输入框值的列表
        return answer

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        time.sleep(2)
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststeps
    def cloze_operate(self):
        """《完形填空》 游戏过程"""
        if self.wait_check_page():
            content = []
            timestr = []  # 获取每小题的时间
            rate = self.rate()
            self.font_operate()  # Aa文字大小切换按钮 切换 及状态统计

            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 判断加 点击操作

                if i == 4:
                    self.screen_swipe_up(0.5, 0.5, 0.25, 1000)
                self.question_num()  # 题号
                options = self.option_button(i+1)
                options[random.randint(0, len(options)) - 1].click()  # 随机点击选项
                self.screen_swipe_left(0.9, 0.9, 0.4, 1000)

                if i == int(rate)-1:  # 最后一小题：1、测试滑动页面是否可以进入结果页   2、拖拽 拖动按钮
                    if not ResultPage().wait_check_result_page(2):  # 结果页检查点
                        self.dragger()  # 拖拽 拖动按钮
                    else:
                        print('★★★ Error - 滑动页面进入了结果页')

                content.append(self.get_result()[i])  # 测试 是否答案已填入文章中
                if content[i] == ' ':
                    print('★★★ Error - 答案未填入文章中')
                else:
                    print('选择的答案:', content[i])

                timestr.append(self.time())  # 统计每小题的计时控件time信息
                print('================')

            Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            Homework().now_time(timestr)  # 判断游戏界面 计时功能控件 是否在计时

    @teststeps
    def font_operate(self):
        """Aa文字大小切换按钮 状态判断 及 切换操作"""
        x = []
        y = []
        middle = self.font_middle()  # first
        large = self.font_large()  # second
        great = self.font_great()  # third

        i = 0
        j = 0
        while i < 3:
            bounds = self.content_desc()  # 获取输入框坐标
            print(middle.get_attribute('checked'), large.get_attribute('checked'), great.get_attribute('checked'))

            if middle.get_attribute('checked') == 'false':
                if large.get_attribute('checked') == 'false':
                    x.insert(2, bounds[0][0])
                    y.insert(2, bounds[1][0])
                    print('当前选中的Aa按钮为第3个:', bounds[0][0], bounds[1][0])
                    j = 3
                else:
                    if large.get_attribute('checked') == 'true':
                        x.insert(1, bounds[0][0])
                        y.insert(1, bounds[1][0])
                        print('当前选中的Aa按钮为第2个:', bounds[0][0], bounds[1][0])
                        j = 2
            else:
                x.insert(0, bounds[0][0])
                y.insert(0, bounds[1][0])
                print('当前选中的Aa按钮为第1个:', bounds[0][0], bounds[1][0])
                j = 1

            if j == 1:
                large.click()
            elif j == 2:
                great.click()
            else:
                middle.click()
            i += 1
            print('--------------------------------------------')
            time.sleep(2)

        if not float(y[2]) > float(y[1]) > float(y[0]):
            print('★★★ Error - Aa文字大小切换按钮:', y)
        print('==============================================')
