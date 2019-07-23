#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午10:51
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from goods import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页
]
