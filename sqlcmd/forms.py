# -*- coding: utf-8 -*-
from django import forms
from .models import UserModels


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModels
        fields = ('name', 'telephone', 'age', 'position')
        labels = {
            'name': '姓名',
            'age': '年龄',
            'telephone': '电话',
            'position': '暂定',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = '性别'
        self.fields['telephone'].required = False
