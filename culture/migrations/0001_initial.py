# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='com',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_name', models.TextField(max_length=100, verbose_name='企业名称')),
                ('email', models.EmailField(max_length=254, verbose_name='联系邮箱')),
                ('phone', models.TextField(max_length=20, verbose_name='联系电话')),
                ('count', models.TextField(max_length=100, verbose_name='供应数量')),
                ('add', models.TextField(max_length=100, verbose_name='企业地址')),
            ],
        ),
        migrations.CreateModel(
            name='per',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_name', models.TextField(max_length=100, verbose_name='用户昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('phone', models.TextField(max_length=20, verbose_name='用户电话')),
                ('add', models.TextField(max_length=100, verbose_name='用户地址')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('pass_wd', models.CharField(max_length=60, verbose_name='密码')),
            ],
        ),
        migrations.AddField(
            model_name='per',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='culture.user'),
        ),
        migrations.AddField(
            model_name='com',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='culture.user'),
        ),
    ]