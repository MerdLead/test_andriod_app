#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.student.homework.object_page.homework_page import Homework
from conf.decorator import teststeps, teststep
from conf.base_page import BasePage


class ReadCompre(BasePage):
    """阅读理解"""
    @teststeps
    def wait_check_page(self):
        """以“title:阅读理解”的xpath-index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'阅读理解')]")
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
    def dragger(self):
        """拖动按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/dragger")
        return ele

    @teststep
    def question_num(self):
        """题目内容"""
        num = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/question")
        return num

    def article_view_size(self):
        """获取整个文章页面大小"""
        num = self.driver.find_element_by_id("com.vanthink.student.debug:id/ss_view")
        var = num.size
        return var['height']

    @teststep
    def option_button(self, var):
        """选项"""
        print(var)
        ele = self.driver \
            .find_elements_by_xpath(
            "//android.widget.TextView[@text=  '%s']/following-sibling::android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"  % var)
        print(ele)
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

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        time.sleep(2)
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststeps
    def reading_operate(self):
        """《阅读理解》 游戏过程"""
        if self.wait_check_page():
            timestr = []  # 获取每小题的时间

            screen = self.get_window_size()[1]
            drag = self.dragger()  # 拖动按钮
            loc = self.get_element_location(drag)  # 获取按钮坐标
            self.driver.swipe(loc[0] + 45, loc[1] + 45, loc[0] + 45, loc[1] + 600)  # 拖拽按钮到最底部，以便测试Aa

            self.font_operate()  # Aa文字大小切换按钮 状态判断 及 切换操作

            loc = self.get_element_location(drag)  # 获取按钮坐标
            self.driver.swipe(loc[0] + 45, loc[1] + 45, loc[0] + 45, loc[1]-750)  # 向上拖拽

            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 状态判断 加点击

                self.screen_swipe_up(0.5, 0.3, 0.2, 1000)
                if i != 0 and i != int(rate)-1:
                    item = self.question_num()[1].text  # 下一道题目出现
                    while int(item[0]) < i+1:
                        self.screen_swipe_up(0.5, 0.9, 0.8, 1000)
                        ele = self.question_num()[1].text
                        index = int(ele[0])
                        print('题号:', index)
                    self.screen_swipe_up(0.5, 0.9, 0.65, 1000)

                content = self.question_num()  # 题目内容
                if i == int(rate)-1:
                    question = content[len(content)-1].text
                    self.screen_swipe_up(0.5, 0.9, 0.6, 1000)
                    options = self.option_button(question)
                    options[random.randint(0, len(options)) - 1].click()  # 随机点击选项
                else:
                    question = content[0].text
                    options = self.option_button(question)
                    options[random.randint(0, len(options)) - 1].click()  # 随机点击选项

                if i == int(rate) - 1:
                    self.dragger()
                    loca = self.get_element_location(drag)
                    self.driver.swipe(loca[0] + 45, loca[1] + 45, loca[0] + 45, (loca[1] + 450)/1280*screen)
                timestr.append(self.time())  # 统计每小题的计时控件time信息
                print('---------------------------')

            Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            Homework().now_time(timestr)  # 判断游戏界面 计时功能控件 是否在计时

    @teststeps
    def font_operate(self):
        """Aa文字大小切换按钮 状态判断 及 切换操作"""
        loc = []
        middle = self.font_middle()  # first
        large = self.font_large()  # second
        great = self.font_great()  # third

        i = 0
        j = 0
        while i < 3:
            y = self.article_view_size()  # 获取整个文章页面大小
            print(middle.get_attribute('checked'), large.get_attribute('checked'), great.get_attribute('checked'))
            if middle.get_attribute('checked') == 'false':
                if large.get_attribute('checked') == 'false':
                    print('当前选中的Aa按钮为第3个,页面高度:', y)
                    loc.insert(2, y)
                    j = 3
                else:
                    if large.get_attribute('checked') == 'true':
                        print('当前选中的Aa按钮为第2个,页面高度:', y)
                        loc.insert(1, y)
                        j = 2
            else:
                print('当前选中的Aa按钮为第1个,页面高度:', y)
                loc.insert(0, y)
                j = 1

            if j == 1:
                large.click()
            elif j == 2:
                great.click()
            else:
                middle.click()
            i += 1
            time.sleep(2)
            print('-----------------------------------------')

        if not float(loc[2]) > float(loc[1]) > float(loc[0]):
            print('★★★ Error - Aa文字大小切换按钮:', loc)
        print('=============================================')
