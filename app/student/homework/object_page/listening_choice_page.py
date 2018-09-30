#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI
import time
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from app.student.homework.object_page.homework_page import Homework
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.base_page import BasePage
from conf.decorator import teststeps, teststep
from utils.toast_find import Toast


class Listening(BasePage):
    """听力练习"""

    @teststeps
    def wait_check_page(self):
        """以“title:听力练习”的ID为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'听力练习')]")
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
    def play_voice(self):
        """播放按钮"""
        horn = self.driver.find_element_by_id("com.vanthink.student.debug:id/fab_audio")
        return horn

    @teststeps
    def red_tips(self):
        """上方红色提示"""
        try:
            self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_hint")
            return True
        except:
            return False

    @teststeps
    def option_button(self, var):
        """选项"""
        ele = self.driver \
            .find_elements_by_xpath(
                "//android.widget.TextView[contains(@text, '%s')]"
                "/following-sibling::android.widget.LinearLayout/android.widget.LinearLayout"
                "/android.widget.LinearLayout/android.widget.TextView" % var)
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
    def answer_selected(self):
        """定位选项，进行答题"""
        answer = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/tv_char")
        return answer

    @teststep
    def questions_num(self):
        """"""
        num = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/question")
        return num

    @teststep
    def text_views(self):
        """"""
        tvs = self.driver\
            .find_elements_by_xpath("//android.widget.TextView")
        return tvs

    @teststep
    def next_button(self):
        """‘下一题’按钮"""
        time.sleep(1)
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/fab_submit") \
            .click()

    @teststep
    def answer_check_button(self):
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/detail").click()

    @teststep
    def answer_voice_play(self):
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/iv_play").click()

    @teststep
    def play_again_button(self):
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/again").click()
        self.listen_choice()

    @teststeps
    def listen_choice(self):
        if self.wait_check_page():  # 页面检查
            horn = self.play_voice()
            if horn.get_attribute("enabled"):  # 播放按钮检查
                retip = self.red_tips()  # 顶部红色提示信息
                if retip:   # 检查是否有红色提示
                    timestr = []  # 获取每小题的时间

                    horn.click()  # 点击发音按钮
                    retip = self.red_tips()  # 顶部红色提示信息
                    if retip is False:  # 检查红色提示是否消失
                        tipsum = int(self.rate())  # 获取待完成数
                        print("作业个数：", tipsum)
                        swipe_num = int(round(tipsum/3))  # 获取翻页次数
                        print("需要翻页的次数", swipe_num)
                        self.swipe_operate(self.click_options, swipe_num, timestr)
                    print(timestr)
                    Homework().now_time(timestr)
                else:
                    print("----没有红色标识------")
            else:
                print("出现错误：喇叭不可点-------")
        else:
            try:
                Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            except Exception:
                print("未进入主界面")
                raise

    @teststeps
    def swipe_operate(self, func, swipe_num, timestr):
        for i in range(0, swipe_num):
            rate = self.rate()
            questions = self.questions_num()
            quesnum = len(questions) - 1
            print("当前页面所获取的题目数量：", quesnum)

            tvs = self.text_views()
            print("当前页共有：", len(tvs), "个textView")
            last_one = tvs[len(tvs) - 1]
            print("当前页最后一个TextView", last_one.text)
            print('-----------------------------')

            for j in range(0, quesnum):
                func(rate, j, questions, timestr)

            if i == swipe_num - 1:
                break
            else:
                if last_one.get_attribute("resourceId") == "com.vanthink.student.debug:id/tv_item":
                    self.screen_swipe_up(0.5, 0.87, 0.7, 1000)
                    func(rate, len(questions) - 1, questions, timestr)
                self.screen_swipe_up(0.5, 0.9, 0.2, 1000)
                time.sleep(1)

    @teststeps
    def click_options(self, rate, i, questions, timestr):
        Homework().rate_judge(rate, i)  # 测试当前rate值显示是否正确
        content = questions[i].text
        options = self.option_button(content)
        options[random.randint(0, len(options)) - 1].click()
        time.sleep(1)
        timestr.append(self.time())  # 统计每小题的计时控件time信息
        print('-----------------------------')

    # @teststeps
    # def check_result(self,timestr,answers,itr):
    #     self.next_button_operate('true')  # 下一题 按钮 状态判断 加点击
    #     Homework().now_time(timestr)  # 判断游戏界面 计时功能控件 是否在计时
    #     self.answer_check_button()  # 点击查看答案按钮
    #     if self.answer_page_check:
    #         print("进入查看答案界面-----")
    #         time.sleep(1)
    #         self.answer_voice_play() #点击上方音频播放按钮
    #         question_text = []
    #         self.screen_swipe_up(0.5, 0.97, 0.02, 1000)
