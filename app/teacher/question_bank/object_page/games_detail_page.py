#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps
from utils.click_bounds import ClickBounds


class GamesPage(BasePage):
    """游戏 详情页面"""

    @teststeps
    def wait_check_page(self):
        """以“title:详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'详情')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def recommend_button(self):
        """推荐到学校 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/recommend") \
            .click()
        time.sleep(2)

    @teststep
    def collect_button(self):
        """收藏/取消收藏 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/collect") \
            .click()
        time.sleep(1)

    @teststep
    def put_to_basket_button(self):
        """加入题筐 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/add_pool") \
            .click()

    @teststep
    def game_title(self):
        """title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/title") \
            .text
        print(item)
        return item

    @teststep
    def game_info(self):
        """游戏 具体信息"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/info") \
            .text
        print(item)
        return item

    @teststep
    def teacher_nickname(self):
        """老师昵称"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/name") \
            .text
        print(item)
        return item

    @teststep
    def question_index(self):
        """题号"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/index")
        return item

    @teststep
    def verify_question_index(self):
        """验证 题号 是否存在"""
        try:
            self.driver.find_element_by_id("com.vanthink.vanthinkteacher.debug:id/index")
            return True
        except Exception:
            return False

    @teststep
    def word(self):
        """单词"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/word")
        return item

    @teststep
    def explain(self):
        """解释"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/explain")
        return item

    @teststep
    def sentence(self):
        """句子"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_answer")
        return item

    @teststep
    def hint(self):
        """句子- 解释"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_hint")
        return item

    @teststep
    def speak_button(self, index):
        """听力按钮"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_speak")[index] \
            .click()
        return item

    @teststep
    def verify_speak_button(self):
        """验证 听力按钮 是否存在"""
        try:
            self.driver.find_element_by_id("com.vanthink.vanthinkteacher.debug:id/iv_speak")
            return True
        except Exception:
            return False

    # 单选
    @teststep
    def single_question(self):
        """题目"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/question")
        return item

    @teststep
    def option_char(self):
        """选项 ABCD"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_char")
        return item

    @teststep
    def option_item(self):
        """选项 内容"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_item")
        return item

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        # for i in range(len(ele)):
        #     print(ele[i].text, len(ele[i].text))
        return ele

    @teststeps
    def option_button(self):
        """选项"""
        ele = self.driver \
            .find_elements_by_xpath(
                "//android.widget.TextView[contains(@resource-id,'com.vanthink.vanthinkteacher.debug:id/question')]"
                "/following-sibling::android.widget.LinearLayout/android.widget.LinearLayout"
                "/android.widget.LinearLayout/android.widget.TextView")

        item = []  # 当前页面中所有题目的选项
        var = []  # 所有题目的正确选项
        rate = []  # 百分数值
        count = []  # text为A的元素index

        for i in range(0, len(ele), 2):
            if ele[i].text == 'A':
                count.append(i)
        count.append(len(ele))  # 多余 只为最后一题

        for i in range(len(count)-1):
            options = []  # 每个题目的选项
            for j in range(count[i], count[i+1], 2):
                if j+1 == int(count[i+1]):  # todo BUG !!!
                    self.screen_swipe_up(0.5, 0.6, 0.59, 1000)  # 滑屏

                options.append(ele[j+1].text)
                if self.selected(ele[j]) == 'true':
                    rate.append(ele[j+1].text)
                    var.append(ele[j+1])
            item.append(options)
        return item, var, rate

    @teststeps
    def click_block(self):
        ClickBounds().click_bounds(540, 200)

    @teststep
    def verify_options(self):
        """验证 选项 ABCD 是否存在"""
        try:
            self.driver.find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_char")
            return True
        except Exception:
            return False

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

    @teststep
    def drop_down_button(self, var):
        """正确选项后答对率 下拉按钮"""
        loc = self.get_element_location(var)
        size = self.get_element_size(var)
        x = loc[0] + size[0]//2
        y = loc[1] + size[1]-10
        ClickBounds().click_bounds(x, y)

    @teststep
    def drop_down_content(self):
        """x% 下拉菜单 内容"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/content").text
        print('答题错误详情：', item)
        return item

    @teststeps
    def swipe_operate(self, item):
        ques_last_index = 0
        swipe_num = item
        for i in range(0, swipe_num):
            print('-----------------------------------')
            quesnum = self.single_question()
            ques_first_index = int(quesnum[0].text.split(".")[0])

            if ques_first_index - ques_last_index > 1:  # 判断页面是否滑过，若当前题比上一页做的题不大于1，则下拉直至题目等于上一题的加1
                for step in range(0, 10):
                    self.screen_swipe_down(0.5, 0.5, 0.62, 1000)
                    if int(self.single_question()[0].text.split(".")[0]) == ques_last_index + 1:  # 正好
                        quesnum = self.single_question()
                        break
                    elif int(self.single_question()[0].text.split(".")[0]) < ques_last_index + 1:  # 下拉拉过了
                        self.screen_swipe_up(0.5, 0.6, 0.27, 1000)  # 滑屏
                        if int(self.single_question()[0].text.split(".")[0]) == ques_last_index + 1:  # 正好
                            quesnum = self.single_question()
                            break
                    else:
                        print('再下拉一次:', int(self.single_question()[0].text.split(".")[0]), ques_last_index)

            tvs = self.all_element()
            last_one = tvs[len(tvs) - 1]

            if int(item) == ques_last_index:  # 最后一题
                print("--------滑到底啦---------")
                break
            else:
                if last_one.get_attribute("resourceId") == "com.vanthink.vanthinkteacher.debug:id/question":  # 判断最后一项是否为题目
                    for j in range(0, len(quesnum) - 1):
                        print('-----------------------------')
                        print(quesnum[j].text)
                        self.drop_down(j)  # 选项内容及下拉按钮是否可点击
                        ques_last_index = int(quesnum[len(quesnum) - 2].text.split(".")[0])
                else:  # 判断最后一题是否为选项
                    for k in range(0, len(quesnum)):
                        print('-----------------------------')
                        if k < len(quesnum) - 1:  # 前面的题目照常点击
                            print(quesnum[k].text)
                            self.drop_down(k)  # 选项内容及下拉按钮是否可点击
                        elif k == len(quesnum) - 1:  # 最后一个题目上滑一部分再进行选择
                            self.screen_swipe_up(0.5, 0.76, 0.60, 1000)
                            quesnum = self.single_question()
                            print(quesnum[-1].text)
                            self.drop_down(len(quesnum) - 1)  # 选项内容及下拉按钮是否可点击
                            ques_last_index = int(quesnum[len(quesnum) - 1].text.split(".")[0])

                if i != swipe_num - 1:
                    self.screen_swipe_up(0.5, 0.9, 0.27, 1000)  # 滑屏

    @teststeps
    def drop_down(self, k):
        """下拉按钮"""
        options = self.option_button()
        rate = re.sub("\D", "", options[2][k])
        print('该题所有选项:', options[0][k])

        if int(rate) < 100:
            self.drop_down_button(options[1][k])
            time.sleep(1)
            content = self.drop_down_content()
            self.click_block()

            item = self.rm_bracket(content)  # 去掉括号及其内的内容
            var = item.split('\n')  # 以'\n'分割字符串

            # z = re.compile(r'[(](.*?)[)]', re.S)
            # count = re.findall(z, content)
            # print(count)

            for i in range(0, len(var)-1, 2):  # len()-1是为了去掉最后一个换行符分割出的空元素
                if var[i] not in options[0][k]:
                    print('★★★ Error -下拉菜单内容不是本题选项', options[0][k], var[i])

        elif int(rate) == 100:
            print('该题正确率100%')
        else:
            print('★★★ Error -该题正确率', rate)

    @teststeps
    def rm_bracket(self, var):
        st = []
        ret = []
        for x in var:
            if x == '(':
                st.append(x)
            elif x == ')':
                st.pop()
            else:
                if len(st) == 0:
                    ret.append(x)  # 没有'('
        return ''.join(ret)
