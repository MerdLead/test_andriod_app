# coding=utf-8
import unittest

from app.student.login.object_page.home_page import HomePage
from app.student.homework.object_page.homework_page import Homework
from app.student.login.object_page.login_page import LoginPage
from app.student.login.test_data.login_failed_toast import VALID_LOGIN_TOAST
from app.teacher.wordbook.object_page.word_book import Word_Book
from conf.decorator import setup, teardown, testcase
from utils.toast_find import Toast

class Games(unittest.TestCase):
    """听力选择"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.homework = Homework()
        cls.word_book = Word_Book()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_listen_choice(self):
        self.login_page.app_status()  # 判断APP当前状态
        if self.home_page.wait_check_page():
            print("已进入主界面：")
            self.home_page.click_recite_word_label()
            if self.word_book.wait_check_page():
                self.word_book.word_book_type()   #单词本游戏过程
                self.word_book.play_again()    #再练一组
            else:
                print("未进入单词本界面")
        else:
            try:
                Toast().find_toast(VALID_LOGIN_TOAST.login_failed())
            except Exception:
                print("未进入主界面")
                raise



