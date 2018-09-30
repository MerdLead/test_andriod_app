import time

from app.student.homework.object_page.homework_page import Homework
from app.teacher.wordbook.test_cases.mysql import MysqlWord
from conf.basepage import BasePage
from conf.decorator import teststeps, teststep
from utils.games_keyboard import games_keyboard


class SpellingWord(BasePage):

    @teststep
    def explain(self):
        """展示的翻译"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_explain").text
        print("解释：",word)
        return word

    # -----------自定义模式的元素-------------
    @teststep
    def word(self):
        """展示的Word"""
        ele = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        word = ele[1::2]
        print('word：', word)
        return word

    @teststep
    def mine_answer(self):
        """展示的Word  前后含额外字符:aa"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return word[1::2]

    @teststeps
    def keyboard_operate(self, j, value):
        """点击键盘 具体操作"""
        if j == 4:
            games_keyboard('capslock')  # 点击键盘 切换到 大写字母
            games_keyboard(value.upper())  # 点击键盘对应 大写字母
            games_keyboard('capslock')  # 点击键盘 切换到 小写字母
        else:
            games_keyboard(value)  # 点击键盘对应字母

    @teststep
    def finish_word(self):
        """完成答题 之后 展示的Word 前后含额外字符：aa"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return word[1::2]

    @teststep
    def judge_by_id(self,element):
        """判断 答案是否展示"""
        try:
            self.driver.find_element_by_id(element)
            return True
        except:
            return False

    @teststep
    def correct(self):
        """展示的答案"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_answer").text
        return word

    #----------默写模式的元素--------------
    @teststep
    def dictation_finish_word(self):
        """完成答题 之后 展示的Word  前后不含额外字符:aa"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return word[::2]

    @teststep
    def dictation_mine_answer(self):
        """展示的Word  前后不含额外字符:aa"""
        word = self.driver \
            .find_element_by_id("com.vanthink.student.debug:id/tv_word").text
        return word[::2]

    @teststeps
    def click_voice(self):
        self.driver.find_element_by_id("com.vanthink.student.debug:id/play_voice").click()


    @teststeps
    def word_spell(self):
        print("-----------------")
        answer = []  # return值 与结果页内容比对
        explain = self.explain()
        value = MysqlWord().get_word(explain)[0]
        if self.judge_by_id("com.vanthink.student.debug:id/tv_word"):    #页面是否有单词，有则为自定义模式
            word = self.word()  # 未缺失的字母
            if value != word:  # 随机消除的字母消除了
                for j in range(len(value)):
                    if value[j] != word[j]:
                        print('缺失的字母：', value[j])
                        self.keyboard_operate(j, value[j])  # 点击键盘 具体操作
                answer.append(self.finish_word())  # 我的答案
                Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
                self.result_operate(answer, self.mine_answer())  # 下一步按钮后的答案页面 测试

        else:  # 没有则为默写模式
            for i in range(0,len(value)):
                print('缺失的字母：', value[i])
                self.keyboard_operate(i, value[i])
            answer.append(self.dictation_finish_word())  # 我的答案
            Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
            self.result_operate(answer, self.dictation_mine_answer())  # 下一步按钮后的答案页面 测试
        Homework().next_button_operate('true')  # 下一题 按钮 状态判断 加点击
        time.sleep(3)



    @teststeps
    def result_operate(self, answer, mine):
        result = answer[len(answer) - 1]
        print('我的答案:', result)
        print('答题结果:', mine)
        if self.judge_by_id("com.vanthink.student.debug:id/tv_answer"):
            correct = self.correct()  # 正确答案
            if len(mine) <= len(correct):  # 输入少于或等于单词字母数的字符
                if mine.lower() != result.lower():  # 展示的 我的答题结果 是否与我填入的一致
                    print('Error - 字符数少于或等于时:', mine.lower(), result.lower())
            else:  # 输入过多的字符
                if correct + mine[len(correct):].lower() != correct + result[
                                                                      len(correct):].lower():  # 展示的 我的答题结果 是否与我填入的一致
                    print('Error - 字符输入过多时:', correct + mine[len(correct):].lower(),
                          correct + result[len(correct):].lower())
        else:  # 回答正确
            if mine.lower() != result.lower():  # 展示的 我的答题结果 是否与我填入的一致
                print('Error - 展示的答题结果 与我填入的不一致:', mine.lower(), result.lower())