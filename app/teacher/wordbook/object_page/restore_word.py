import time

from app.student.homework.object_page.homework_page import Homework
from app.teacher.wordbook.object_page.Mysql_word import MysqlWord
from conf.basepage import BasePage
from conf.decorator import teststeps, teststep


class WordRestore(BasePage):
    @teststep
    def prompt(self):
        """展示的提示词"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_prompt").text
        return ele

    @teststep
    def click_voice(self):
        """页面内音量按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/fab_sound") \
            .click()

    @teststep
    def word(self):
        """展示的 待还原的单词"""
        word = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_word")
        return word

    @teststep
    def button_swipe(self, from_x, from_y, to_x, to_y, steps=1000):
        """拖动单词button"""
        self.driver.swipe(from_x, from_y, to_x, to_y, steps)

    @teststep
    def get_element_location(self, ele):
        """获取元素坐标"""
        x = ele.location['x']
        y = ele.location['y']

        return x, y

    @teststeps
    def drag_operate(self, word2, word):
        loc = self.get_element_location(word2)
        y2 = self.get_element_location(word)[1] - 40
        self.button_swipe(loc[0], loc[1], loc[0], y2, 1000)
        time.sleep(1)

    @teststeps
    def restore_word(self):
        print("*********************")
        self.click_voice()  # 听力按钮

        explain = self.prompt()  # 展示的提示词
        print("英文解释：",explain)
        english = MysqlWord().get_word(explain)[0]
        eng_word = ''
        alphas = self.word()
        for j in range(0,len(alphas)):
            eng_word = eng_word + alphas[j].text
        print("还原前单词为：",eng_word)

        for i in range(len(english)-1,-1,-1):    # 倒序
            words = self.word()
            for j in range(len(words)):
                letter = words[j].text
                if letter[0] == english[i] and j != 0:
                    self.drag_operate(words[j], words[0])  # 拖拽到第一个位置
                    break
        print("还原后单词为：", english)
        Homework().next_button_operate('true')  # 下一题 按钮 判断加 点击操作