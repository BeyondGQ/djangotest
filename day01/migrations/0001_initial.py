# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DJ_User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('sex', models.CharField(default='1', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('last_time', models.DateTimeField(auto_now=True)),
                ('head_img', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户列表',
                'db_table': 'D_USER',
                'ordering': ['create_date'],
            },
        ),
    ]
