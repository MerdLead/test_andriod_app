#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.teacher.question_bank.object_page.filter_page import FilterPage
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class RecommendPage(BasePage):
    """我的推荐 页面"""
    def __init__(self):
        self.filter = FilterPage()

    @teststeps
    def wait_check_page(self):
        """以“title:我的推荐”的text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'我的推荐')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def filter_button(self):
        """以“筛选 按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/filter") \
            .click()

    @teststep
    def more_button(self):
        """以“更多 按钮”的class name为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageView") \
            .click()

    @teststep
    def label_manage_button(self):
        """以“标签管理 按钮”的class name为依据"""
        self.driver \
            .find_elements_by_class_name("android.widget.ImageView") \
            .click()

    @teststep
    def the_end(self):
        """以“没有更多了”的text为依据"""
        item = self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'没有更多了')]") \
            .text
        return item

    @teststep
    def question_basket(self):
        """以 右下角“题筐 按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/fab_pool") \
            .click()

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststep
    def menu_button(self, index):
        """以 条目右侧“菜单按钮”的id为依据"""
        self.driver\
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_eg")[index] \
            .click()

    # 标签管理
    @teststeps
    def wait_check_manage_page(self):
        """以“title:老师测试版”的text为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,"
                   "'com.vanthink.vanthinkteacher.debug:id/fb_add_label')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    # 菜单 内容
    @teststep
    def put_to_basket(self):
        """以 菜单- 加入题筐 的text为依据"""
        self.driver\
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'加入题筐')]") \
            .click()

    @teststep
    def stick_label(self):
        """以 菜单- 贴标签 的text为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'贴标签')]") \
            .click()

    @teststep
    def recommend_to_school(self):
        """以 菜单- 推荐到学校 的text为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'推荐到学校')]") \
            .click()

    @teststep
    def cancel_collection(self):
        """以 菜单- 取消收藏 的text为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'取消收藏')]") \
            .click()

    # 贴标签
    @teststeps
    def wait_check_label_page(self):
        """以“title:贴标签”的text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'贴标签')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def save_button(self):
        """以 贴标签 - 保存按钮 的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/certain") \
            .click()

    @teststep
    def check_box(self, index):
        """以 贴标签 - 单选框 的id为依据"""
        self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/cb_checked")[index] \
            .click()

    @teststep
    def add_label(self):
        """以 贴标签 - 创建标签 的id为依据"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/fb_add_label") \
            .click()

    @teststeps
    def wait_check_tips_page(self):
        """以“icon”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.vanthinkteacher.debug:id/md_title')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def tips_title(self):
        """title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_title").text
        print(item)
        return item

    @teststep
    def input(self):
        """输入框"""
        ele = self.driver \
            .find_element_by_id("android:id/input")
        return ele

    @teststep
    def character_num(self):
        """字符数"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_minMax").text
        return ele

    @teststep
    def click_negative_button(self):
        """以“取消按钮”的id为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'取消')]") \
            .click()

    @teststep
    def click_positive_button(self):
        """以“确认按钮”的id为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'确定')]") \
            .click()

    @teststep
    def positive_button(self):
        """以“确认按钮”的id为依据"""
        ele = self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'确定')]")
        value = ele.get_property('value')
        return value['enabled']

    # 资源类型
    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        # for i in range(len(ele)):
        #     print(ele[i].text)
        return ele

    @teststeps
    def filter_all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.all_element()
        count = []
        for i in range(len(ele)):
            if ele[i].text == '资源类型':
                count.append(i)
            elif ele[i].text == '自定义标签':
                count.append(i)
            elif ele[i].text == '活动类型':
                count.append(i)
            elif ele[i].text == '系统标签':
                count.append(i)
                break

        return ele, count

    @teststeps
    def filter_content(self, ele, index):
        """筛选的所有label"""
        content = []
        for i in range(len(index)):
            if i + 1 == len(index):
                print('---------------------')
                for j in range(ele[1][i], len(ele[0]) - 2):
                    print(ele[0][j].text)
                    content.append(ele[0][j].text)
            else:
                print('---------------------')
                for j in range(ele[1][i], ele[1][i + 1]):
                    print(ele[0][j].text)
                    content.append(ele[0][j].text)
        return content

    @teststeps
    def source_type_selected(self, ele, index):
        """选中的资源类型"""
        if self.filter.selected(self.filter.question_menu()) == 'true':  # 题单
            print('题单:')
            var = self.filter_content(ele, index)
            self.label_judge(var, index, 3)
        else:
            if self.filter.selected(self.filter.game_list()) == 'true':  # 大题
                var = self.filter_content(ele, index)
                self.label_judge(var, index, 4)
            else:
                if self.filter.selected(self.filter.test_paper()) == 'true':  # 试卷
                    var = self.filter_content(ele, index)
                    self.label_judge(var, index, 2)

    @teststeps
    def label_judge(self, var, index, count):
        """有无 自定义标签时，判断不同资源类型标签数"""
        if '自定义标签' in var:
            if len(index) != count:
                print('★★★ Error- 标签少了', var)
        else:  # 没有自定义标签
            if len(index) + 1 != count:  # 加1是为了 匹配参数值
                print('★★★ Error- 标签少了', var)
