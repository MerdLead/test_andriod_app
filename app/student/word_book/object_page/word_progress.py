from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.student.word_book.object_page.data_action import DataActionPage
from conf.base_page import BasePage
from conf.decorator import teststep


class ProgressPage(BasePage):
    def __init__(self):
        self.common = DataActionPage()

    @teststep
    def wait_check_progress_page(self):
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'单词本进度')]")
        try:
            WebDriverWait (self.driver, 5, 0.5).until (lambda x: x.find_element (*locator))
            return True
        except:
            return False

    @teststep
    def word_progress_icon(self):
        """词书进度"""
        self.driver.\
            find_element_by_id('com.vanthink.student.debug:id/word_statistics')\
            .click()

    @teststep
    def first_turn(self):
        """一轮"""
        ele = self.driver.find_element_by_id('com.vanthink.student.debug:id/first_time').text
        print(ele,end='，')

    @teststep
    def third_turn(self):
        """三轮"""
        ele = self.driver.find_element_by_id ('com.vanthink.student.debug:id/three_time').text
        print (ele,end='，')

    @teststep
    def total(self):
        """总数"""
        ele = self.driver.find_element_by_id ('com.vanthink.student.debug:id/total').text
        print (ele)

    @teststep
    def label_name(self):
        """标签名称"""
        ele = self.driver.find_elements_by_id('com.vanthink.student.debug:id/name')
        return ele

    @teststep
    def word_statistics(self):
        """单词数据"""
        ele = self.driver.find_elements_by_id("com.vanthink.student.debug:id/statistics")
        return ele

    @teststep
    def find_pencil_icon(self):
        try:
            self.driver.find_element_by_id('com.vanthink.student.debug:id/img')
            return True
        except:
            return False

    @teststep
    def progress_ele_check(self):
        """页面元素打印"""
        print("\n----<词书进度页面>----\n")

        self.first_turn ()  # 一轮
        self.third_turn ()  # 三轮
        self.total ()  # 总数

        labels = self.label_name()  #页面标签名
        statistics =self.word_statistics() #单词数据
        label_name = self.get_label_names() #数据库标签名称

        for i in range(len(labels)):
            print(labels[i].text,'\t',statistics[i].text)

            labels_id = self.common.get_all_label_ids ()    # 数据库标签id
            first_count = int (statistics[i].text.split ("/")[1]) #一轮单词数
            third_count = int (statistics[i].text.split ('/')[0]) #三轮单词数
            all_count = int (statistics[i].text.split ('/')[2].split (' ')[0]) #单词总数
            print ('一轮单词数:', first_count, ' 三轮单词数:', third_count, ' 单词总数:', all_count,'\n')

            if third_count != all_count:
                if self.find_pencil_icon():
                    print('正在练习标记存在,验证成功\n')
                else:
                    print('★★★ Error--未发现正在练习标记！')

            for j in range(len(label_name)):
                if label_name[j] == labels[i].text.split('-')[-1]:  #数据库标签名与页面标签名对比
                    self.count_compare(labels_id[j],first_count,third_count,all_count)

    @teststep
    def get_label_names(self):
        """获取标签名称"""
        labels_id = self.common.get_all_label_ids()
        label_names = []
        for i in labels_id:
            name = self.common.get_label_name(i)
            label_names.append(name)
        return  label_names

    @teststep
    def count_compare(self,label_id,first_count,third_count,total):
        """获取对应熟练度的单词数，并与页面数字比较"""
        count = self.common.get_words_count(label_id)  #返回单词id 与单词熟练度
        if count[0] == first_count:
            print('一轮单词数验证正确')
        else:
            print('★★★ Error-- 一轮单词数与数据库不匹配')

        if count[1] == third_count:
            print ('三轮单词数验证正确')
        else:
            print ('★★★ Error-- 三轮单词数与数据库不匹配')

        if count[2] == total:
            print ('单词总数数验证正确')
        else:
            print ('★★★ Error-- 单词总数与数据库不匹配')

        print ('----------------------------------')