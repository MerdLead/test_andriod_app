#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import re
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.result_page import ResultPage
from utils.games_keyboard import games_keyboard
from utils.click_bounds import ClickBounds
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class FlashCard(BasePage):
    """闪卡练习"""
    # 以下为 抄写模式和学习模式共有元素
    @teststeps
    def wait_check_page(self):
        """以“title:闪卡练习”的ID为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'闪卡练习')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_star(self):
        """闪卡练习页面内五角星按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/iv_star") \
            .click()

    @teststep
    def click_voice(self):
        """闪卡练习页面内音量按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/play_voice") \
            .click()

    @teststep
    def rate(self):
        """获取作业数量"""
        rate = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/rate").text
        return rate

    # 以下为学习模式 特有元素
    @teststep
    def english_study(self):
        """单页面内展示的Word"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_english").text
        return word

    @teststep
    def explain_study(self):
        """单页面内展示的翻译"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_chinese").text
        return word

    @teststep
    def click_rotate(self):
        """闪卡练习页面内翻转页面按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/iv_rotate").click()
        print('单双页面 切换:')

    @teststep
    def double_english_judge(self):
        """判断双页面内展示的word是否存在"""
        ele = self.find_element("com.vanthink.student.debug:id/tv_double_english")
        return ele

    @teststep
    def double_english(self):
        """双页面内展示的word"""
        word = self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/tv_double_english").text
        return word

    @teststep
    def double_explain_judge(self):
        """判断双页面内展示的explain是否存在"""
        ele = self.find_element("com.vanthink.student.debug:id/tv_double_explain")
        return ele

    @teststep
    def double_explain(self):
        """双页面内展示的explain"""
        word = self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/tv_double_explain").text
        return word

    @teststep
    def click_blank(self):
        """点击空白处"""
        ClickBounds().click_bounds(430, 800)
        print('点击空白处，切换双页面:')
        time.sleep(1)

    # 以下为抄写模式 特有元素
    @teststep
    def word_copy(self):
        """闪卡练习- 抄写模式 内展示的Word"""
        ele = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return ele

    @teststep
    def english_copy(self):
        """单页面内 答题框填入的Word"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/english").text
        return word

    @teststep
    def explain_copy(self):
        """闪卡练习内展示的翻译"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/chinese").text
        return word

    # 以下为闪卡练习 结果页
    @teststeps
    def wait_check_result_page(self):
        """以“title:答题报告”的ID为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'完成学习')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def finish_study(self):
        """完成学习"""
        ele = self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@index,0)]").text
        print(ele)
        return ele

    @teststep
    def study_sum(self):
        """eg: study_sum:6个内容,0标记★;抄写模式"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/study_sum").text
        print(ele)
        return ele

    @teststep
    def study_again_button(self):
        """再练一遍"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/textView") \
            .click()

    @teststep
    def star_again_button(self):
        """标星内容再练一遍"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_star_en") \
            .click()

    @teststep
    def star_button(self):
        """五星按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_select")
        return ele

    @teststep
    def voice_button(self, index):
        """语音按钮"""
        self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_voice")[index] \
            .click()

    @teststep
    def result_word(self):
        """展示的Word"""
        ele = self.driver.find_elements_by_id("com.vanthink.student.debug:id/tv_word")
        return ele

    @teststep
    def result_explain(self):
        """展示的  解释"""
        word = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_explain")
        return word

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        time.sleep(2)
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststeps
    def study_pattern(self):
        """《闪卡练习 学习模式》 游戏过程"""
        if self.wait_check_page():
            answer = []   # return值 与结果页内容比对
            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_judge('true')  # 下一题 按钮 状态判断

                self.voice_operate(i)  # 听力按钮

                if i in (1, 2):  # 第2、3题  进入为双页面
                    word = self.double_english()  # 单词
                    print('由双页面进入-- 单词:%s' % word)

                    answer.append(self.double_english())
                    if i == 2:
                        self.click_blank()  # 点击空白处，切换单词、解释页面
                        explain = self.double_explain()  # 解释
                        print('解释:%s' % explain)
                else:
                    word = self.english_study()  # 单词
                    explain = self.explain_study()  # 解释
                    print('单词:%s,解释:%s' % (word, explain))
                    answer.append(self.english_study())

                    self.click_rotate()  # 单双页面 切换
                    word = self.double_english()  # 单词
                    print('单词:%s' % word)

                    self.click_blank()  # 点击空白处，切换单词、解释页面
                    explain = self.double_explain()  # 解释
                    print('解释:%s' % explain)

                if i not in (0, 1):
                    self.click_rotate()  # 单双页面 切换

                if i in range(1, int(rate), 2):  # 点击star按钮
                    self.click_star()

                if i == 2 and i != int(rate) - 1:  # 第三题 滑屏进入下一题
                    self.screen_swipe_left(0.7, 0.5, 0.2, 1000)
                    time.sleep(1)
                else:
                    if i == int(rate) - 1:  # 最后一题 尝试滑屏进入结果页
                        self.screen_swipe_left(0.6, 0.5, 0.2, 1000)
                        if ResultPage().wait_check_result_page(2):
                            print('★★★ Error - 滑动页面进入了结果页')
                        else:
                            print('滑动页面未进入结果页')

                    Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
                print('--------------------------------')
            print('=========================================')
            return rate, answer

    @teststeps
    def copy_pattern(self):
        """《闪卡练习 抄写模式》 游戏过程"""
        if self.wait_check_page():  # 页面检查点
            answer = []  # return值 与结果页内容比对
            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                answer.append(self.word_copy())

                self.voice_operate(i)  # 听力按钮

                word = list(self.word_copy())  # 展示的Word -- 转化为list形式
                print("第%s题,单词是:%s" % (i, self.word_copy()))

                if len(self.english_copy()) == 0:  # 抄写模式 消除全部字母
                    for j in range(len(word)):
                        if j == 4:
                            games_keyboard('capslock')  # 点击键盘 切换到 大写字母
                            games_keyboard(word[j].upper())  # 点击键盘对应 大写字母
                        else:
                            if j == 5:
                                games_keyboard('capslock')  # 点击键盘 切换到 小写字母
                            games_keyboard(word[j].lower())  # 点击键盘对应字母

                if i in range(1, int(rate), 2):  # 点击star按钮
                    self.click_star()
                time.sleep(4)
                print('--------------------------------')
            print('=========================================')
            return rate, answer

    @teststeps
    def voice_operate(self, i):
        """听力按钮 操作"""
        if i == 2:  # 第3题
            j = 0
            print('多次点击发音按钮:')
            while j < 4:
                print(j)
                self.click_voice()  # 多次点击发音按钮
                j += 1
            time.sleep(1)
        else:
            self.click_voice()  # 点击 发音按钮

    @teststeps
    def result_page(self, i, answer):
        """结果页操作"""
        print('查看答案按钮：')
        print('判断是否滑动：', i)
        if int(i) < 9:
            self.result_operate(i, answer)
        else:
            self.result_operate(i, answer)
            self.screen_swipe_up(0.5, 0.75, 0.35, 1000)
            self.result_operate(i, answer)
            self.screen_swipe_down(0.5, 0.75, 0.35, 1000)
        print('=================================')

    @teststeps
    def result_operate(self, index, answer):
        """结果页 具体操作"""
        word = self.result_word()
        for i in range(len(word)):
            print(word[i].text, answer[i])
            if word[i].text != answer[i]:  # 结果页 展示的word与题目中是否一致
                print('★★★ Error 查看答案页 展示的word与题中不一致')

        for index in range(0, int(index), 3):  # 点击 结果页 听力按钮
            self.voice_button(index)  # 结果页 - 听力按钮
            self.star_button()[index].click()  # 结果页 star 按钮

        self.finish_study()  # 完成学习
        self.study_sum()  # 学习结果

    @teststeps
    def selected_sum(self):
        """标星的数目统计"""
        var = self.star_button()  # 结果页star按钮
        ele = []  # 结果页标星的作业数
        for i in range(len(var)):
            if var[i].get_attribute("selected") == 'true':
                ele.append(i)

        if len(ele) == 0:  # 结果页标星的作业数为0，则执行以下操作
            print('结果页标星的作业数为0, 点击star按钮:')
            for index in range(0, len(var), 2):
                self.star_button()[index].click()  # 结果页 star 按钮

            ele = []  # 结果页标星的作业数
            for i in range(len(var)):
                if var[i].get_attribute("selected") == 'true':
                    ele.append(i)

            self.study_sum()  # 学习情况
            print('----------------')

        print('star按钮数目：', len(var))
        print('标星数：', len(ele))
        print('========================')
        return len(ele)
