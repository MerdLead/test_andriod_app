import re
import time

from app.student.word_book.object_page.data_action import DataActionPage
from conf.base_page import BasePage
from conf.decorator import teststeps
from app.student.homework.object_page.homework_page import Homework

class MatchingWord(BasePage):
    def __init__(self):
        self.homework = Homework()
        self.common =DataActionPage()

    """连连看"""
    @teststeps
    def get_wordList(self):
        """获取页面内所有 word &解释"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        return ele

    @teststeps
    def is_word(self, word):
        """判断 是否为字母"""
        pattern = re.compile(r'^[A-Za-z. ]+$')
        if  pattern.match(word):
            return True
        else:
            return False

    @teststeps
    def card_match(self,ll):
        if ll == 0:
            print('\n单词连连看模式(新词) \n')

        english = []  # 单词list
        english_index = []  # 单词在所有button中的索引
        explain = []  # 解释list
        explain_index = []  # 解释在所有button中的索引

        word_list = self.get_wordList()  # 获取所有buton
        for i in range(1, len(word_list)):
            if self.is_word(word_list[i].text):  # 如果是字母
                english.append(word_list[i].text)
                english_index.append(i)
            else:  # 如果是汉字
                explain.append(word_list[i].text)
                explain_index.append(i)
        print("英文序列:%s"%english_index,"\n英文单词:%s"%english, "\n解释序列:%s"%explain, "\n英文解释:%s\n"%explain_index)

        for j in range(len(explain)):  # 具体操作
            word = self.common.get_word_by_explain(explain[j])
            word_list[explain_index[j]].click()
            print('解释：%s'%explain[j])
            for k in range(len(english)):
                if english[k] == word:
                    word_list[english_index[k]].click()
                    print("单词：%s"%word)
                    break
            print ('----------------------------------')
        time.sleep(5)
