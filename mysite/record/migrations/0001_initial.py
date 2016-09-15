# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import record.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('banner', models.ImageField(upload_to=record.models.pic_upload_path, verbose_name='\u9876\u90e8\u5c01\u9762')),
                ('article_description', models.CharField(max_length=200, verbose_name='\u5168\u6587\u6982\u89c8')),
            ],
            options={
                'verbose_name': '\u8bb0\u5f55',
            },
        ),
    ]