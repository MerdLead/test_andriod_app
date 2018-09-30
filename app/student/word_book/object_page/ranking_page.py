from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conf.base_page import BasePage
from conf.decorator import teststeps, teststep


class Ranking(BasePage):
    """单词本 - 排行榜"""

    @teststeps
    def wait_check_page(self):
        """以“炫耀一下”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'炫耀一下')]")
        try:
            WebDriverWait(self.driver, 2, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def vanclass_choose(self):
        """班级展示 及切换"""
        ele = self.driver \
            .find_elements_by_id("android:id/text1")
        return ele

    @teststep
    def word_num(self):
        """单词数"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/tv_score").text
        return ele

    @teststep
    def word_type(self):
        """wording:词"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/type").text
        return ele

    @teststep
    def rank_info(self):
        """第X名"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/tv_ranking").text
        print(ele)

    @teststep
    def share_button(self):
        """炫耀一下"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/flaunt_share") \
            .click()

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
    def st_score(self):
        """提示title"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_score")
        return item

    # 炫耀一下
    @teststeps
    def wait_check_share_page(self):
        """以“title: 炫耀一下”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'炫耀一下')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False