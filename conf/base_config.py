#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI


class GetVariable (object):
    """参数化文档"""

    REPORT_ROOT = 'storges/test_report'  # 测试报告存放路径

    # 以下为 devices.py 配置信息
    PACKAGE = '../student_debug_1.2.7.apk'
    PLATFORM_VER = '5.1.1'

    # case统计 配置信息
    CASE_PATH = 'app/student/word_book/test_cases'
    CASE_PATTERN = 'test001*.py'

    # 以下为 appium_server.py 配置信息
    CMD = "appium -a 127.0.0.1 -p %s -bp 4728 --no-reset"
    SERVER_URL = 'http://127.0.0.1:%s/wd/hub/status'
    SERVER_LOG = 'appium_server_port_%s.log'
    KILL = 'taskkill /PID %d /F'

    # 做题情况统计 Excel表格存放路径
    EXCEL_PATH = 'storges/test_report/games_result_info.xlsx'

    # 学生的ID
    STU_ID = 0
    # 需要测试的单词熟练度
    LEVEL = 1
    # 需改动的时间数
    TIME_COUNT = 1
    # 年级
    GRADE = '四年级'
