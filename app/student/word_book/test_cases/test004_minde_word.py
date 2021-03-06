import unittest

from app.student.homework.object_page.home_page import HomePage
from app.student.word_book.object_page.data_action import DataActionPage
from app.student.word_book.object_page.my_word_page import MyWordPage
from app.student.word_book.object_page.word_book import WordBook
from app.student.word_book.object_page.clear_user_data import CleanDataPage
from conf.decorator import setup, teardown, teststeps


class MineWord(unittest.TestCase):

    @classmethod
    @setup
    def setUp(cls):
        cls.home = HomePage()
        cls.word = WordBook()
        cls.mine = MyWordPage()


    @teardown
    def tearDown(self):
        pass

    @teststeps
    def test_mine_word(self):
        """我的单词"""
        if self.home.wait_check_page ():  # 页面检查点
            DataActionPage ().get_id_back_home()
            if self.home.wait_check_page ():  # 页面检查点
                print ('进入主界面')
                self.home.click_hk_tab (1)  # 点击 背单词
                if self.home.wait_check_word_title():  # 页面检查点
                    total = self.word.total_word()
                    self.mine.click_my_word_btn()
                    if self.mine.wait_check_mine_word_page():
                        if self.mine.no_word_tips():
                            self.mine.no_word_tip_text()
                        else:
                            self.mine.play_mine_word(total)

