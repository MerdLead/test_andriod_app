#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import random

import time

from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.result_page import ResultPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from conf.base_page import BasePage
from conf.decorator import teststep, teststeps


class VocabularyChoice(BasePage):
    """词汇选择"""
    def __init__(self):
        self.result = ResultPage()

    @teststeps
    def wait_check_page(self):
        """以“title:词汇选择”的xpath-index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'词汇选择')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_voice(self):
        """页面内音量按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/fab_sound") \
            .click()

    @teststep
    def rate(self):
        """获取作业数量"""
        rate = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/rate").text
        return rate

    @teststep
    def time(self):
        """获取作业时间"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/time").text
        return ele

    @teststep
    def question_content(self):
        """获取题目内容"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_head").text
        return ele

    @teststep
    def option_selected(self, index):
        """获取所有选项 - 四个选项selected属性"""
        time.sleep(1)
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/option")[index].get_attribute('selected')
        return ele

    @teststep
    def option_button(self):
        """获取四个选项"""
        ele = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/option")
        return ele

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        time.sleep(2)
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    # 听音选词模式 特有元素
    @teststep
    def voice(self):
        """点击喇叭,听音选词后的小喇叭"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/iv_speak")\
            .click()

    @teststep
    def tips(self):
        """tips:点击喇叭,听音选词"""
        word = self.driver \
            .find_elements_by_xpath("//android.widget.TextView[contains(@index,0)]")[0].text
        print('tips:', word)
        return word

    # 以下为答案详情页面元素
    @teststep
    def result_voice(self, index):
        """语音按钮"""
        self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_speak")[index] \
            .click()

    @teststep
    def result_answer(self, index):
        """单词"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_answer")[index].text
        return ele

    @teststep
    def result_explain(self, index):
        """解释"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_hint")[index].text
        return ele

    @teststep
    def result_mine(self, index):
        """我的"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_mine")[index].get_attribute("selected")
        return ele

    @teststeps
    def back_up(self):
        """返回"""
        j = 0
        while j < 2:
            self.back_up_button()  # 结果页 返回按钮
            j += 1

    @teststeps
    def diff_type(self, tpe):
        """选择 不同模式小游戏的 游戏方法"""
        print(tpe)
        if tpe == '选单词':
            result = self.vocab_select_choice_word()
            return result
        elif tpe == '选解释':
            result = self.vocab_select_choice_explain()
            return result
        elif tpe == '听音选词':  # 听音选词模式
            result = self.vocab_select_listen_choice()
            return result
            # print('听音选词模式')

    @teststeps
    def vocab_select_choice_explain(self):
        """《词汇选择》 - 选解释模式 游戏过程--普通单词一般做法，符合yb字体规范的特殊处理"""
        if self.wait_check_page():
            count = 0
            questions = []  # 答对的题
            timestr = []  # 获取每小题的时间
            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 判断加 点击操作

                self.click_voice()  # 点击发音按钮
                item = self.question_content()  # 题目
                print('题目:', item)

                options = self.option_button()
                options[random.randint(0, len(options)-1)].click()  # 随机点击选项
                # self.options_statistic(options, count, questions)  # 选择对错统计

                print('----------------------------------')
                timestr.append(self.time())  # 统计每小题的计时控件time信息
                Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            print('==============================================')
            return rate, count, questions

    @teststeps
    def vocab_select_choice_word(self):
        """《词汇选择》 - 选单词模式 游戏过程"""
        if self.wait_check_page():
            count = 0
            questions = []  # 答对的题
            timestr = []  # 获取每小题的时间
            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 判断加 点击操作

                item = self.question_content()  # 题目
                print('题目:', item)

                options = self.option_button()
                options[random.randint(0, len(options)-1)].click()  # 随机点击选项
                # self.options_statistic(options, count, questions)  # 选择对错统计

                print('----------------------------------')
                timestr.append(self.time())  # 统计每小题的计时控件time信息
                Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            print('==============================================')
            return rate, count, questions

    @teststeps
    def vocab_select_listen_choice(self):
        """《词汇选择》 - 听音选词模式 游戏过程"""
        if self.wait_check_page():
            count = 0
            questions = []  # 答对的题
            timestr = []  # 获取每小题的时间
            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 判断加 点击操作

                self.voice()   # 题目后的听力按钮
                self.click_voice()  # 发音按钮

                options = self.option_button()
                options[random.randint(0, len(options)-1)].click()  # 随机点击选项
                # self.options_statistic(options, count, questions)  # 选择对错统计

                # print('----------------------------------')
                timestr.append(self.time())  # 统计每小题的计时控件time信息
                Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            print('==============================================')
            return rate, count, questions

    @teststeps
    def options_statistic(self, options, count, questions):
        """选择对错统计"""
        ele = []  # 四个选项selected属性值为true的个数
        print(len(options))
        for j in range(len(options)):  # 统计答案正确与否
            if self.option_selected(j) == 'true':
                ele.append(j)

        if len(ele) == 1:  # 如果选项的selected属性为true的作业数为1,说明答对了，则+1
            count += 1
            print('回答正确:', options[ele[0]].text)
            questions.append(self.question_content())
        else:  # len(ele) == 2
            print('回答错误:', ele)

    @teststeps
    def result_detail_page(self, rate):
        """《词汇选择》 查看答案 操作过程"""
        if self.result.wait_check_result_page():  # 结果页检查点
            self.result.check_result_button()  # 结果页 查看答案 按钮
            if self.result.wait_check_detail_page():
                print('查看答案:')
                self.error_sum(rate)
                time.sleep(2)
            print('==============================================')

    @teststeps
    def error_sum(self, rate):
        """查看答案 - 点击答错的题 对应的 听力按钮"""
        print('题数:', int(rate))
        for i in range(0, int(rate)):
            print('解释:', self.result_explain(i))  # 解释
            print('单词:', self.result_answer(i))  # 正确word
            print('对错标识:', self.result_mine(i))  # 对错标识
            print('-----------------------------------')
            self.result_voice(i)  # 点击发音按钮
        self.back_up_button()  # 返回结果页

    @teststeps
    def study_again(self, tpe):
        """《词汇选择》 选解释&听音选词模式 操作过程"""
        if self.result.wait_check_result_page():  # 结果页检查点
            self.result.again_button()  # 结果页 错题再练 按钮
            print('错题再练:')
            self.diff_type(tpe)  # 不同模式 对应不同的游戏过程
