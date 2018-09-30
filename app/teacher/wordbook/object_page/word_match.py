import re
import time

from app.teacher.wordbook.object_page.Mysql_word import MysqlWord
from conf.basepage import BasePage
from conf.decorator import teststeps


class MatchingWord(BasePage):
    @teststeps
    def get_wordList(self):
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        return ele

    def iseg_word(self,word):
        pattern = re.findall(r'^[A-Za-z ]+$',word)
        if len(pattern)!= 0:
            return True
        else:
            return False


    @teststeps
    def card_match(self):
        english = []  # 单词list
        english_index  = []  # 单词在所有button中的索引
        explain = []  # 解释list
        explain_index = []  # 解释在所有button中的索引
        word_list = self.get_wordList()
        for i in range(1,len(word_list)):
            if self.iseg_word(word_list[i].text):  # 如果是字母
                english.append(word_list[i].text)
                english_index.append(i)
            else:  # 如果是汉字
                explain.append(word_list[i].text)
                explain_index.append(i)

        for j in range(len(explain)): # 具体操作
            word  = MysqlWord().get_word(explain[j])[0]
            word_list[explain_index[j]].click()
            time.sleep(1)
            for k in range(len(english)):
                if english[k] == word:
                    word_list[english_index[k]].click()
                    print("######################")
                    print("解释：", explain[j])
                    print("word：", word)
                    time.sleep(1)

        time.sleep(3)

