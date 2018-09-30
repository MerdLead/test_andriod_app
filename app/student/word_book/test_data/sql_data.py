#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from conf.decorator import teststeps


class Sql:
    @teststeps
    def add_word(self, eng, exp):  # 数据库添加操作
        return "INSERT INTO word_list(`english`, `explain`) VALUES ('%s', '%s')" % (eng, exp)

    @teststeps
    def get_all_word(self, var='word_list'):
        """获取数据库所有数据"""
        sql = "select * from %s" % var
        return sql

    @teststeps
    def get_word(self, exp, var='word_list'):  # 根据解释查询指定单词
        sql = "SELECT english FROM %s WHERE `explain` = '%s'" % (var, exp)
        return sql

    @teststeps
    def get_explain(self, eng, var='word_list'):  # 根据单词查询指定解释
        sql = "SELECT explain FROM %s WHERE `english` = '%s'" % (var, eng)
        return sql
