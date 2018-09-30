#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class FilterPage(BasePage):
    """ 筛选 页面"""

    @teststeps
    def wait_check_page(self):
        """以“title:资源类型”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'资源类型')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def question_menu(self):
        """以“题单”的text为依据"""
        ele = self.driver \
            .find_elements_by_xpath(
                "//android.widget.TextView[contains(@resource-id,"
                "'com.vanthink.vanthinkteacher.debug:id/tv_label_name')]")[2]
        return ele

    @teststep
    def click_question_menu(self):
        """以“题单”的text为依据"""
        self.driver \
            .find_elements_by_xpath(
                "//android.widget.TextView[contains(@resource-id,"
                "'com.vanthink.vanthinkteacher.debug:id/tv_label_name')]")[2] \
            .click()

    @teststep
    def game_list(self):
        """以“大题”的text为依据"""
        ele = self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'大题')]")
        return ele

    @teststep
    def click_game_list(self):
        """以“大题”的text为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'大题')]") \
            .click()

    @teststep
    def test_paper(self):
        """以“试卷”的text为依据"""
        ele = self.driver \
            .find_elements_by_xpath(
                "//android.widget.TextView[contains(@resource-id,"
                "'com.vanthink.vanthinkteacher.debug:id/tv_label_name')]")[4]
        return ele

    @teststep
    def click_test_paper(self):
        """以“试卷”的text为依据"""
        self.driver \
            .find_elements_by_xpath(
                "//android.widget.TextView[contains(@resource-id,"
                "'com.vanthink.vanthinkteacher.debug:id/tv_label_name')]")[4]\
            .click()

    @teststep
    def reset_button(self):
        """以“重置按钮”的text为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_first") \
            .click()

    @teststep
    def commit_button(self):
        """以“确定按钮”的text为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_second") \
            .click()

    @teststep
    def expand_button(self):
        """以“上下拉 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/iv_expand") \
            .click()

    @teststeps
    def label_title(self):
        """以“标签 title”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_title")
        content = []
        for i in range(len(ele)):
            content.append(ele[i].text)
        return content

    @teststep
    def label_name(self):
        """以“标签 name”的id为依据"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_label_name")
        # for i in range(len(ele)):
        #     print(ele[i].text)
        return ele

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        #
        # for i in range(len(ele)):
        #     print(ele[i].text)
        return ele

    # 资源类型
    @teststeps
    def filter_all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.all_element()
        count = []
        for i in range(len(ele)):
            if ele[i].text == '题库':
                count.append(i)
            elif ele[i].text == '资源类型':
                count.append(i)
            elif ele[i].text == '自定义标签':
                count.append(i)
            elif ele[i].text == '活动类型':
                count.append(i)
            elif ele[i].text == '系统标签':
                count.append(i)
                break

        count.append(len(ele)-2)
        return ele, count

    @teststeps
    def filter_content(self, ele, index):
        """筛选的所有label"""
        content = []
        for i in range(len(index)):
            if i + 1 == len(index):
                print('---------------------')
                for j in range(ele[1][i], len(ele[0]) - 7):
                    print(ele[0][j].text)
                    content.append(ele[0][j].text)
            else:
                print('---------------------')
                for j in range(ele[1][i], ele[1][i + 1]):
                    print(ele[0][j].text)
                    content.append(ele[0][j].text)

        return content

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

    @teststeps
    def source_type_selected(self, ele, index):
        """选中的资源类型"""
        if self.selected(self.question_menu()) == 'true':  # 题单
            print('题单:')
            var = self.filter_content(ele, index)
            self.label_judge(var, index, 3)
        else:
            if self.selected(self.game_list()) == 'true':  # 大题
                var = self.filter_content(ele, index)
                self.label_judge(var, index, 4)
            else:
                if self.selected(self.test_paper()) == 'true':  # 试卷
                    var = self.filter_content(ele, index)
                    self.label_judge(var, index, 2)

    @teststeps
    def label_judge(self, var, index, count):
        """有无 自定义标签时，判断不同资源类型标签数"""
        print('---------------------')
        if len(index) != count:  # 加1是为了 匹配参数值
            print('★★★ Error- 标签少了', var)
