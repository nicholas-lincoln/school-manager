# -*- coding: utf-8 -*-
import datetime
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'password', 's_name', 'gender', 'birth', 'phone_number', 'enrolled_class')
        labels = {
            'username': '账号',
            'password': '密码',
            's_name': '姓名',
            'gender': '性别',
            'birth': '出生日期',
            'phone_number': '电话号码',
            'enrolled_class': '所在班级',
        }
        widgets = {
            'birth': forms.DateInput(attrs={
                'type': 'date',
                'max': datetime.date.today().strftime('%Y-%m-%d')  # Set max date to today
            }),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # self.fields['gender'].empty_label = '性别'
        self.fields['gender'].choices = [('', '性别')] + list(self.fields['gender'].choices)[1:]
        self.fields['enrolled_class'].empty_label = '所在班级'
        self.fields['phone_number'].required = False
