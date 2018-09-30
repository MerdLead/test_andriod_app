#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from app.teacher.user_center.user_information.test_data.image import VALID_IMAGE
from conf.decorator import teststep, teststeps
from conf.basepage import BasePage
from utils.click_bounds import ClickBounds


class ChangeImage(BasePage):
    """更换头像功能所有控件信息
        之所以在这里定义,是为了避免每次调用click_bounds()时，再次计算坐标"""

    @teststeps
    def wait_check_page_camera(self):
        """以 “拍照键”的ID为依据"""
        locator = (By.XPATH,
                   "//android.widget.ImageView[contains(@resource-id,'com.meizu.media.camera:id/shutter_btn')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def wait_check_page_album(self):
        """以相册title:“选择图片”的text为依据"""
        locator = (By.XPATH, "//android.widget.TextView[contains(@text,'选择图片')]")
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def click_camera_button(self):
        """以相机拍照按钮"""
        time.sleep(2)
        self.driver \
            .find_element_by_id("com.meizu.media.camera:id/shutter_btn") \
            .click()

    @teststep
    def click_cancel_button(self):
        """以“相机重拍按钮”的id为依据"""
        # click_bounds(self, 67.5, 1119.5)
        self.driver \
            .find_element_by_id("com.android.camera: id / btn_cancel") \
            .click()

    @teststep
    def click_done_button(self):
        """相机'完成'按钮"""
        time.sleep(2)
        self.driver \
            .find_element_by_id("com.meizu.media.camera:id/btn_done") \
            .click()

    @teststep
    def click_retake_button(self):
        """相机'retake'按钮"""
        time.sleep(2)
        self.driver \
            .find_element_by_id("com.meizu.media.camera:id/btn_retake") \
            .click()

    @teststep
    def click_save_button(self):
        """相机保存按钮"""
        time.sleep(2)
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'完成')]")\
            .click()

    @teststep
    def click_cancel_button(self):
        """相机取消按钮"""
        time.sleep(2)
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'取消')]")\
            .click()

    @teststep
    def click_album(self):
        """点击相册"""
        time.sleep(2)
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'相册')]")\
            .click()

    @teststep
    def choose_album(self):
        """选择相册370,720"""
        ClickBounds().click_bounds(320, 500)

    @teststep
    def choose_image(self):
        """选择相册图片"""
        time.sleep(2)
        print(float(VALID_IMAGE.location_x()), float(VALID_IMAGE.location_y()))
        ClickBounds().click_bounds(float(VALID_IMAGE.location_x()), float(VALID_IMAGE.location_y()))

    @teststep
    def commit_button(self):
        """相册确定按钮"""
        # click_bounds(self, 678, 69)
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'确定')]")\
            .click()

    @teststep
    def cancel_button(self):
        """相册取消按钮"""
        # click_bounds(self, 678, 69)
        self.driver \
            .find_element_by_id("com.android.gallery3d:id/action_cancel") \
            .click()

    @teststep
    def back_up_button(self):
        """相册返回按钮"""
        # click_bounds(self, 43, 74)
        self.driver \
            .find_element_by_id("android:id/home") \
            .click()
