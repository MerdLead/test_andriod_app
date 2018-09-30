from conf.base_page import BasePage
from conf.decorator import teststeps
from utils.games_keyboard import games_keyboard


class WordSpell(BasePage):
    @teststeps
    def word_explain(self):
        explain = self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_explain").text
        return explain

    @teststeps
    def spelling_paly(self,data):
        explain = self.word_explain()
        word = data[explain]

        for j in range(0,len(word)):
            if j == 4:
                games_keyboard('capslock')  # 点击键盘 切换到 大写字母
                games_keyboard(word[j].upper())  # 点击键盘对应 大写字母
            else:
                if j == 5:
                    games_keyboard('capslock')  # 点击键盘 切换到 小写字母
                games_keyboard(word[j].lower())  # 点击键盘对应字母