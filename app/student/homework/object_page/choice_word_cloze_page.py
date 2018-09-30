#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
import re

from app.student.homework.object_page.homework_page import Homework
from utils.excel_read_write import ExcelUtil
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.student.homework.object_page.result_page import ResultPage
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from conf.base_config import GetVariable as gv
from utils.click_bounds import ClickBounds
from utils.games_keyboard import games_keyboard


class ChoiceWordCloze(BasePage):
    """选词填空"""
    def __init__(self):
        self.bounds = ClickBounds()
        self.result = ResultPage()

    @teststeps
    def wait_check_page(self):
        """以“title:选词填空”的xpath-index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'选词填空')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def rate(self):
        """获取作业数量"""
        rate = self.driver\
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
    def prompt(self):
        """提示词"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/prompt").click()

    @teststep
    def bounds_prompt(self):
        """提示词按钮"""
        ele = self.driver\
            .find_elements_by_xpath("//android.widget.TextView[contains(@index,0)]")[1]
        return ele

    @teststep
    def prompt_content(self):
        """提示词内容"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView[contains(@index,0)]")[1].text
        return ele

    @teststep
    def click_blank(self):
        """点击页面 提示词弹框 以外空白处，弹框消失"""
        self.bounds.click_bounds(67.5, 1119.5)

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
    def content_desc(self):
        """点击输入框，激活小键盘"""
        content = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tb_content").get_attribute('contentDescription')
        item_x = re.match(".*\[(.*)\].*\[", content)  # x值
        item_y = re.match(".*\[(.*)\].*", content)  # y值
        x = item_x.group(1).split(',')  # 所有输入框y值的列表
        print(x)
        y = item_y.group(1).split(',')  # 所有输入框x值的列表
        print(y)
        return x, y

    @teststeps
    def get_result(self):
        """点击输入框，激活小键盘"""
        content = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tb_content").get_attribute('contentDescription')
        value = re.match("\\[(.+?)\\]", content)  # answer
        print(value)
        answer = value.group(1).split(',')  # 所有输入框值的列表
        print('正确答案：', answer)
        return answer

    @teststep
    def click_enter_button(self):
        """点击回车键，激活下一题输入框"""
        self.bounds.click_bounds(660, 1240)

    @teststeps
    def choice_word_filling(self):
        """《选词填空》 游戏过程"""
        if self.wait_check_page():  # 页面检查点
            timestr = []
            self.prompt()  # 右上角 提示词
            content = self.prompt_content()  # 取出提示内容
            self.click_blank()  # 点击空白处 弹框消失
            word_list = content.split('   ')  # 取出单词列表
            print('待输入的单词:', word_list)

            self.font_operate()  # Aa文字大小切换按钮 切换 及状态统计

            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 状态判断 加点击

                if i == 0:
                    item = self.content_desc()
                    time.sleep(2)
                    x = float(item[0][i]) + 88.0
                    y = float(item[1][i]) + 246.0
                    self.bounds.click_bounds(x, y)
                else:
                    self.click_enter_button()

                word = word_list[i]
                print('word:', word)
                if len(word_list) >= int(rate):
                    for index in range(len(word)):
                        if index == 4:
                            games_keyboard('capslock')  # 点击键盘 切换到 大写字母
                            games_keyboard(word[index].upper())  # 点击键盘对应 大写字母
                            games_keyboard('capslock')  # 点击键盘 切换到 小写字母
                        else:
                            games_keyboard(word[index])  # 点击键盘对应字母
                else:
                    games_keyboard('abc')  # 点击键盘对应字母

                timestr.append(self.time())  # 统计每小题的计时控件time信息

            Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            Homework().now_time(timestr)  # 判断游戏界面 计时功能控件 是否在计时
            print('==================================================')
            return rate

    @teststeps
    def detail_page(self, rate, homework_title, game_title):
        """查看答案页面面"""
        self.result.check_result_button()  # 结果页 查看答案 按钮
        if self.result.wait_check_detail_page():  # 页面检查点
            print('查看答案页面:')
            item = self.get_result()
            print('excel-opeate:')
            for i in range(len(item)):
                print('----------------------')
                ExcelUtil().data_write(rate, homework_title, game_title, item[i])
            self.back_up_button()

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
                    print('当前选中的Aa按钮为第3个：', bounds[0][0], bounds[1][0])
                    j = 3
                else:
                    if large.get_attribute('checked') == 'true':
                        x.insert(1, bounds[0][0])
                        y.insert(1, bounds[1][0])
                        print('当前选中的Aa按钮为第2个：', bounds[0][0], bounds[1][0])
                        j = 2
            else:
                x.insert(0, bounds[0][0])
                y.insert(0, bounds[1][0])
                print('当前选中的Aa按钮为第1个：', bounds[0][0], bounds[1][0])
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
