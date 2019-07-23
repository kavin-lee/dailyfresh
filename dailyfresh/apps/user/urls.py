#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午10:51
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),  # 注册
    url(r'^register_handle$', views.register_handle, name='register_handle'),  # 注册处理
    # url(r'^register_handle$', views.register_handle, name='register_handle'),#注册处理
]
