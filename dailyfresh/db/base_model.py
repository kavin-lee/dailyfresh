#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午10:53
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : base_models.py
# @Software: PyCharm
from django.db import models


class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        #说明是一个抽象的模型类
        abstract=True