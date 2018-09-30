import random
import time

from app.student.homework.object_page.homework_page import Homework
from conf.basepage import BasePage
from conf.decorator import teststeps ,teststep


class VocabularyChoose(BasePage):
    @teststep
    def click_voice(self):
        """页面内音量按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/fab_sound") \
            .click()

    @teststep
    def question_content(self):
        """获取题目内容"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_head").text
        return ele

    @teststep
    def option_button(self):
        """获取四个选项"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView[contains(@resource-id,'com.vanthink.student.debug:id/option')]")
        return ele


    @teststeps
    def vocab_select_listen_choice(self,answer):
        print("--~--~--~--~--~--~--~--~--~")
        self.click_voice()
        option_list = self.option_button()     #获取当前页面所有选项

        if len(answer) == 0:                    #若answer为0，则说明上一选项为正确选项，随机选择
            option_list[random.randint(0,len(option_list)-1)].click()
            time.sleep(2)
            options = self.option_button()
            for i in range(0,len(options)):
                if options[i].get_attribute("selected") == "true":
                    if options[i].get_attribute("contentDescription") == "true":
                        print("选项正确,选项为",options[i].text)
                        break

                elif options[i].get_attribute("selected") == "false":
                    if options[i].get_attribute("contentDescription") == "true":
                        print("选择错误，正确选项为：",options[i].text)
                        answer.append(options[i].text)

        elif len(answer) == 1:  #若answer为其他，则说明上一选项为错误选项，这一次需定向选择
            for j in range(0,len(option_list)):
                if option_list[j].text == answer[0]:
                    option_list[j].click()
                    break
            print("已选择正确选项：",answer[0])
            del answer[:]
        time.sleep(3)
        Homework().next_button_operate("true")


