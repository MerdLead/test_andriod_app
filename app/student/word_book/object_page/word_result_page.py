import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.student.homework.object_page.home_page import HomePage
from app.student.word_book.object_page.flash_card_page import FlashCard
from conf.base_page import BasePage
from conf.decorator import teststep, teststeps


class ResultPage(BasePage):

    def __init__(self):
        self.home = HomePage()

    @teststep
    def wait_check_result_page(self):
        """结果页 以今日已练单词图片的Id为依据"""
        locator = (By.ID,'com.vanthink.student.debug:id/word_count')
        try:
            WebDriverWait (self.driver, 3, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False

    @teststep
    def wait_check_show_page(self):
        """打卡页，以'炫耀一下'页面标题作为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'炫耀一下')]")
        try:
            WebDriverWait (self.driver, 3, 0.5).until (lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_check_next_grade(self):
        """再来一组 以继续挑战的图片的Id为依据"""
        locator = (By.ID, "com.vanthink.student.debug:id/img")
        try:
            WebDriverWait (self.driver, 3, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False


    @teststeps
    def get_result_all_ele(self):
        """结果页面"""
        print(' <结果页>：')
        word_count = self.driver.find_element_by_id("com.vanthink.student.debug:id/word_count").text
        print('今日已练单词：%s'%word_count)
        date = self.driver.find_element_by_id('com.vanthink.student.debug:id/date').text
        print('日期：%s'%date)
        all_word_count = self.driver.find_element_by_id("com.vanthink.student.debug:id/all_word_count").text
        print(all_word_count)
        remark_text = self.driver.find_element_by_id("com.vanthink.student.debug:id/text").text
        print(remark_text)
        print('----------------------------------------')

    @teststep
    def clock_button(self):
        """打卡"""
        self.driver.\
            find_element_by_id('com.vanthink.student.debug:id/punch_clock')\
            .click()
        time.sleep(2)

    @teststeps
    def show_page_ele(self):
        """炫耀一下页面"""
        print('<炫耀一下>：')
        print('功能按钮：')
        wx = self.driver.find_element_by_id("com.vanthink.student.debug:id/weixin").text
        wx_friend = self.driver.find_element_by_id('com.vanthink.student.debug:id/weixin_friends').text
        img_save = self.driver.find_element_by_id('com.vanthink.student.debug:id/save_img').text
        print(wx,wx_friend,img_save)
        print('-----------------------------------------')

    @teststep
    def rank_button(self):
        """右上角排名按钮"""
        self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/rank")\
            .click()
        time.sleep(3)

    @teststep
    def more_again_button(self):
        """再来一组"""
        self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/again")\
            .click()

    @teststep
    def level_up_text(self):
        """单词已练完说明"""
        ele = self.driver.find_element_by_id("com.vanthink.student.debug:id/level_up_hint").text
        print(ele)

    @teststep
    def no_study_btn(self):
        """不练了"""
        self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/cancel")\
            .click()

    @teststep
    def nex_level_text(self):
        ele = self.driver.find_element_by_xpath("//android.widget.TextView[@index,0]")
        print('已选年级 :%s'%ele)
        print('--------------------------------------')

    @teststep
    def continue_study_btn(self):
        """继续练习"""
        self.driver.\
            find_element_by_id("com.vanthink.student.debug:id/confirm")\
            .click()

    @teststeps
    def result_page_handle(self):
        # 结果页处理
        if self.wait_check_result_page ():
            print ('进入结果页面')
            self.get_result_all_ele ()  # 结果页元素
            self.clock_button ()  # 打卡
            self.show_page_ele ()  # 炫耀一下页面
            self.home.back_up_button ()  # 返回

            self.more_again_button ()  # 再练一次
            if self.wait_check_next_grade ():  # 继续挑战页面
                self.level_up_text()
            self.home.back_to_home()



