#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from conf.basepage import BasePage
from conf.decorator import teststep, teststeps
from utils.click_bounds import ClickBounds


class PaperDetailPage(BasePage):
    """试卷 详情页面"""

    @teststeps
    def wait_check_page(self):
        """以“title:布置试卷”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'布置试卷')]")
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
    def share_button(self):
        """分享 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/share") \
            .click()

    @teststep
    def paper_type(self):
        """试卷"""
        if self.driver.find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_paper"):
            item = self.driver.find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_paper")
            print(item.text)
            return True
        else:
            return False

    @teststep
    def paper_title(self):
        """title"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_paper_name") \
            .text
        print('试卷名称:', item)
        return item

    @teststep
    def teacher_nickname(self):
        """作者"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_author") \
            .text
        print('上传者:', item)
        return item

    @teststep
    def question_name(self):
        """小游戏名"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_name")
        return item

    @teststep
    def num(self, index):
        """每个小游戏 题数"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_desc")[index]
        return item

    @teststep
    def arrow(self, index):
        """箭头"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/iv_arrow")[index]
        return item

    @teststep
    def assign_button(self):
        """布置试卷 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_assign") \
            .click()

    @teststep
    def sentence(self):
        """句子"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/tv_answer")
        return item

    # 分享 功能
    @teststeps
    def wait_check_share_page(self):
        """以“title:分享”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'分享')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def help_button(self):
        """? 按钮 """
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/question") \
            .click()

    @teststep
    def school_upload_img(self):
        """学校徽标 图片上传 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/upload_img")\
            .click()

    @teststep
    def qr_upload_img(self):
        """二维码 图片上传 按钮"""
        self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/upload_img_qr") \
            .click()

    @teststeps
    def all_element(self):
        """页面内所有class name为android.widget.TextView的元素"""
        ele = self.driver \
            .find_elements_by_class_name("android.widget.TextView")
        content = []
        for i in range(len(ele)):
            # print(ele[i].text)
            content.append(ele[i].text)
        # print('++++++++++++++++')
        return ele, content

    @teststeps
    def share_name(self):
        """页面名称"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_name").text
        print(item)
        return item

    @teststeps
    def share_name_edit(self):
        """页面名称 编辑框"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/name")
        return item

    @teststeps
    def share_school(self):
        """学校"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_school").text
        print(item)
        return item

    @teststeps
    def share_school_edit(self):
        """学校 编辑框"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/school")
        return item

    @teststeps
    def share_contact(self):
        """联系方式"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/tv_contact_information").text
        print(item)
        return item

    @teststeps
    def share_contact_edit(self):
        """联系方式 编辑框"""
        item = self.driver \
            .find_element_by_id("com.vanthink.vanthinkteacher.debug:id/contact_information")
        return item

    @teststep
    def click_next(self):
        """点击键盘 下一个 按钮"""
        ClickBounds().click_bounds(994, 1845)

    @teststep
    def click_hide(self):
        """点击 隐藏键盘 按钮"""
        ClickBounds().click_bounds(990, 1210)

    @teststep
    def wechat_friend(self):
        """微信好友"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'微信好友')]") \
            .click()

    @teststep
    def wechat_circle(self):
        """微信朋友圈"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'微信朋友圈')]") \
            .click()

    @teststep
    def copy_link(self):
        """复制链接"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'复制链接')]")\
            .click()

    # 该校h5分享次数已用完
    @teststeps
    def wait_check_toast_page(self):
        """以“title:提示”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'提示')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def share_page_info(self):
        """试卷详情页 分享页面信息"""
        content = self.all_element()

        name = self.share_name_edit()  # 页面名称
        school = self.share_school_edit()  # 学校
        contact = self.share_contact_edit()  # 联系方式

        print('------------------------------------------')
        print('试卷分享页面：', '\n',
              content[1][1], '\n',
              content[1][3], '\n',
              content[1][4], '\n',
              content[1][5], ':', name.text, '\n',
              content[1][6], ':', school.text, '\n',
              content[1][7], ':', contact.text, '\n',
              content[1][8], ':', content[1][9:12])
        print('------------------------------------------')

    # 使用说明
    @teststeps
    def wait_check_help_page(self):
        """以“title:使用说明”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'使用说明')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    # 上传图片
    @teststeps
    def wait_check_change_page(self):
        """以“title:更改学校图标”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'更改学校图标')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststeps
    def wait_check_exchange_page(self):
        """以“title:更改二维码”为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'更改二维码')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_photograph(self):
        """以“拍照”的xpath @index为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'拍照')]") \
            .click()

    @teststep
    def click_album(self):
        """以“从相册选择”的xpath @index为依据"""
        time.sleep(2)
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'从相册选择')]") \
            .click()

    # 布置试卷 页面
    @teststep
    def choose_button(self):
        """单选框"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/choose")
        return item

    @teststep
    def class_name(self):
        """班级名称"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/class_name")
        return item

    @teststep
    def choose_count(self):
        """每个班级的描述信息： 选择了x/x位学生"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.vanthinkteacher.debug:id/choose_count")
        return item

    # 温馨提示 页面
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
    def tips_page_info(self):
        """温馨提示 页面信息"""
        print('------------------------------------------', '\n',
              '温馨提示 页面:')

        if self.wait_check_tips_page():
            self.tips_title()
            self.tips_content()
            self.never_notify()  # 不再提醒
            self.cancel_button()  # 取消按钮

            self.assign_button()  # 布置试卷 按钮
            if self.wait_check_tips_page():
                self.commit_button()
        else:
            print('★★★ Error- 无icon')

    @teststeps
    def assign_page_info(self):
        """试卷详情页 布置试卷页面信息"""
        if self.wait_check_share_page():
            content = self.all_element()
            print('------------------------------------------')
            print('布置试卷页面：', '\n',
                  content[1][1], '\n',
                  content[1][2])
            name = self.class_name()  # 班级名
            count = self.choose_count()  # 班级描述信息
            print('------------------------', '\n',
                  '班级列表：')
            for i in range(len(count)):
                print('  ', name[i].text, ' ', count[i].text)
