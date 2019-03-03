from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ()

class user(models.Model):
    username = models.CharField('用户名', max_length=100)
    pass_wd = models.CharField('密码', max_length=60)
    def __str__(self):
        return self.username

class per(models.Model):
    user = models.OneToOneField(user)
    use_name = models.TextField('用户昵称', max_length=100)
    t_name = models.TextField('真实姓名', max_length=100)
    qq = models.TextField('QQ', max_length=100)
    email = models.EmailField('用户邮箱')
    phone = models.TextField('用户电话',max_length=20)
    add = models.TextField('用户地址', max_length=100)
    information = models.TextField('用户简介',max_length=1000)
    img = models.ImageField(upload_to='img',blank=True)
    def __str__(self):
        return self.use_name

class com(models.Model):
    user = models.OneToOneField(user)
    use_name = models.TextField('企业名称',max_length=100)
    t_name = models.TextField('真实姓名', max_length=100)
    qq = models.TextField('QQ', max_length=100)
    email = models.EmailField('联系邮箱')
    phone = models.TextField('联系电话',max_length=20)
    count = models.TextField('供应数量', max_length=100)
    add = models.TextField('企业地址', max_length=100)
    def __str__(self):
        return self.use_name
# Create your models here.
