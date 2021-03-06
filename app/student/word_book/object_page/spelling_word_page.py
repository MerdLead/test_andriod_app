
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from app.student.homework.object_page.homework_page import Homework
from app.student.word_book.object_page.data_action import DataActionPage
from app.student.word_book.object_page.flash_card_page import FlashCard
from conf.base_page import BasePage
from conf.decorator import teststeps, teststep
from utils.games_keyboard import games_keyboard
from utils.get_attribute import GetAttribute


class SpellingWord(BasePage):
    """单词拼写"""
    def __init__(self):
        self.get = GetAttribute()
        self.homework = Homework()
        self.common = DataActionPage()

    @teststeps
    def wait_check_page(self):
        """以“词汇选择 -句子选单词模式”的 提示按钮 为依据"""
        locator = (By.XPATH,
                   "//android.widget.TextView[contains(@resource-id,'com.vanthink.student.debug:id/hint')]")
        try:
            WebDriverWait(self.driver, 2, 0.5).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    @teststep
    def explain(self):
        """展示的翻译"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_explain").text
        return word

    @teststep
    def word(self):
        """展示的Word"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        word = ele[1::2]
        print('word：', word)

    @teststep
    def mine_answer(self):
        """展示的Word  前后含额外字符:aa"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return word[::2]

    @teststep
    def finish_word(self):
        """完成答题 之后 展示的Word 每个字母之间有空格"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return word[::2]

    @teststep
    def correct_judge(self):
        """判断 答案是否展示"""
        try:
            self.driver.find_element_by_id("com.vanthink.student.debug:id/tv_answer")
            return True
        except:
            return False

    @teststep
    def correct(self):
        """展示的答案"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_answer").text
        return word

    # 默写模式
    @teststep
    def hint_button(self):
        """提示按钮"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/hint")
        return ele

    @teststeps
    def dictation_word_judge(self):
        """判断是否展示Word"""
        try:
            self.driver \
                .find_element_by_id("com.vanthink.student.debug:id/tv_word")
            return True
        except:
            return False

    @teststeps
    def dictation_word(self):
        """展示的Word"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        value = ele[::2]
        return value

    @teststeps
    def dictation_pattern_new(self, i):
        """单词默写 新词"""
        if i == 0:
            print('\n单词拼写 - 默写模式(新词)\n')
        self.dictation_pattern_core()

    @teststeps
    def dictation_pattern_recite(self, i,first_game):
        """单词默写 新词"""
        if i == 0:
            level1_count = self.common.get_different_level_words(1)  # 获取需要B轮复习的单词
            if level1_count != 0:
                if first_game[0] != '词汇选择(复习)':
                    print ('★★★ Error-第一个游戏不是B1的词汇选择游戏')
                else:
                    print ("B轮单词存在,首个游戏为 '词汇选择(复习)' 名称正确！")
            else:
                if first_game[0] != '词汇运用(复习)':
                    print ("★★★ Error-第一个游戏不是B2/C1/D1/E1的词汇运用游戏'")
                else:
                    print ("B轮单词已结束，首个游戏为 '词汇运用(复习)' 名称正确！\n")

            print ('\n单词拼写 - 默写模式(新词)\n')
        self.dictation_pattern_core ()


    @teststeps
    def dictation_pattern_mine(self, i,familiar_add):
        """单词默写 我的单词"""
        if i == 0:
            print ("\n单词拼写 - 默写模式(单词详情)\n")
        explain = self.explain ()  # 题目
        value = self.common.get_word_by_explain (explain)
        familiars = self.common.get_familiar_words () + familiar_add
        if i in range(0,5):
            self.dictation_pattern_core()
            if value not in familiars:
                print ('★★★ Error-- 单词未被标熟却出现默写模式')
        else:
            FlashCard().tips_operate()
            for i in familiar_add:
                level = self.common.get_word_level(i)
                if level < 3:
                    print("★★★ Error--提交未成功，单词熟练度未更改")


    def dictation_pattern_core(self):
        """单词拼写 - 《默写模式》游戏过程"""
        explain = self.explain ()  # 题目
        value = self.common.get_word_by_explain (explain)

        self.homework.next_button_operate ('false')  # 下一题 按钮 判断加 点击操作
        if self.dictation_word_judge ():  # 默写模式 - 字母未全部消除
            print ('★★★ Error - 单词拼写 默写模式 - 字母未全部消除')

        hint = self.hint_button ()  # 提示按钮

        if self.get.enabled (hint) == 'true':
            hint.click ()  # 点击 提示按钮
            if self.get.enabled (self.hint_button ()) != 'false':
                print ('★★★ Error - 点击后提示按钮enabled属性错误')

            if self.dictation_word_judge ():  # 出现首字母提示
                word = self.dictation_word ()
                if len (word) == 1:
                    if word == value[0]:
                        print ('点击提示出现首字母提示', word)
                    else:
                        print('点击提示出现首字母提示', word)
                        print ("★★★ Error - 首字母提示错误")
                else:
                    print ('★★★ Error - 提示字母不为一个')
            else:
                print ("★★★ Error - 首字母提示未出现")
        else:
            print ('★★★ Error - 提示按钮enabled属性错误')

        games_keyboard ('backspace')
        for j in range (0, len (value)):
            self.keyboard_operate (j, value[j])  # 点击键盘 具体操作

        answer = self.finish_word ()  # 我的答案
        self.homework.next_button_operate ('true')  # 下一题 按钮 状态判断 加点击
        self.result_operate (answer, self.mine_answer ())  # 下一步按钮后的答案页面 测试
        self.homework.click_voice ()
        self.homework.next_button_operate ('true')  # 下一题 按钮 状态判断 加点击


    @teststeps
    def result_operate(self, answer, mine):
        """下一步按钮后的答案页面"""
        print('我的答案:', answer)
        print('答题结果:', mine)
        if self.correct_judge():
            correct = self.correct()  # 正确答案
            if len(mine) <= len(correct):  # 输入少于或等于单词字母数的字符
                if mine.lower() != answer.lower():  # 展示的 我的答题结果 是否与我填入的一致
                    print('★★★ Error - 字符数少于或等于时:', mine.lower(), answer.lower())
            else:  # 输入过多的字符
                if correct + mine[len(correct):].lower() != correct + answer[len(correct):].lower():  # 展示的 我的答题结果 是否与我填入的一致
                    print('★★★ Error - 字符输入过多时:', correct + mine[len(correct):].lower(),correct + answer[len(correct):].lower())
        else:  # 回答正确
            if mine.lower() != answer.lower():  # 展示的 我的答题结果 是否与我填入的一致
                print('★★★ Error - 展示的答题结果 与我填入的不一致:', mine.lower(), answer.lower())
            else:
                print('回答正确!')
        print('----------------------------------')

    @teststeps
    def keyboard_operate(self, j, value):
        """点击键盘 具体操作"""
        if j == 4:
            games_keyboard('capslock')  # 点击键盘 切换到 大写字母
            games_keyboard(value.upper())  # 点击键盘对应 大写字母
            games_keyboard('capslock')  # 点击键盘 切换到 小写字母
        else:
            games_keyboard(value)  # 点击键盘对应字母

