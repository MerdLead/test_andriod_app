import time
from app.student.login.test_data.account import VALID_ACCOUNT
from app.student.login.object_page.home_page import HomePage
from app.student.user_center.object_page.user_center_page import UserCenterPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class LoginPage(BasePage):

    @teststeps
    def wait_check_page(self):
        """以“登录按钮”的xpath@text为依据"""
        locator = (By.XPATH, "//android.widget.Button[contains(@text,'登录')]")
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def input_username(self, username):
        """以“请输入手机号码”的TEXT为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.EditText[contains(@text,'请输入手机号')]") \
            .send_keys(username)

    @teststep
    def input_password(self, password):
        """以“请输入登录密码”的XPATH为依据"""
        self.driver \
            .find_elements_by_xpath("//android.widget.EditText[contains(@index,0)]")[1] \
            .send_keys(password)

    @teststep
    def login_button(self):
        """以“登录”Button的ID为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.Button[contains(@text,'登录')]") \
            .click()

    @teststep
    def register(self):
        """以“注册帐号”的ID为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.student.debug:id/register') \
            .click()

    @teststep
    def remember_password(self):
        """以“显示密码”的ID为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.student.debug:id/pwd_visible') \
            .click()

    @teststep
    def forget_password(self):
        """以“忘记密码？”的ID为依据"""
        self.driver \
            .find_element_by_id('com.vanthink.student.debug:id/forget_pwd') \
            .click()

    @teststeps
    def login(self):
        """登录"""
        print('在登录界面：')
        time.sleep(2)
        self.input_username(VALID_ACCOUNT.account())
        self.input_password(VALID_ACCOUNT.password())
        self.login_button()
        time.sleep(2)

    @teststeps
    def app_status(self):
        """判断应用当前状态"""
        activity = self.wait_activity()
        if HomePage().wait_check_page():  # 在主界面
            print('主界面')
        elif activity == '':  # 崩溃退出
            self.launch_app()  # 重启APP
            if HomePage().wait_check_page():  # 在主界面
                print('主界面')
            elif self.wait_check_page():  # 在登录界面
                self.login()
        elif self.wait_check_page():  # 在登录界面
            self.login()
        else:
            print('在其他页面')
            self.close_app()  # 关闭APP
            self.launch_app()  # 重启APP
            if HomePage().wait_check_page():  # 在主界面
                print('主界面')
            elif self.wait_check_page():  # 在登录界面
                self.login()

    @teststeps
    def enter_user_info_page(self):
        """由 主界面 进入个人信息页"""
        if HomePage().wait_check_page():
            # 进入首页后点击‘个人中心’按钮
            HomePage().click_tab_profile()
            # 点击登录头像按钮，进行个人信息操作
            UserCenterPage().click_avatar_profile()

    @teststep
    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        self.driver.launch_app()
        time.sleep(5)

    @teststep
    def close_app(self):
        """Close on the device the application specified in the desired capabilities.
        """
        self.driver.close_app()

    @teststep
    def remove_app(self):
        """Remove on the device the application
        """
        self.driver.remove_app("com.vanthink.student.debug")

    @teststep
    def is_app_installed(self):
        """Check app was installed on the device the application
        """
        self.driver.is_app_installed("com.vanthink.student.debug")

    @teststep
    def install_app(self):
        """Remove on the device the application
        """
        self.driver.install_app('../student_debug_1.2.7.apk')
        print('安装APP')
