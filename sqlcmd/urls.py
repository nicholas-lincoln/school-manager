# -*- coding: utf-8 -*-
from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_form, name='user_insert'),  # get和post请求，插入用户
    path('<int:id>/', views.user_form, name='user_update'),  # get和post请求，更新用户
    path('delete/<int:id>/', views.user_delete, name='user_delete'),    # 删除用户
    path('list/', views.user_list, name='user_list')    # get请求,显示所有用户
]
