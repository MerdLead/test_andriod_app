#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI

# 学生名字由2~20位中文、英文组成
name_data = (
    {'name': '', 'count': '0', 'assert': '姓名不能为空'},  # 为空
    {'name': 'q', 'count': '1', 'assert': '名字由2-20位中文、英文组成'},  # 1个字符
    {'name': '万', 'count': '1', 'assert': '名字由2-20位中文、英文组成'},  # 1个字符
    {'name': '万w', 'count': '2'},  # 2个字符
    {'name': 'DE', 'count': '2'},  # 2个字符  区分大小写
    {'name': 'de', 'count': '2'},  # 2个字符  区分大小写
    {'name': 'van在线教育12', 'count': '10'},
    {'name': 'v@在线$123', 'count': '8', 'assert': '名字由2-20位中文、英文组成'},  # 8个字符 特殊字符
    {'name': '以VA2Nthink数字studeVANr', 'count': '21', 'assert': '名字由2-20位中文、英文组成'},   # 多于20个字符 - 21个
    {'name': 'V8AN7K4v     nkstu在线', 'count': '20'},   # 20个字符  5个连续空格
    {'name': 'q18 az12xQ ZS XE19在育', 'count': '20'},  # 20个字符  空格
)
