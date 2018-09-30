#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.base_page import BasePage
from conf.decorator import teststep, teststeps


class ReleasePage(BasePage):
    """ 发布作业 页面"""

    @teststeps
    def wait_check_release_page(self):
        """以“title:发布作业”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'发布作业')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def hw_title(self):
        """作业名称"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/hw_title").text
        return item

    @teststep
    def hw_name_edit(self):
        """作业名称 编辑框"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/hw_name")
        return item

    @teststep
    def hw_mode_title(self):
        """题目列表"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/hw_mode_title").text
        print(item)
        return item

    @teststep
    def adjust_order_button(self):
        """调整题目顺序"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/bank") \
            .click()

    @teststep
    def hw_mode_free(self):
        """作业模式 - 自由模式"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/free")
        return item

    @teststep
    def hw_mode_reach(self):
        """作业模式 - 达标模式"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/reach")
        return item

    @teststep
    def mode_checked(self, ele):
        """作业模式 - checked属性"""
        value = ele.get_attribute('checked')
        return value

    @teststep
    def choose_button(self):
        """班级 单选框"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/choose")
        return ele

    @teststep
    def van_name(self):
        """班级 名称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/class_name")
        return ele

    @teststep
    def choose_count(self):
        """班级 描述"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/choose_count")
        return ele

    @teststep
    def put_into_button(self):
        """存入草稿 按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_first")
        return ele

    @teststep
    def now_assign_button(self):
        """立即布置 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/action_second") \
            .click()

    @teststep
    def enabled(self, var):
        """元素 enabled属性值"""
        value = var.get_attribute('enabled')
        return value

    # 班级页面 学生list
    @teststep
    def st_title(self):
        """学生title"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/title")
        return item

    @teststep
    def st_phone(self):
        """学生title"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/sub_title")
        return item

    # 调整题目顺序
    @teststeps
    def wait_check_adjust_page(self):
        """以“title:题目列表”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'题目列表')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def confirm_button(self):
        """确定按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/confirm") \
            .click()

    @teststep
    def game_type(self):
        """游戏类型"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/type")
        return ele

    @teststep
    def game_name(self):
        """游戏 名称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/test_bank_name")
        return ele

    @teststep
    def drag_icon(self, index):
        """拖拽 icon"""
        self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_drag_icon")[index]\
            .click()

    # 班级 学生列表
    @teststeps
    def wait_check_class_page(self, var):
        """以“title:班级名称”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % var)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    # 温馨提示 页面
    @teststeps
    def wait_check_tips_page(self):
        """以“icon”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.vanthinkteacher.debug:id/md_title')]")
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def tips_title(self):
        """温馨提示title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_title").text
        print(item)
        return item

    @teststep
    def tips_content(self):
        """温馨提示 具体内容"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_content").text
        print(item)
        return item

    @teststep
    def never_notify(self):
        """不再提醒"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_promptCheckbox") \
            .click()

    @teststep
    def cancel_button(self):
        """取消 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultNegative") \
            .click()

    @teststep
    def commit_button(self):
        """确定 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/md_buttonDefaultPositive") \
            .click()

    @teststeps
    def tips_operate(self):
        """温馨提示 页面信息  -- 无 不再提醒 元素"""
        if self.wait_check_tips_page():  # 温馨提示 页面
            self.tips_title()
            self.tips_content()
            self.commit_button()  # 确定按钮

    @teststeps
    def tips_page_info(self):
        """温馨提示 页面信息  -- 有 不再提醒 元素"""
        if self.wait_check_tips_page():
            print('------------------------------------------', '\n',
                  '温馨提示 页面:')
            self.tips_title()
            self.tips_content()
            self.never_notify()  # 不再提醒
            self.cancel_button()  # 取消按钮

            self.now_assign_button()  # 立即布置 按钮
            time.sleep(1)
            self.commit_button()  # 确定按钮

    @teststeps
    def hw_mode_operate(self, ele):
        """发布作业 - 作业模式"""
        self.hw_mode_title()  # 作业模式

        free = self.hw_mode_free()  # 自由模式
        reach = self.hw_mode_reach()  # 达标模式
        print('  ', free.text, reach.text, ele[5].text)
        if self.mode_checked(free) is False:
            print('★★★ Error- 默认选择的作业模式有误')
        else:
            reach.click()  # 选择达标模式
            if self.mode_checked(reach) is False:
                print('★★★ Error- 作业模式 checked属性有误')
        print('-------------------------')

        return free, reach

    @teststeps
    def hw_adjust_order(self):
        """发布作业 - 调整题目顺序"""
        self.adjust_order_button()  # 调整题目顺序 按钮
        if self.wait_check_adjust_page():  # 页面检查点
            if self.wait_check_tips_page():  # 提示框
                self.tips_title()
                self.tips_content()
                self.commit_button()  # 确定按钮

            mode = self.game_type()
            name = self.game_name()
            print('----------------------------')
            print('题目顺序:')

            if len(mode) > 5:
                for i in range(len(mode)-1):
                    print(mode[i].text, name[i].text)
            else:
                for i in range(len(mode)):
                    print(mode[i].text, name[i].text)

            if len(mode) > 5:
                self.screen_swipe_up(0.5, 0.75, 0.3, 3)
                self.screen_swipe_down(0.5, 0.45, 0.7, 3)

                self.judge_hw_adjust(mode, name)
            if len(mode) == 3:
                self.screen_swipe_up(0.5, 0.45, 0.2, 3)
                self.screen_swipe_down(0.5, 0.3, 0.5, 3)

                self.judge_hw_adjust(mode, name)
            else:
                print('只有%s道大题' % len(mode))

    @teststeps
    def judge_hw_adjust(self, mode, name):
        """判断 调整题目顺序"""
        mode1 = self.game_type()
        name1 = self.game_name()
        print('----------------------------')
        print('题目顺序:')
        if len(mode1) > 5:
            for i in range(len(mode1) - 1):
                if mode == mode1 and name == name1:
                    print('★★★ Error- 调整题目顺序')
                    print(mode1[i].text, name1[i].text)
        else:
            for i in range(len(mode1)):
                if mode == mode1 and name == name1:
                    print('★★★ Error- 调整题目顺序')
                    print(mode1[i].text, name1[i].text)

    @teststeps
    def text_view(self):
        var = self.driver \
            .find_elements_by_xpath("//android.widget.RelativeLayout")
        content = []
        item = 0
        for i in range(1, len(var) - 5):
            ele = var[i].find_elements_by_xpath('//android.widget.TextView')

            if len(ele) == 4:
                item += 1
                for j in range(len(ele)):
                    print(ele[j].text)
                    content.append(ele[j].text)

        return content, item
