import random
import time
from math import ceil
from app.student.homework.object_page.home_page import HomePage
from app.student.word_book.object_page.data_action import DataActionPage
from utils.mysql_data import MysqlData
from app.student.word_book.object_page.word_book import WordBook
from conf.base_page import BasePage
from conf.decorator import teststeps, teststep


class MyWordPage(BasePage):
    """单词本 - 我的单词"""
    def __init__(self):
        self.home = HomePage()
        self.mysql = MysqlData()
        self.word = WordBook()
        self.common = DataActionPage()

    @teststeps
    def wait_check_mine_word_page(self):
        """以“我的单词”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'我的单词')]")
        try:
            WebDriverWait(self.driver, 3, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False


    @teststeps
    def no_word_tips(self):
        """wording:您还没有已背单词哦，快开始背单词吧"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.student.debug:id/status_error_hint_view")
            return True
        except Exception:
            return False

    @teststeps
    def no_word_tip_text(self):

        """wording:您还没有已背单词哦，快开始背单词吧"""
        ele = self.driver.find_element_by_id ('com.vanthink.student.debug:id/status_error_hint_view').text
        print(ele.text)

    @teststep
    def click_my_word_btn(self):
        """我的单词"""
        self.driver.\
            find_element_by_id('com.vanthink.student.debug:id/my_word')\
            .click()

    @teststep
    def total_word(self):
        """单词总数"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/total_word").text
        return ele

    @teststep
    def word_detail_text(self):
        """查看单词详情"""
        ele = self.driver\
            .find_element_by_xpath("//android.widget.TextView[contains(@text, '点单词可看详情')]").text
        print(ele)

    @teststep
    def voice_button(self):
        """听音 按钮"""
        ele = self.driver\
                  .find_elements_by_id("com.vanthink.student.debug:id/iv_speak")
        return ele

    @teststep
    def get_words(self):
        """单词"""
        ele = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/word")
        return ele

    @teststep
    def progress(self):
        """每个单词的轮次"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/progress")
        return ele

    @teststep
    def order_info(self):
        """排名"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_order")
        return ele

    @teststep
    def st_icon(self):
        """头像"""
        ele = self.driver\
            .find_elements_by_id("com.vanthink.student.debug:id/iv_head")
        return ele

    @teststep
    def st_name(self):
        """学生姓名"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_name")
        return ele

    @teststep
    def get_all_words(self,word):
        """将所有单词存储在一个数组中"""
        word_list = []
        for i in range(ceil(int(word)/13)):
            words = self.get_words()
            for j in range(len(words)):
                word_list.append (words[j].text)
            self.screen_swipe_up (0.5, 0.9, 0.1, 1000)
        self.screen_swipe_down (0.5, 0.1, 0.9, 1000)
        return word_list



    @teststep
    def play_mine_word(self, word):
        """我的单词 主要过程"""
        total_text = self.total_word ()
        if total_text.split (":")[1] != word:
            print ('★★★ Error--题目总数不正确！')
        else:
            print('\n----<我的单词页面>-----\n')
            print(total_text)
            self.word_detail_text()

            words_list= self.get_all_words(word) #获取所有单词
            all_words = list(set(words_list))    #滑屏后添加至新数组，去重
            all_words.sort(key=words_list.index) #保留原有顺序
            print('所有单词：',all_words)

            words = self.get_words ()
            words[random.randint (0, len (words)-1)].click () #随机点击一个单词
            self.word.play_word_book ()  # 我的单词练习过程

            time.sleep (3)
            self.home.back_to_home()



