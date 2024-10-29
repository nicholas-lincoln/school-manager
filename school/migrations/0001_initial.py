# Generated by Django 5.1.1 on 2024-09-30 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='学科')),
                ('description', models.TextField(blank=True, null=True, verbose_name='课程描述')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=100, verbose_name='老师姓名')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='性别')),
                ('subject', models.CharField(max_length=100, verbose_name='学科')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='电话号码')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='班级名称')),
                ('grade', models.IntegerField(verbose_name='年纪')),
                ('courses', models.ManyToManyField(related_name='classes', to='school.course', verbose_name='学科')),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_teacher', to='school.teacher', verbose_name='课堂老师')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100, verbose_name='学生姓名')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='性别')),
                ('birth', models.DateField(verbose_name='出生年月')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='电话号码')),
                ('enrolled_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.class', verbose_name='所在班级')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='school.teacher', verbose_name='教课老师'),
        ),
    ]
