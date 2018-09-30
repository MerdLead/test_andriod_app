#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
from conf.base_page import BasePage
from conf.decorator import teststep


class GetAttribute(BasePage):
    """获取元素属性"""

    @teststep
    def selected(self, var):
        """元素 selected属性值"""
        value = var.get_attribute('selected')
        return value

    @teststep
    def checked(self, var):
        """元素 checked属性值"""
        value = var.get_attribute('checked')
        return value

    @teststep
    def enabled(self, var):
        """元素 enabled属性值"""
        value = var.get_attribute('enabled')
        return value

    @teststep
    def description(self, var):
        """元素 content_description属性值"""
        value = var.get_attribute('contentDescription')
        return value
