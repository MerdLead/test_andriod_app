# coding=utf-8
import HTMLTestRunner
import unittest
import time

from app.student.login.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.student.user_center.object_page.user_center_page import UserCenterPage, Setting, Privacy
from conf.base_page import BasePage
from conf.decorator import setupclass, teardownclass, testcase
from utils.toast_find import Toast


class PrivacyClause(unittest.TestCase):

    @classmethod
    @setupclass
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.user_center = UserCenterPage()
        cls.setting = Setting()
        cls.privacy_clause = Privacy()

    @classmethod
    @teardownclass
    def tearDown(cls):
        pass

    @testcase
    def test_privacy_clause(self):
        """版权申诉 -- 正常流程"""
        self.login_page.app_status()  # 判断APP当前状态

        if self.home_page.wait_check_page():
            self.home_page.click_tab_profile()  # 进入首页后点击‘个人中心’按钮

            if self.user_center.wait_check_page():  # 页面检查点
                self.user_center.click_setting()  # 进入设置页面
                if self.setting.wait_check_page():
                    self.setting.privacy_clause()  # 隐私条款

                    if self.privacy_clause.wait_check_page():
                        for i in range(4):
                            print('翻页%s次' % (i + 1))
                            BasePage().screen_swipe_up(0.5, 0.5, 0.25, 1000)
                        print('下拉一次')
                        BasePage().screen_swipe_down(0.5, 0.2, 0.9, 1000)

                        self.home_page.back_up_button()

                        if self.setting.wait_check_page():
                            print('success')
                        else:
                            print(' failed  ')
                        self.setting.back_up()  # 返回主界面
                    else:
                        print('未进入隐私条款页面')
        else:
            Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            print("未进入主界面")


if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(PrivacyClause('test_privacy_clause'))

        report_title = u'Example用例执行报告'
        desc = '用于展示修改样式后的HTMLTestRunner'
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        filename = 'C:\\Users\\V\\Desktop\\Testreport\\Result_' + timestr + '.html'
        print(filename)
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=report_title,
            description=desc)
        runner.run(suite)
        fp.close()
