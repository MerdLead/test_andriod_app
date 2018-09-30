#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI
import re
import time
from math import ceil, floor

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from app.student.homework.object_page.homework_page import Homework
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from conf.base_page import BasePage
from conf.decorator import teststeps, teststep
from app.student.homework.object_page.result_page import ResultPage
import random

from utils.toast_find import Toast


class Listening(BasePage):

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
    def answer_page_check(self):
        """以“查看答案的ID为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'查看答案)]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def rate(self):
        """获取作业数量"""
        rate = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/rate").text
        return rate

    @teststeps
    def play_voice(self):
        """播放按钮"""
        horn = self.driver.find_element_by_id("com.vanthink.student.debug:id/fab_audio")
        return horn

    @teststeps
    def red_tips(self):
        """上方红色提示"""
        redtip = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_hint")
        return redtip


    @teststeps
    def option_button(self, var):
        """选项"""
        print(var)
        ele = self.driver \
            .find_elements_by_xpath(
            "//android.widget.TextView[@text=  '%s']/following-sibling::android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView" % var)
        item = []
        for i in range(0, len(ele),2):
            item.append(ele[i])
        print('选项个数:', len(item))
        return item

    @teststeps
    def time(self):
        """获取作业时间"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/time").text
        return ele

    @teststeps
    def questions_num(self):
        num = self.driver.find_elements_by_id("com.vanthink.student.debug:id/question")
        return num

    @teststeps
    def TextViews(self):
        tvs = self.driver.find_elements_by_xpath("//android.widget.TextView")
        return  tvs

    @teststeps
    def next_button_operate(self, var):
        """下一步按钮 判断 加 点击操作"""
        self.next_button_judge(var)  # 下一题 按钮 状态判断
        self.next_button()  # 点击 下一题 按钮

    @teststeps
    def next_button_judge(self,var):
        item = self.driver.find_element_by_id("com.vanthink.student.debug:id/fab_submit").get_attribute("enabled")  # ‘下一题’按钮
        if item != var:  # 测试 下一步 按钮 状态
            print('★★★ 下一步按钮 状态Error', item)

    @teststeps
    def next_button(self):
        """‘下一题’按钮"""
        time.sleep(1)
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/fab_submit") \
            .click()

    @teststeps
    def imageButton(self):
        imageBt = self.driver.find_elements_by_xpath("//android.widget.ImageButton")
        return imageBt

    @teststeps
    def answer_check_button(self):
        self.driver.find_element_by_id("com.vanthink.student.debug:id/detail").click()

    @teststeps
    def answer_voice_play(self):
        self.driver.find_element_by_id("com.vanthink.student.debug:id/iv_play").click()

    @teststeps
    def play_again_button(self):
        self.driver.find_element_by_id("com.vanthink.student.debug:id/again").click()
        self.listen_choice()

    @teststeps
    def page_source(self):
        """以“获取page_source”的TEXT为依据"""
        print('打开：', self.driver.page_source)

    @teststeps
    def listen_choice(self):
        if self.wait_check_page():  #页面检查
            horn = self.play_voice()
            if horn.get_attribute("enabled"): #播放按钮检查
                retip = self.red_tips()
                if retip:   #检查是否有红色提示
                    horn.click()
                    result_dict = {}
                    timestr = []  # 获取每小题的时间
                    tipsum = int(self.rate()) #获取待完成数
                    print("作业个数：",tipsum)

                    swipe_num = int(ceil(tipsum / 3))  # 获取翻页次数
                    print("需要翻页的次数", swipe_num)

                    ques_last_index = 0
                    for i in range(0,swipe_num) :
                        quesnum = self.questions_num()
                        print("上一页面的最后一题题号为：",ques_last_index)
                        ques_first_index = int(quesnum[0].text.split(".")[0])
                        print("当前页第一题题号为：",ques_first_index)

                        if ques_first_index - ques_last_index >1: #判断页面是否滑过，若当前题比上一页做的题不大于1，则下拉直至题目等于上一题的加1
                            for step in range(0,10):
                                self.screen_swipe_down(0.5,0.5,0.62,1000)
                                if int(self.questions_num()[0].text.split(".")[0]) == ques_last_index+1:
                                    break
                                else:
                                    print("继续滑屏----")
                        rate = self.rate()
                        tvs = self.TextViews()
                        last_one = tvs[len(tvs) - 1]
                        quesnum = self.questions_num()

                        if ques_first_index - ques_last_index == 0:
                            print("--------滑到底啦---------")
                            for x in range(1,len(quesnum)):
                                self.click_options(rate, x, quesnum, timestr,result_dict)
                            break

                        if last_one.get_attribute("resourceId") == "com.vanthink.student.debug:id/question": #判断最后一项是否为题目
                            for j in range(0,len(quesnum)-1):
                                self.click_options(rate, j, quesnum, timestr,result_dict)
                                ques_last_index = int(quesnum[len(quesnum)-2].text.split(".")[0])

                        if last_one.get_attribute("resourceId") == "com.vanthink.student.debug:id/tv_item": #判断最后一题是否为选项
                            for k in range(0,len(quesnum)):
                                    if k < len(quesnum)-1:  #前面的题目照常点击
                                        self.click_options(rate,k,quesnum,timestr,result_dict)
                                    if k == len(quesnum)-1: #最后一个题目上滑一部分再进行选择
                                        self.screen_swipe_up(0.5,0.76,0.60,1000)
                                        time.sleep(2)
                                        self.click_options(rate, k, quesnum, timestr,result_dict)
                                        ques_last_index = int(quesnum[len(quesnum)-1].text.split(".")[0])
                                        break

                        if i == swipe_num -1:
                            break
                        self.screen_swipe_up(0.5,0.9,0.27,1000) #滑屏

                    print("所选答案为:",result_dict)
                    Homework().now_time(timestr)
                    self.next_click()
                    self.result_check(tipsum,result_dict)
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
    def click_options(self,rate,index,quesnum,timestr,result_dict):
        Homework().rate_judge(rate, index, self.rate())  # 测试当前rate值显示是否正确
        ques_index = int(quesnum[index].text.split(".")[0])
        options = self.option_button(quesnum[index].text)
        options[random.randint(0, len(options)) - 1].click()
        time.sleep(1)
        for i in range(0,len(options)):
            if options[i].get_attribute("selected") == "true":
                result_dict[ques_index] = options[i].text
        timestr.append(self.time())  # 统计每小题的计时控件time信息

    @teststeps
    def next_click(self):
        while True:   #因音频播放时间过长，且必须等待音频播放完毕后才会出现下一步按钮，所以对喇叭同一位置进行判断
            imageButton = self.imageButton()
            if imageButton[1].get_attribute("resourceId") == "com.vanthink.student.debug:id/fab_submit": #若为下一步的样式，则点击
                self.next_button_operate("true")
                time.sleep(3)
                break
            if imageButton[1].get_attribute("resourceId") == "com.vanthink.student.debug:id/fab_audio":  #若为喇叭样式，则继续等待
                time.sleep(1)

    @teststeps
    def result_check(self,tipsum,result_dict):
        self.answer_check_button()
        if ResultPage().wait_check_detail_page() :
            print("-----进入查看答案页面------")
            self.answer_voice_play()
            ex_last_index = 0
            while True:
                quesnum = self.questions_num()
                ques_index = int(quesnum[0].text.split(".")[0]) #获取页面第一题的题号
                ques_last_index = int(quesnum[len(quesnum)-1].text.split(".")[0]) #最后一题题号
                if ques_last_index != tipsum:
                    if ques_index - ex_last_index > 1 :
                        for step in range(0, 10):
                            self.screen_swipe_down(0.5, 0.5, 0.62, 1000)
                            if int(self.questions_num()[0].text.split(".")[0]) == ex_last_index + 1:
                                break
                    index = 0
                    self.result_compare(quesnum, index, result_dict)
                    ex_last_index = ques_index
                    self.screen_swipe_up(0.5, 0.84, 0.6, 1000)

                else:
                    self.screen_swipe_up(0.5,0.7,0.4,1000)
                    for i in range(0,len(quesnum)):
                        self.result_compare(quesnum, i, result_dict)
                    print("-------滑到底啦^_^-------")
                    break
            ResultPage().back_up_button()

    @teststeps
    def result_compare(self,quesnum,index,result_dict):
        selected_opt = []
        options = self.option_button(quesnum[index].text)
        tip_num = int(quesnum[index].text.split(".")[0])
        for j in range(0, len(options)):
            if options[j].get_attribute("selected") == "true":
                selected_opt.append(options[j].text)
        if len(selected_opt) == 1:
            if result_dict[tip_num] == selected_opt[0]:
                print("----所选答案与页面展示一致----")
            else:
                print("Error ★★★ 所选答案与页面展示不一致！！！")
        if len(selected_opt) == 2:
            for k in range(0, 2):
                if result_dict[tip_num] == selected_opt[k]:
                    continue
                else:
                    print("所选答案为",result_dict[tip_num],"正确答案为", selected_opt[k])
        if len(selected_opt) >= 3:
            print("Error ★★★ 出现多余选项！！！")