# -*- coding: utf-8 -*-
from django.urls import path
from . import views
urlpatterns = [
    path('', views.student_form, name='student_insert'),  # get和post请求，插入用户
    path('<int:id>/', views.student_form, name='student_update'),  # get和post请求，更新用户
    path('delete/<int:id>/', views.student_delete, name='student_delete'),    # 删除用户
    path('list/', views.student_list, name='student_list')    # get请求,显示所有用户
]
