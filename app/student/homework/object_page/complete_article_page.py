#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI
import re
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.student.homework.object_page.homework_page import Homework
from app.student.homework.object_page.result_page import ResultPage
from conf.decorator import teststeps, teststep
from conf.base_page import BasePage
from conf.base_config import GetVariable as gv
from utils.excel_read_write import ExcelUtil


class CompleteArticle(BasePage):
    """补全文章"""
    def __init__(self):
        self.result = ResultPage()

    @teststeps
    def wait_check_page(self):
        """以“title:补全文章”的xpath-index为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'补全文章')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def rate(self):
        """获取作业数量"""
        rate = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/rate").text
        return rate

    @teststep
    def font_middle(self):
        """第一个Aa"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/font_middle")

        return ele

    @teststep
    def font_large(self):
        """第二个Aa"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/font_large")
        return ele

    @teststep
    def font_great(self):
        """第三个Aa"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/font_great")
        return ele

    @teststep
    def dragger(self):
        """拖动按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/dragger")
        return ele

    @teststep
    def question_num(self):
        """题目内容"""
        num = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/question")
        return num

    @teststep
    def option_button(self, index):
        """选项ABCD"""
        ele = self.driver \
            .find_elements_by_id('com.vanthink.student.debug:id/tv_char')[index]
        return ele

    @teststep
    def option_content(self, index):
        """选项 内容"""
        ele = self.driver \
            .find_elements_by_id('com.vanthink.student.debug:id/tv_item')[index].text
        print('选项内容:', ele)
        return ele

    @teststep
    def time(self):
        """获取作业时间"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/time").text
        return ele

    @teststeps
    def content_desc(self):
        """点击输入框，激活小键盘"""
        content = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/ss_view").get_attribute('contentDescription')
        item_x = re.match(".*\[(.*)\].*\[", content)  # x值
        item_y = re.match(".*\[(.*)\].*", content)  # y值
        x = item_x.group(1).split(',')  # 所有输入框y值的列表
        y = item_y.group(1).split(',')  # 所有输入框x值的列表
        return x, y

    @teststeps
    def get_result(self):
        """点击输入框，激活小键盘"""
        content = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/ss_view").get_attribute('contentDescription')
        value = re.match("\\[(.+?)\\]", content)  # answer
        answer = value.group(1).split(',')  # 所有输入框值的列表
        return answer

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        time.sleep(1)
        self.driver \
            .find_element_by_class_name("android.widget.ImageButton") \
            .click()

    @teststeps
    def complete_article_operate(self):
        """《补全文章》 游戏过程"""
        if self.wait_check_page():
            content = []
            timestr = []  # 获取每小题的时间
            screen = self.get_window_size()[1]
            drag = self.dragger()

            self.font_operate()  # Aa文字大小切换按钮 切换 及状态统计

            rate = self.rate()
            for i in range(int(rate)):
                Homework().rate_judge(rate, i, self.rate())  # 测试当前rate值显示是否正确
                Homework().next_button_operate('false')  # 下一题 按钮 判断加 点击操作

                options = self.option_button(i)
                options.click()  # 依次点击选项

                if i == int(rate) - 1:
                    self.dragger()  # 拖拽 拖动按钮
                    loca = self.get_element_location(drag)
                    self.driver.swipe(loca[0] + 45, loca[1] + 45, loca[0] + 45, (loca[1] + 450)/1280*screen)

                content.append(self.get_result()[i])  # 测试 是否答案已填入文章中
                if content[i] == ' ':
                    print('★★★ Error - 答案未填入文章中')
                else:
                    print('第%s题:' % i)
                    print(options.text, content[i])
                timestr.append(self.time())  # 统计每小题的计时控件time信息
                print('-------------------------')

            Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            Homework().now_time(timestr)  # 判断游戏界面 计时功能控件 是否在计时
            print('============================================')
            return rate

    @teststeps
    def detail_page(self):
        """查看答案页面"""
        self.result.check_result_button()  # 结果页 查看答案 按钮
        if self.result.wait_check_detail_page():  # 页面检查点
            print('查看答案页面:')
            item = self.get_result()
            print("正确答案:", item)
            self.back_up_button()

    @teststeps
    def font_operate(self):
        """Aa文字大小切换按钮 状态判断 及 切换操作"""
        x = []
        y = []
        middle = self.font_middle()  # first
        large = self.font_large()  # second
        great = self.font_great()  # third

        i = 0
        j = 0
        while i < 3:
            bounds = self.content_desc()  # 获取输入框坐标
            print(middle.get_attribute('checked'), large.get_attribute('checked'), great.get_attribute('checked'))

            if middle.get_attribute('checked') == 'false':
                if large.get_attribute('checked') == 'false':
                    x.insert(2, bounds[0][0])
                    y.insert(2, bounds[1][0])
                    print('当前选中的Aa按钮为第3个:', bounds[0][0], bounds[1][0])
                    j = 3
                else:
                    if large.get_attribute('checked') == 'true':
                        x.insert(1, bounds[0][0])
                        y.insert(1, bounds[1][0])
                        print('当前选中的Aa按钮为第2个:', bounds[0][0], bounds[1][0])
                        j = 2
            else:
                x.insert(0, bounds[0][0])
                y.insert(0, bounds[1][0])
                print('当前选中的Aa按钮为第1个:', bounds[0][0], bounds[1][0])
                j = 1

            if j == 1:
                large.click()
            elif j == 2:
                great.click()
            else:
                middle.click()
            i += 1
            print('--------------------------------------------')
            time.sleep(2)

        if not float(y[2]) > float(y[1]) > float(y[0]):
            print('★★★ Error - Aa文字大小切换按钮:', y)
        print('==============================================')
