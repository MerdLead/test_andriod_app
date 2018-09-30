#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from app.student.login.object_page.home_page import HomePage
from app.student.user_center.object_page.user_center_page import UserCenterPage
from app.student.user_center.test_data.image import VALID_IMAGE
from utils.click_bounds import ClickBounds
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class UserInfoPage(BasePage):
    """个人信息页面所有控件信息"""

    @teststep
    def wait_check_page(self, var=20):
        """以“title:个人信息”的xpath @text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'个人信息')]")
        try:
            WebDriverWait(self.driver, var, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def image(self):
        """以“头像”的id为依据
            用于判断是否有展示头像，但是具体头像内容不能判定"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/avatar")
        return ele

    @teststep
    def nickname(self):
        """以“昵称”的id为依据
            用于判断昵称修改前后是否相同，默认修改后的昵称与修改前不同"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/nick").text
        return ele

    @teststep
    def phone(self):
        """以“手机号”的id为依据
            用于判断手机号修改前后是否相同，默认修改后的手机号与修改前不同"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/phone").text
        return ele

    @teststep
    def click_image(self):
        """以“头像”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/avatar_profile")\
            .click()
        time.sleep(2)

    @teststep
    def click_nickname(self):
        """以“昵称”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/nick_profile")\
            .click()

    @teststep
    def click_username(self):
        """以“用户名”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/name_profile")\
            .click()

    @teststep
    def click_phone_number(self):
        """以“手机号”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/phone_profile")\
            .click()

    @teststep
    def click_password(self):
        """以“密码”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/pwd_profile")\
            .click()

    @teststep
    def input(self):
        """以“修改昵称/用户名/手机号的二级页面中输入框”的class_name为依据"""
        ele = self.driver\
            .find_element_by_class_name('android.widget.EditText')
        return ele

    @teststep
    def click_negative_button(self):
        """以“取消按钮”的id为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.student.debug:id/md_buttonDefaultNegative')\
            .click()

    @teststep
    def positive_button(self):
        """以“确认按钮”的id为依据"""
        ele = self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'确定')]")
        value = ele.get_attribute('enabled')
        return value

    @teststep
    def click_positive_button(self):
        """以“确认按钮”的id为依据"""
        self.driver\
            .find_element_by_id('com.vanthink.student.debug:id/md_buttonDefaultPositive')\
            .click()

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
        """title"""
        item = self.driver \
            .find_elements_by_id("com.vanthink.student.debug:id/md_title")
        for i in range(len(item)):
            print(item[i].text)
        print('---------------')
        return item

    @teststep
    def click_photograph(self):
        """以“拍照”的xpath @index为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'拍照')]") \
            .click()
        print('点击 拍照 按钮')

    @teststep
    def click_album(self):
        """以“从相册选择”的xpath @index为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'从相册选择')]") \
            .click()
        print('点击 从相册选择 按钮')

    @teststep
    def click_block(self):
        """点击页面空白区域"""
        ClickBounds().click_bounds(540, 300)

    @teststep
    def back_up_button(self):
        """以“返回按钮”的class name为依据"""
        self.driver\
            .find_element_by_class_name("android.widget.ImageButton")\
            .click()

    @teststeps
    def back_up(self):
        """从个人信息页 返回主界面"""
        if self.wait_check_page():
            self.back_up_button()  # 返回按钮
            if UserCenterPage().wait_check_page():  # 页面检查点
                HomePage().click_tab_hw()


class ChangeImage(BasePage):
    """更换头像功能所有控件信息
        之所以在这里定义,是为了避免每次调用click_bounds()时，再次计算坐标"""
    @teststep
    def wait_check_page_camera(self):
        """以拍照页面左下角按钮 的为依据"""
        locator = (By.XPATH,
                   "//android.widget.ImageView[contains(@resource-id, 'com.meizu.media.camera:id/flashlight_control')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_check_page_album(self):
        """以相册title:“选择照片”的ID为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'选择图片')]")
        element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))

        return element.text

    # 拍照
    @teststep
    def click_camera_button(self):
        """以相机拍照按钮"""
        # self.driver.keyevent(27)
        self.driver\
            .find_element_by_id("com.meizu.media.camera:id/shutter_btn")\
            .click()

    @teststep
    def wait_check_retake_page(self):
        """以拍照页面左下角按钮 的为依据"""
        locator = (By.XPATH,
                   "//android.widget.ImageView[contains(@resource-id, 'com.meizu.media.camera:id/btn_retake')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_retake_button(self):
        """相机'retake'按钮"""
        # click_bounds(self, 359.5, 1119.5)
        self.driver \
            .find_element_by_id("com.meizu.media.camera:id/btn_retake") \
            .click()

    @teststep
    def click_done_button(self):
        """相机'完成'按钮"""
        # click_bounds(self, 652.5, 1119.5)
        self.driver \
            .find_element_by_id("com.meizu.media.camera:id/btn_done") \
            .click()

    @teststep
    def wait_check_save_page(self):
        """以拍照页面左下角按钮 的为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text, '取消')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_cancel_button(self):
        """以“相机取消按钮”的id为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'取消')]") \
            .click()

    @teststep
    def click_save_button(self):
        """以“相机保存按钮”的id为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'完成')]") \
            .click()

    # 从相册选择
    @teststep
    def choose_album(self):
        """选择相册"""
        self.driver \
            .find_element_by_id("com.meizu.media.gallery:id/top_tab_gallery_title") \
            .click()

    @teststep
    def open_album(self):
        """打开相册"""
        self.driver \
            .find_elements_by_id("com.meizu.media.gallery:id/album_name")[0] \
            .click()

    @teststep
    def wait_check_all_picture_page(self):
        """所有图片 的为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@text, '所有图片')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def choose_image(self):
        """选择相册图片"""
        ClickBounds().click_bounds(float(VALID_IMAGE.location_x()), float(VALID_IMAGE.location_y()))

    @teststep
    def album_commit_button(self):
        """相册确定按钮"""
        self.driver \
            .find_element_by_id("com.meizu.media.gallery:id/action_get_multi_confirm") \
            .click()

    @teststep
    def back_up_button(self):
        """相册返回按钮"""
        self.driver \
            .find_element_by_id("android:id/home") \
            .click()


class PhoneReset(BasePage):
    """修改手机号页面所有控件信息"""

    @teststep
    def wait_check_page(self):
        """以“title:手机号码”的xpath @text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'手机号码')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def et_phone(self):
        """以“手机号”的id为依据"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/et_phone")
        return ele

    @teststep
    def verify(self):
        """以“验证码”的id为依据"""

        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/verify_input")
        return ele

    @teststep
    def count_time(self):
        """以“获取验证码按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/count_time")\
            .click()

    @teststep
    def btn_certain(self):
        """以“确定按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/btn_certain")\
            .click()


class PwdReset(BasePage):
    """修改密码页面所有控件信息"""

    @teststep
    def wait_check_page(self):
        """以“title:重置密码”的xpath @text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'重置密码')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def pwd_origin(self):
        """以“原始密码”的id为依据"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/pwd_origin")
        return ele

    @teststep
    def pwd_new(self):
        """以“新密码”的id为依据"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/pwd_new")
        return ele

    @teststep
    def pwd_confirm(self):
        """以“新密码二次确认”的id为依据"""
        ele = self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/pwd_confirm")
        return ele

    @teststep
    def pwd_checkbox(self):
        """以“显示密码”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/pwd_visible")\
            .click()

    @teststep
    def confirm_button(self):
        """以“完成按钮”的id为依据"""
        self.driver\
            .find_element_by_id("com.vanthink.student.debug:id/pwd_complete")\
            .click()

    @teststep
    def pwd_tips(self):
        """以“密码组成提示”的xpath @text为依据"""
        self.driver\
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'密码由6-20位英文字母或数字组成')]")
