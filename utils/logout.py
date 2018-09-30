#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from app.student.user_center.object_page.user_center_page import Setting
from app.student.login.object_page.home_page import HomePage
from conf.base_page import BasePage
from conf.decorator import teststeps


class PublicFunction(BasePage):
    """二级页面：问题反馈页面"""

    @teststeps
    def logout(self):
        """退出登录"""
        Setting().logout_button()  # 退出登录 按钮
        self.driver.implicitly_wait(2)
        if HomePage().wait_activity == "com.vanthink.vanthinkstudent.v2.ui.user.login.LoginActivity":
            print('退出登录成功!!!')
        else:
            print(' 退出登录失败 ')
