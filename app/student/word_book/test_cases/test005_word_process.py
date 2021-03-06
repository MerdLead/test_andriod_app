import unittest

from app.student.homework.object_page.home_page import HomePage
from app.student.login.object_page.login_page import LoginPage
from app.student.word_book.object_page.data_action import DataActionPage
from utils.mysql_data import MysqlData
from app.student.word_book.object_page.word_book import WordBook
from app.student.word_book.object_page.word_progress import ProgressPage
from conf.decorator import setup, teardown


class WordProcess(unittest.TestCase):
    @classmethod
    @setup
    def setUp(cls):
        cls.home = HomePage()
        cls.mysql = MysqlData()
        cls.word = WordBook()
        cls.progress = ProgressPage()
        cls.login = LoginPage ()
        cls.login.app_status ()  # 判断APP当前状态
        DataActionPage().get_id_back_home()

    @teardown
    def tearDown(self):
        pass

    def test_word_process(self):
        if self.home.wait_check_page():
            print('进入主界面')
            self.home.click_hk_tab (1)  # 点击 背单词
            if self.word.wait_check_start_page():
                self.progress.word_progress_icon()
                if self.progress.wait_check_progress_page():
                    self.progress.progress_ele_check()
                    self.home.back_to_home()


