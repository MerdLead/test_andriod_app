#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.teacher.homework.object_page.release_hw_page import ReleasePage
from conf.basepage import BasePage
from conf.decorator import teststep, teststeps


class SpokenDetailPage(BasePage):
    """ 口语详情 页面"""
    @teststeps
    def __init__(self):
        self.tips = ReleasePage()

    @teststeps
    def wait_check_spoken_page(self):
        """以“title: 老师测试版”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'老师测试版')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def wait_check_spoken_detail_page(self):
        """以“title: 按题查看”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'按题查看')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def st_finish_status(self):
        """学生 完成与否"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/status")
        return ele

    @teststep
    def st_name(self):
        """学生 昵称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/name")
        return ele

    @teststep
    def st_icon(self):
        """学生 头像"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/head")
        return ele

    # 详情页
    @teststeps
    def wait_check_detail_page(self):
        """以“title: 详情”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'详情')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def sentence(self):
        """句子"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/sentence")
        return ele

    @teststep
    def finish_ratio(self):
        """完成率"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/finish_ratio")
        return ele

    @teststep
    def spoken_speak(self):
        """播音按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_speak")
        return ele

    @teststep
    def all_pass_button(self):
        """全部过关 按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/all_pass")
        return ele

    @teststep
    def pass_button(self):
        """过关按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/is_pass")
        return ele

    @teststep
    def judge_result_name(self):
        """判断是否存在 结果元素"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/result_name")
            return True
        except:
            return False

    @teststep
    def result_name(self):
        """结果"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/result_name")
        return ele

    # 主界面 小题详情页
    @teststep
    def explain(self):
        """说明"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/explain").text
        return ele

    @teststep
    def total_report(self):
        """小题 报告"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/report").text
        return ele

    @teststep
    def enabled(self, var):
        """元素 enabled属性值"""
        value = var.get_attribute('enabled')
        return value

    @teststeps
    def judge_all_pass_button(self):
        """全部过关 按钮"""
        all_pass = self.all_pass_button()
        if self.enabled(all_pass):
            all_pass.click()
            if self.tips.wait_check_tips_page():
                self.tips.cancel_button()

                if self.wait_check_detail_page():  # 页面检查点
                    all_pass = self.all_pass_button()
                    all_pass.click()
                    if self.tips.wait_check_tips_page():
                        self.tips.commit_button()

            if self.wait_check_detail_page():  # 页面检查点
                all_pass = self.all_pass_button()
                if self.enabled(all_pass):
                    all_pass.click()
                    if self.tips.wait_check_tips_page():
                        self.tips.commit_button()
        #         else:
        #             print('★★★ Error- 2全部过关 按钮状态', self.enabled(all_pass))
        # else:
        #     print('★★★ Error- 全部过关 按钮状态', self.enabled(all_pass))
        print('-------------------------')
