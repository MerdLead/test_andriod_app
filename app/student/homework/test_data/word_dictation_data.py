import random


# data base of word dictation
# we can add a or multiple expalin_word in it, like this '{'explain': 'xxxxxxxxxxx', 'word': 'yyyyyyyy'},'
_VALID_WORDDICTATION = (
    {'explain': '你好（首字母大写，自定义去除最后一个字母）', 'word': 'Hello'},
    {'explain': '结束（自定义去除最后一个字母）', 'word': 'over'},
    {'explain': '苹果（首字母大写，自定义去除最后一个字母）', 'word': 'Apple'},
    {'explain': '喜欢（自定义去除最后一个字母）', 'word': 'like'},
    {'explain': '但是（自定义去除最后一个字母）', 'word': 'but'},
    {'explain': '一样的单词', 'word': 'aabbcd'},

)


class WordDictation:
    def __init__(self):
            self.valid_word_dict = _VALID_WORDDICTATION[random.randint(0, len(_VALID_WORDDICTATION)) - 1]

    # def explain(self):
    #     return self.valid_word_dict['explain']

    def word(self):
        return self.valid_word_dict['word']


# global variable
# a instance of expalin_word
# it can be used in any place via 'from App.student.test_data.word_dictation_data import VALID_WORD_DICT'
VALID_WORD_DICT = WordDictation()
# VALID_WORD_DICT.explain()
VALID_WORD_DICT.word()

