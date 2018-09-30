import pymysql
from conf.decorator import teststeps


class MysqlWord:

    @teststeps
    def __init__(self):
        self.db = pymysql.connect("localhost","root","root","word")
        self.cursor = self.db.cursor()

    @teststeps
    def add_word(self,eng,exp):     #数据库添加操作
        sql = "INSERT INTO word_list(`english`, `explain`) VALUES ('%s', '%s')"%(eng,exp)
        try:
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

        self.db.close()

    @teststeps
    def get_word(self,exp):  #根据翻译查询指定单词
        sql = "SELECT english FROM word_list WHERE `explain` = '%s'"% exp
        result = 0
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except:
            print("ERROR！！无法查询到此单词！！")
        self.db.close()
        return result

    @teststeps
    def get_all_word(self):
        sql = "select * from word_list"
        results = 0
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        self.db.close()
        return  results