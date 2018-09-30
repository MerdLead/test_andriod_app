import random
import time

from app.student.homework.object_page.homework_page import Homework
from app.teacher.wordbook.object_page.Mysql_word import MysqlWord
from conf.basepage import BasePage
from conf.decorator import teststeps
from utils.click_bounds import ClickBounds
from utils.games_keyboard import games_keyboard


class Flash_card(BasePage):
    @teststeps
    def click_voice(self):
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/play_voice") \
            .click()

    @teststeps
    def double_page(self):
        """点击右上角的单字进入双页面"""
        self.driver.find_element_by_id("com.vanthink.student.debug:id/side").click()

    @teststeps
    def double_english(self):
        """双页面内展示的word"""
        word = self.driver. \
            find_element_by_id("com.vanthink.student.debug:id/tv_double_english").text
        return word

    @teststeps
    def double_explain(self):
        explain = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_double_explain").text
        return explain

    @teststeps
    def click_blank(self):
        """点击空白处"""
        ClickBounds().click_bounds(430, 800)
        print('点击空白处，切换双页面:')
        time.sleep(1)

    @teststeps
    def english_study(self):
        english = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_english").text
        return english

    @teststeps
    def explain_study(self):
        explain = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_chinese").text
        return explain

    @teststeps
    def click_star(self):
        """闪卡练习页面内五角星按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/iv_star") \
            .click()

    @teststeps
    def familiar_word(self):
        """设置为熟词"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/is_expert") \
            .click()

    @teststeps
    def word_copy(self):
        """闪卡练习- 抄写模式 内展示的Word"""
        ele = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return ele

    @teststeps
    def english_copy(self):
        """单页面内 答题框填入的Word"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/english").text
        return word

    @teststeps
    def copy_explain(self):
        ex = self.driver.find_element_by_id("com.vanthink.student.debug:id/chinese").text
        return ex

    @teststeps
    def study_word(self,i,word_dict):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
        self.click_voice()  # 听力按钮
        if i in (2, 5):  # 第2、3题  进入为双页面
            self.double_page()
            word = self.double_english()  # 单词
            print('由双页面进入-- 单词:%s' % word)
            self.click_blank()
            explain = self.double_explain()  # 解释
            print('解释:%s' % explain)
            MysqlWord().add_word(word,explain)
            word_dict[explain] = word
            self.double_page()
        else:
            word = self.english_study()  # 单词
            explain = self.explain_study()  # 解释
            word_dict[explain] = word
            MysqlWord().add_word(word,explain)
            print('单词:%s,解释:%s' % (word, explain))

        if i in range(0,random.randint(3,7),2):  # 点击star按钮
            self.click_star()

        if i in range(0, random.randint(2,5),2):  # 点击star按钮
            self.familiar_word()

        if i == 2 or i == 5:
            self.screen_swipe_left(0.7, 0.5, 0.2, 1000)
            time.sleep(1)
        else:
            Homework().next_button_operate('true')
            time.sleep(1)

    @teststeps
    def copy_word(self):
        print("============================")
        self.click_voice()  # 听力按钮
        time.sleep(1)
        word = list(self.word_copy())  # 展示的Word -- 转化为list形式
        print("单词是:%s" % (self.word_copy()),",解释是:%s" % (self.copy_explain()))
        if len(self.english_copy()) == 0:  # 抄写模式 消除全部字母
            for j in range(0,len(word)):
                if j == 4:
                    games_keyboard('capslock')  # 点击键盘 切换到 大写字母
                    games_keyboard(word[j].upper())  # 点击键盘对应 大写字母
                else:
                    if j == 5:
                        games_keyboard('capslock')  # 点击键盘 切换到 小写字母
                    games_keyboard(word[j].lower())  # 点击键盘对应字母
            time.sleep(3)


