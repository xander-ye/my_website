# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20160915_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='video',
            field=models.TextField(blank=True, default='', verbose_name='\u89c6\u9891\u94fe\u63a5'),
        ),
    ]
