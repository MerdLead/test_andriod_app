import datetime

from app.student.homework.object_page.home_page import HomePage
from utils.mysql_data import MysqlData
from conf.base_page import BasePage
from conf.decorator import teststep
from conf.base_config import GetVariable as gv


class DataActionPage(BasePage):
    """数据操作类"""
    def __init__(self):
        self.mysql = MysqlData()
        self.home = HomePage()

    @teststep
    def get_user_phone(self):
        """获取用户手机号"""
        self.home.click_tab_profile ()
        if self.home.wait_check_head_img ():
            self.home.click_avatar_profile ()
            if self.home.wait_check_person_msg ():
                phone = self.home.user_phone ()
                user_phone = phone.replace ("****", "1111")
                return user_phone

    @teststep
    def get_student_id(self):
        """获取学生id"""
        phone = self.get_user_phone()
        stu_id = self.mysql.find_student_id (phone)
        gv.STU_ID = stu_id


    @teststep
    def get_id_back_home(self):
        """返回主页面"""
        self.get_student_id()
        self.home.back_up_button()
        if self.home.wait_check_head_img ():
            self.home.click_tab_home ()

    @teststep
    def get_word_by_explain(self, explain):
        """根据翻译从数据库中获取单词
           若获取的单词可能为多个,则与数据库中的单词作比较
        """
        if ';' in explain:  #解释拆分 对于有多个解释的单词，采用;前第一个解释
            explain = explain.split (';')[0]
        prop = explain.split ('. ')[0] + '.'
        exp = explain.split ('. ')[1]
        english = self.mysql.find_word_by_explain (prop, exp)
        all_word_id = self.mysql.find_all_fluency_id(gv.STU_ID) #获取当前用户下所有的单词数据

        id_list = []
        for i in all_word_id:   #将获取元祖形式的word_id 存在在一个数组中
            id_list.append(i[0])

        word = ''      #若由解释获得多个单词，则采用在当前用户数据下的单词
        if len(english) == 1:
            word = english[0][0]
        else:
           for j in english:
               word_id = self.mysql.find_id_by_word(j[0])
               if word_id in id_list:
                    word = j[0]
                    break
        return word

    @teststep
    def get_change_date(self, num):
        """为数据库提供修改日期"""
        now = datetime.datetime.now ()
        word_date = (now + datetime.timedelta (days=-num)).strftime ("%Y-%m-%d %H:%M:%S")
        record_date = (now + datetime.timedelta (days=-2)).strftime ("%Y-%m-%d %H:%M:%S")
        print('单词时间：',word_date)
        print('去重时间：',record_date)
        return word_date, record_date


    @teststep
    def change_word_date(self):
        phone = self.get_user_phone ()
        stu_id = self.mysql.find_student_id (phone)
        date = self.get_change_date (gv.TIME_COUNT)  # 获取修改的时间
        gv.STU_ID = stu_id
        print("LEVEL：",gv.LEVEL)
        self.mysql.update_word_date (str (date[0]), stu_id,gv.LEVEL)
        self.mysql.update_word_record (str (date[1]), stu_id)  # 单词去重，更改record的create时间

    @teststep
    def get_all_label_ids(self):
        """获取标签id"""
        label = []
        label_list = self.mysql.find_book_label(gv.STU_ID)
        for lab in label_list:
            label.append(lab[0])
        label_ids = list(set(label))
        label_ids.sort(key=label.index)
        return label_ids

    @teststep
    def get_label_name(self,label_id):
        """获取标签名称"""
        name = self.mysql.find_label_name(label_id)
        return name

    @teststep
    def get_words_count(self,label_id):
        """获取单词总数 与一轮 三轮单词数"""
        result = self.mysql.find_word_by_label(gv.STU_ID,label_id)
        first_count = []
        third_count = []
        for i in range(len(result)):
            if result[i][1] >= 1:
                first_count.append(i)
            if result[i][1] >= 3:
                third_count.append(i)
        return len(first_count),len(third_count),len(result)


    @teststep
    def get_star_words(self):
        """获取标星单词"""
        star_list = []
        star_ids = self.mysql.find_star_word_id(gv.STU_ID)
        for i in range(len(star_ids)):
            star_word = self.mysql.find_word_by_id(star_ids[i])
            star_list.append(star_word)
        return star_list

    @teststep
    def get_familiar_words(self):
        """获取标熟单词"""
        familiar_list = []
        familiar_ids = self.mysql.find_familiar_word_id(gv.STU_ID)
        for i in range(len(familiar_ids)):
            star_word = self.mysql.find_word_by_id(familiar_ids[i])
            familiar_list.append(star_word)
        return familiar_list

    @teststep
    def get_word_level(self,word):
        """获取单词的熟练度"""
        level = self.mysql.find_word_level(gv.STU_ID,word)
        return int(level)

    @teststep
    def change_play_times(self,time):
        """更改练习次数"""
        self.mysql.update_play_times(gv.STU_ID,time)

    @teststep
    def change_today_word_count(self, count):
        """更改今日练习词数"""
        self.mysql.update_today_word_count(gv.STU_ID,count)

    @teststep
    def change_today_new_count(self, count):
        """更改今日新词数"""
        self.mysql.update_today_new_count (gv.STU_ID, count)

    @teststep
    def delete_all_star(self):
        """删除所有star数据"""
        self.mysql.delete_all_star(gv.STU_ID)

    @teststep
    def delete_all_score(self):
        """删除所有score数据"""
        self.mysql.delete_all_score(gv.STU_ID)


    @teststep
    def delete_all_word(self):
        """删除用户所有单词数据"""
        self.mysql.delete_all_word(gv.STU_ID)

    @teststep
    def delete_all_record(self):
        """删除所有去重记录"""
        self.mysql.delete_all_record(gv.STU_ID)

    def delete_all_fluency_flag(self):
        """删除所有标星标熟记录"""
        self.mysql.delete_fluency_flag(gv.STU_ID)

    @teststep
    def get_need_recite_count(self,level):
        """获取需要复习的单词数"""
        words = self.mysql.find_range_fluency(gv.STU_ID, level)
        return len(words)

    @teststep
    def change_new_word_level(self,before,after):
        """更改熟练度"""
        self.mysql.update_level_zero(gv.STU_ID,before,after)

    @teststep
    def get_different_level_words(self,level):
        """获取新词个数"""
        words = self.mysql.find_word_different_level(gv.STU_ID,level)
        return len(words)
