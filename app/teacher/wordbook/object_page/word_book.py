import json
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.student.homework.object_page.homework_page import Homework
from app.teacher.wordbook.object_page.flash_card import Flash_card
from app.student.wordbook.object_page.restore_word import WordRestore
from app.student.wordbook.object_page.spelling_word import SpellingWord
from app.student.wordbook.object_page.vocabulary_choose import VocabularyChoose
from app.student.wordbook.object_page.word_match import MatchingWord
from conf.basepage import BasePage
from conf.decorator import teststeps,teststep


class Word_Book(BasePage):
    @teststeps
    def wait_check_page(self):  #将'已学单词总数'作为页面检查点
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'已学单词总数')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False
    @teststeps

    @teststeps    #使用xpath方法定位页面元素
    def button_check_by_xpath(self,string):
        try:
            self.driver.find_element_by_xpath(string)
            return True
        except:
            return False

    @teststeps  # 使用id方法定位页面元素
    def button_check_by_id(self, string):
        try:
            self.driver.find_element_by_id(string)
            return True
        except:
            return False

    @teststeps
    def word_strat_button(self):  #Go标志按钮
        self.driver.find_element_by_id("com.vanthink.student.debug:id/word_start").click()

    @teststeps
    def word_continue_button(self): #继续标志按钮
        self.driver.find_element_by_id("com.vanthink.student.debug:id/word_continue").click()

    @teststeps
    def grade_list(self):  #年级列表
        grades = self.driver.find_elements_by_id("com.vanthink.student.debug:id/tv_grade")
        return grades

    @teststeps
    def game_title(self):  #题型标题
        tv_title = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_title")
        return  tv_title

    @teststeps
    def store_data(self,word_dict):  # 将生词存入json文件在中
        with open("word.json",'w') as file:
            file.write(json.dumps(word_dict,ensure_ascii=False))

    @teststeps
    def load_data(self):
        with open("word.json",'r') as file: #单词默写和单词拼写时根据解释从json中获取对应的英文单词
            word_dict = json.loads(file.read())
            return word_dict

    @teststeps
    def result_text(self):   #结果页面新词和复习描述
        result = self.driver.find_element_by_id("com.vanthink.student.debug:id/text")
        return result

    @teststeps
    def get_word_count(self): #结果页已背单词描述
        count = self.driver.find_element_by_id('com.vanthink.student.debug:id/all_word_count')
        return  count

    @teststeps
    def click_card(self):
        self.driver.find_element_by_id("com.vanthink.student.debug:id/punch_clock").click()

    @teststeps
    def click_again(self):
        self.driver.find_element_by_id( "com.vanthink.student.debug:id/again").click()

    @teststeps
    def word_book_type(self):
        if self.button_check_by_xpath("//android.widget.TextView[contains(@text,'你准备好了吗?')]"):
            print("开始单词本练习")
            self.word_strat_button()
            time.sleep(1)
            #
            # 点击准备好后，有三种情况：
            # 1、未选择年级将跳转到年级选择页面
            # 2、进行新词游戏界面
            # 3、单词已练完的提示页面
            #
            if self.button_check_by_xpath("//android.widget.TextView[contains(@text,'请选择你所处年级')]"):
                print("选择年级")
                grades = self.grade_list()
                for i in range(0,len(grades)):
                    if grades[i].text == "三年级":
                        grades[i].click()
                        break
                print("年级为三年级")
                time.sleep(2)
                self.word_strat_button()
                time.sleep(2)
                self.play_word_book()
            elif self.button_check_by_id("com.vanthink.student.debug:id/status_error_hint_view"):
                print("单词已练完，暂不安排新词学习！！")
            else:
                time.sleep(2)
                self.play_word_book()

        elif self.button_check_by_xpath("//android.widget.TextView[contains(@text,'欢迎回来!继续上一次的练习吧?')]"):
            print("继续单词本练习")
            self.word_continue_button()
            time.sleep(2)
            self.play_word_book()

    @teststeps
    def play_word_book(self):
        i = 0
        answer = []
        word_dict = {}
        while True:
            if self.button_check_by_id("com.vanthink.student.debug:id/tv_title"):
                if self.game_title().text == "闪卡练习(新词)":
                    # """闪卡练习模式有三种情况：
                    # 1、点击star星标会进行闪卡抄写模式
                    # 2、点击熟词后会进入单词默写模式
                    # 3、什么都不点会进入下一游戏模式
                    # """
                    if self.button_check_by_xpath("//android.widget.TextView[contains(@text,'设置熟词')]"):
                        Flash_card().study_word(i, word_dict)
                        i = i+1
                    if self.button_check_by_id("com.vanthink.student.debug:id/keyboard"):
                        Flash_card().copy_word()

                elif self.game_title().text == "词汇选择(新词)":
                    VocabularyChoose().vocab_select_listen_choice(answer)

                elif self.game_title().text == "连连看(新词)":
                    time.sleep(1)
                    MatchingWord().card_match()

                elif self.game_title().text == "还原单词(新词)":
                    WordRestore().restore_word()

                elif self.game_title().text == "单词拼写(新词)":
                    SpellingWord().word_spell()
            else:
                break

        if self.button_check_by_xpath("//android.widget.TextView[contains(@text,'单词本')]"):
            print("----------进入结果页---------")
            result_text = self.result_text().text
            count_text = self.get_word_count().text
            result = re.findall(r'\d',result_text)
            count = re.findall(r'\d',count_text)
            if int(count[0]+count[1]) == int(result[1]+result[2]):
                print(result_text)
                print(count_text)
            else:
                print("错误！已背单词个数与新词个数不一致！！！")

            self.click_card()
            time.sleep(3)
            if self.button_check_by_id("com.vanthink.student.debug:id/share_img"):
                print("打卡成功")
            else:
                print("ERROR！未进入打卡页面")
            time.sleep(3)
            Homework().back_up_button()

        else:
            print("ERROR! 未进入结果页")

    @teststeps
    def play_again(self):

        time.sleep(3)
        self.click_again()
        print("再来一组")
        time.sleep(4)
        if self.button_check_by_id("com.vanthink.student.debug:id/status_error_hint_view"):
            print("单词已练完，暂不安排新词学习！！")
            Homework().back_up_button()
        else:
            self.play_word_book()







