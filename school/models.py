
from django.db import models

# 性别选择
GENDER_CHOICES = [
    ('男', '男'),
    ('女', '女'),
]


### 1. Student Model ###
class Student(models.Model):
    s_name = models.CharField(max_length=100, verbose_name="学生姓名")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="性别")
    birth = models.DateField(verbose_name="出生年月")
    enrolled_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='students',
                                       verbose_name="所在班级")
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    phone_number = models.CharField(max_length=15, verbose_name="电话号码", blank=True, null=True)

    def __str__(self):
        return self.s_name, self.gender, self.enrolled_class, self.birth


### 2. Teacher Model ###
class Teacher(models.Model):
    t_name = models.CharField(max_length=100, verbose_name="老师姓名")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="性别")
    subject = models.CharField(max_length=100, verbose_name="学科")
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    phone_number = models.CharField(max_length=15, verbose_name="电话号码", blank=True, null=True)

    def __str__(self):
        return self.t_name


### 3. Course Model ###
class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="学科")
    description = models.TextField(verbose_name="课程描述", blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses', verbose_name="教课老师")

    def __str__(self):
        return self.name


### 4. Class Model ###
class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name="班级名称")
    grade = models.IntegerField(verbose_name="年纪")
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='class_teacher', verbose_name="课堂老师")
    courses = models.ManyToManyField(Course, related_name='classes', verbose_name="学科")

    def __str__(self):
        return f" {self.name} - {self.grade} 班"
