import time

from app.student.homework.object_page.homework_page import Homework
from app.student.word_book.object_page.data_action import DataActionPage
from conf.base_page import BasePage
from conf.decorator import teststeps, teststep


class WordRestore(BasePage):
    def __init__(self):
        self.common = DataActionPage()

    """还原单词"""
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
        """拖拽 操作"""
        loc = self.get_element_location(word2)
        y2 = self.get_element_location(word)[1] - 40
        self.button_swipe(loc[0], loc[1], loc[0], y2, 1000)
        time.sleep(1)

    @teststeps
    def get_mapping_word(self,english,attr):
        word = []
        english_index = []
        attr_index = []

        #获取和多字母的首字母相同的字母索引值
        index = 0
        for i in range (len (english)):
            for j in range (len (attr)):    #判断首字母连续的字母是否和卡片中多个字母是否一致，一致则存储第一个字母的索引
                if ''.join (english[i:i + len (attr[j])]) == attr[j]:
                    english_index.append (i)
                    attr_index.append (j)
                    index = index + 1
                    break
        print (english_index)

        #根据上面获得的索引值，将对应的字母变换为多个字母
        #再根据多个字母的长度，把占用后面的字母变为空
        for i in range (len (english)):
            for j in range (len (english_index)):
                if i == english_index[j]:
                    english[i] = attr[attr_index[j]]
                    for m in range (1, len (attr[attr_index[j]])):
                        english[i + m] = ''

        #将不为空的字母存入数组中，获取到和还原单词相同的字母个数
        for i in english:
            if i != '':
                word.append (i)
        print (word)
        return word

    @teststep
    def restore_word_core(self,english):
        """还原单词主要步骤"""
        index = 0
        for k in range (len(english)):  # 正序排列
            words = self.word ()
            for m in range (index, len(words)):  # 排过后不再进行
                letter = words[m].text
                if letter == english[k]:
                    if words[m] == words[index]:
                        index = index + 1
                        break
                    else:
                        self.drag_operate (words[m], words[index])
                        index = index + 1  # 每个位置还原后不再进行比对
                        break

    @teststeps
    def restore_word(self, i):
        if i == 0:
            print('\n还原单词模式(新词)\n')

        self.click_voice()  # 听力按钮
        Homework().next_button_operate ('false')

        explain = self.prompt()  # 展示的提示词
        english = self.common.get_word_by_explain(explain)
        print ("英文解释：%s"%explain)

        eng_word = ''
        dou_count = []
        alphas = self.word()

        for j in range (0, len(alphas)):
            if len(alphas[j].text) >=2:
               dou_count.append(alphas[j].text) #将多个单词的存在一个数组中
            eng_word = eng_word + alphas[j].text
        print ("还原前单词为：", eng_word)

        if len(dou_count) == 0:       #若还原前没有两个字母在一起
            self.restore_word_core(english)
        else:                        #若出现有两个字母在一起的字符串，先将正确的单词对应拆分，然后对比排序
            map_word = self.get_mapping_word(list(english),dou_count)
            self.restore_word_core(map_word)

        print('还原后单词为：%s'%english)
        print ('----------------------------------')

