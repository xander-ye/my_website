# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-01 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_auto_20161101_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactdata',
            options={'verbose_name': '\u5ba2\u6237', 'verbose_name_plural': '\u5ba2\u6237'},
        ),
        migrations.AlterModelOptions(
            name='recordimg',
            options={'verbose_name_plural': '\u56fe\u7247'},
        ),
        migrations.AddField(
            model_name='contactdata',
            name='qq_wechat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f'),
        ),
    ]