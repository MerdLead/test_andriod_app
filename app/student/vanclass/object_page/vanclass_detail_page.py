#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.base_page import BasePage
from conf.decorator import teststep, teststeps
from utils.click_bounds import ClickBounds


class VanclassDetailPage(BasePage):
    """ 班级详情页 修改、查询页面元素信息"""
    # 修改 页面
    @teststeps
    def wait_check_tips_page(self, var=20):
        """以“icon”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.student.debug:id/md_title')]")
        try:
            WebDriverWait(self.driver, var, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def tips_title(self):
        """提示框 title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/md_title").text
        print(item)
        return item

    @teststep
    def tips_content(self):
        """提示框 具体内容"""
        item = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/md_content").text
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
            .find_element_by_id("com.vanthink.student.debug:id/md_minMax").text
        print(ele)
        return ele

    @teststep
    def commit_button(self):
        """确定 按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/md_buttonDefaultPositive")
        return ele

    @teststep
    def cancel_button(self):
        """取消 按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/md_buttonDefaultNegative")
        return ele

    @teststep
    def enabled(self, var):
        """元素 enabled属性值"""
        value = var.get_attribute('enabled')
        return value

    @teststeps
    def click_block(self):
        ClickBounds().click_bounds(540, 200)

    # 积分排行榜
    @teststeps
    def wait_check_score_page(self):
        """以“title:积分排行榜”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'积分排行榜')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def score_all_tab(self, index):
        """本周 &上周 &本月 &全部 index=1-4"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView")[index]
        return ele

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

    @teststep
    def st_order(self):
        """排序"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_order")
        return ele

    @teststep
    def st_icon(self):
        """头像"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_student_icon")
        return ele

    @teststep
    def st_name(self):
        """学生 昵称"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_student_name")
        return ele

    @teststep
    def num(self):
        """积分/星星数目"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_nums")
        return ele

    # 星星排行榜
    @teststeps
    def wait_check_star_page(self):
        """以“title:星星排行榜”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'星星排行榜')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    # 本班作业
    @teststeps
    def wait_check_page(self, var):
        """以“title: 班级名称/ 作业名称/本班卷子/口语作业”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % var)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def all_finish_tab(self, index):
        """全部 未完成 已完成  index= 1-3"""
        ele = self.driver \
            .find_elements_by_xpath("//android.widget.TextView")[index]
        # item = self.driver \
        #     .find_elements_by_xpath("//android.widget.TextView")
        # for i in range(len(item)):
        #     print(item[i].text)
        return ele

    @teststep
    def end_tips(self):
        """没有更多了"""
        try:
            self.driver.find_element_by_id("com.vanthink.student.debug:id/end")
            return True
        except Exception:
            return False

    @teststep
    def hw_name(self):
        """作业name"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_homework_name")
        return ele

    @teststep
    def accurency(self):
        """正答率"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_accurency")
        return ele

    @teststep
    def spend_time(self):
        """用时"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_spend_time")
        return ele

    @teststep
    def progress(self):
        """完成进度"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/roundProgressBar")
        return ele

    @teststep
    def finish_status(self):
        """已经有x人完成"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_homework_desc")
        return ele

    @teststep
    def create_time(self):
        """作业创建时间"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_create_date")
        return ele

    @teststep
    def remind(self):
        """提醒 按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/remind")
        return ele

    @teststep
    def rank_button(self, index):
        """排行榜 按钮"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/iv_ranking")[index].click()
        return ele

    # 分享
    @teststep
    def share_button(self):
        """分享 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/share")\
            .click()

    @teststeps
    def wait_check_share_page(self, var=20):
        """以“title”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@text,'炫耀一下')]")
        try:
            WebDriverWait(self.driver, var, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def share_img(self):
        """图片"""
        try:
            self.driver.find_element_by_id("com.vanthink.student.debug:id/share_img")
            return True
        except Exception:
            return False

    @teststep
    def wechat_friend(self):
        """微信好友"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/weixin") \
            .click()
        print('微信好友')

    @teststep
    def wechat_circle(self):
        """微信朋友圈"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/weixin_friends") \
            .click()
        print('微信朋友圈')

    @teststep
    def save_img(self):
        """保存图片"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/save_img") \
            .click()
        print('保存图片')

    # 打卡
    @teststep
    def reward_button(self):
        """分享 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/reward") \
            .click()

    @teststeps
    def wait_check_reward_page(self, var=20):
        """以“title”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@text,'打卡')]")
        try:
            WebDriverWait(self.driver, var, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def get_reward_button(self):
        """礼包 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/iv_reward") \
            .click()

    @teststep
    def reward_desc(self):
        """提示：点击礼包打卡吧"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_reward_desc") \
            .text
        return ele

    @teststep
    def reward_tips(self):
        """获取奖励 说明"""
        ele = self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@index,'2')]") \
            .text
        print(ele)

    # 打卡结果页
    @teststeps
    def wait_check_reward_result_page(self, var=20):
        """以“title”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.student.debug:id/tv_cards')]")
        try:
            WebDriverWait(self.driver, var, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def reward_img(self):
        """图片"""
        try:
            self.driver.find_element_by_id("com.vanthink.student.debug:id/iv_reward_pic")
            return True
        except Exception:
            return False

    @teststep
    def check_complete_button(self):
        """查看完整卡片 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_cards") \
            .click()

    # 完整卡片页
    @teststeps
    def wait_check_complete_page(self, var=20):
        """以“title”为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id, com.vanthink.student.debug:id/iv_frag)]")
        try:
            WebDriverWait(self.driver, var, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def img_num(self):
        """图片 张数"""
        ele = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/tv_nums")
        return ele

    @teststeps
    def tips_operate(self):
        """tips弹框  """
        if self.wait_check_tips_page():  # tips弹框 检查点
            self.tips_title()
            self.tips_content()
            self.commit_button().click()  # 确定按钮
            print('------------------------------')

    @teststeps
    def button_enbaled_judge(self, length, button, size1):
        """确定按钮enabled状态"""
        if 0 < length <= 30:
            if length != int(size1):
                print('★★★ Error- 字符数展示有误', length, size1)
            else:
                if self.enabled(button) == 'false':
                    print('★★★ Error- 确定按钮不可点击')

        elif length == 0:
            if length != int(size1):
                print('★★★ Error- 字符数展示有误', length, size1)
            else:
                if self.enabled(button) == 'true':
                    print('★★★ Error- 确定按钮未置灰可点击')
        elif length > 30:
            if length != int(size1):
                print('★★★ Error- 字符数展示有误', length, size1)
            else:
                if self.enabled(button) == 'true':
                    print('★★★ Error- 确定按钮未置灰可点击')
        return self.enabled(button)
