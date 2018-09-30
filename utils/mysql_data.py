import datetime
import time
import traceback

import pymysql

from conf.decorator import teststeps


class MysqlData:
    @classmethod
    def start_db(cls):
        """启动数据库"""
        cls.db = pymysql.connect ("172.17.0.200", "tmp", "mysql#0056", "b_vanthink_core")
        cls.cursor = cls.db.cursor ()
        print ('启动数据库')

    def close_db(self):
        print ('关闭数据库')
        self.db.close ()

    @teststeps
    def find_word_by_explain(self, prop, exp):
        """根据翻译查找单词"""
        sql = "SELECT wb.vocabulary FROM wordbank AS wb,wordbank_translation AS wt " \
              "WHERE wb.id = wt.wordbank_id AND wt.part_of_speech = '%s' " \
              "AND wt.translation = '%s'" % (prop, exp)
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()

        return result

    def find_student_id(self, phone):  # 根据翻译查询指定单词
        """根据手机号查找自己的student id"""
        sql = "SELECT ua.id FROM user_account AS ua,`user` WHERE ua.user_id = `user`.id and `user`.phone = '%s'" % phone
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchone ()[0]
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()

        return result

    def find_all_fluency_id(self, stu_id):
        """获取所有Id"""
        sql = "SELECT wordbank_id FROM word_student_fluency WHERE student_id = '%s'" % stu_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()

        return result

    def find_fluency_equal_zero(self, stu_id):
        """获取所有Id"""
        sql = "SELECT id FROM word_student_fluency WHERE student_id = '%s' AND fluency_level = '0' " % stu_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_range_fluency(self, stu_id, level):
        """根据student id 查找对应等级的单词的id"""
        sql = "SELECT id FROM word_student_fluency WHERE student_id = '%s' and fluency_level BETWEEN 1 AND '%s'" % (
            stu_id, str (level))
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def update_level_zero(self, stu_id, before, after):
        """变更单词的熟练度"""
        sql = "UPDATE word_student_fluency SET fluency_level = '%s' WHERE student_id= '%s' and fluency_level = '%s'" % (
            after, stu_id, before)
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()

    def update_word_record(self, date, stu_id):
        """根据student_id 对已学单词去重"""
        sql = "UPDATE `word_homework_student_record` SET `created_at` = '%s' WHERE `student_id` = %s" % (
            str (date), stu_id)
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except:
            traceback.print_exc ()
            self.db.rollback ()

    def update_word_date(self, date, student_id, level):
        """根据单词熟练度表的id 更改单词的时间，以让单词处于指定轮次的复习"""
        sql = "UPDATE word_student_fluency SET last_finish_at = '%s' WHERE student_id= '%s' and fluency_level BETWEEN 1 AND '%s'" % (
            str (date), student_id, level)
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception as e:
            traceback.print_exc ()
            self.db.rollback ()

    def find_word_by_sentence_exp(self, exp):
        """根据句子的解释查找单词"""
        sql = "SELECT wordbank.vocabulary FROM wordbank,wordbank_sentence AS ws WHERE wordbank.id = ws.wordbank_id AND ws.`explain` = '%s'" % exp
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchone ()[0]
            self.db.commit ()
        except Exception as e:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_word_by_id(self, word_id):
        """根据id查找单词"""
        sql = "SELECT vocabulary FROM wordbank where id = '%s'" % word_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchone ()[0]
            self.db.commit ()
        except Exception as e:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_id_by_word(self, word):
        """根据单词查询单词id"""
        sql = "SELECT id FROM wordbank where vocabulary= '%s'" % word
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchone ()[0]
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def delete_all_word(self, student_id):
        """删除所有单词"""
        sql = "DELETE FROM word_student_fluency WHERE student_id = '%s'" % student_id
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def find_word_different_level(self, stu_id, level):
        """查找所有新词"""
        sql = "SELECT wordbank_id FROM word_student_fluency WHERE student_id = '%s' AND  fluency_level ='%s'" % (
            stu_id, level)
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def delete_all_record(self, student_id):
        """删除用户去重记录"""
        sql = "DELETE FROM word_homework_student_record WHERE student_id = '%s'" % student_id
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def delete_fluency_flag(self, student_id):
        """删除标星标熟数据"""
        sql = "DELETE FROM word_student_fluency_flag where student_id = '%s'" % student_id
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def find_word_level(self, stu_id, word):
        """查找单词的熟练度"""
        sql = "SELECT fluency_level from wordbank,word_student_fluency as wsf where" \
              " wordbank.id = wsf.wordbank_id AND wsf.student_id = '%s' AND wordbank.vocabulary = '%s'" % (stu_id, word)
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchone ()[0]
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_book_label(self, stu_id):
        """查询标签id"""
        sql = "SELECT label_ids FROM word_student_fluency WHERE student_id = '%s'" % stu_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_label_name(self, label_id):
        """根据标签id 查询标签名称"""
        sql = "SELECT name FROM label WHERE id = '%s'" % label_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchone ()[0]
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_word_by_label(self, stu_id, label_id):
        """查询指定用户下，对应标签的"""
        sql = "SELECT wordbank_id,fluency_level FROM word_student_fluency WHERE student_id = '%s' AND label_ids = '%s'" % (
            stu_id, label_id)
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_star_word_id(self, stu_id):
        """查询标星单词"""
        sql = "SELECT wordbank_id FROM word_student_fluency_flag WHERE student_id ='%s' AND flag = 'star_word'" % stu_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def find_familiar_word_id(self, stu_id):
        """查询标熟单词"""
        sql = "SELECT wordbank_id FROM word_student_fluency_flag WHERE student_id ='%s' AND flag = 'familiar_word'" % stu_id
        result = 0
        try:
            self.cursor.execute (sql)
            result = self.cursor.fetchall ()
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
        return result

    def update_play_times(self, stu_id, times):
        """更改练习次数"""
        sql = "UPDATE user_student_data SET `value` = '%s' WHERE user_account_id = '%s' AND `key` = 'word_play_times'" % (
            times, stu_id)
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def update_today_word_count(self, stu_id, count):
        """更改今日练习个数"""
        sql = "UPDATE user_student_data SET `value` = '%s' WHERE user_account_id = '%s' AND `key` = 'today_word_count'" % (
            count, stu_id)
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def update_today_new_count(self, stu_id, count):
        """更改今日新词个数"""
        sql = "UPDATE user_student_data SET `value` = '%s' WHERE user_account_id = '%s' AND `key` = 'today_new_count'" % (
            count, stu_id)
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def delete_all_star(self, stu_id):
        sql = "DELETE FROM user_student_data where user_account_id = '%s'AND `key` = 'star' " % stu_id
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()

    def delete_all_score(self, stu_id):
        sql = "DELETE FROM user_student_data where user_account_id = '%s'AND `key` = 'score'" % stu_id
        try:
            self.cursor.execute (sql)
            self.db.commit ()
        except Exception:
            traceback.print_exc ()
            self.db.rollback ()
