# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-01 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_auto_20161101_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdata',
            name='qq_wechat',
        ),
    ]
