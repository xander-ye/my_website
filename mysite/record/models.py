# coding=utf-8

from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models, utils
import os
from uuid import uuid4
from django.utils.encoding import python_2_unicode_compatible




def pic_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('records/', filename)





@python_2_unicode_compatible
class Record(models.Model):
    class Meta:
        verbose_name='记录'
        verbose_name_plural='我的流水账'

    TYPE_CHOICES = (
        ('type_video', '视频'),
        ('type_phtoto', '摄影'),
        ('type_travel', '游记'),
        ('type_program', '编程'),
    )
    record_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='类型',blank=False)
    title=models.CharField(max_length=100,verbose_name='标题')
    banner=models.ImageField(
        upload_to=pic_upload_path,
        verbose_name='封面',
        null=True,
        blank=True,
    )
    article_description=models.TextField(
        verbose_name='概览',
        null=True,
        blank=True,
    )
    content = RichTextUploadingField(
        verbose_name='正文',
        null=True,
        blank=True,
    )
    video = models.CharField(
        max_length=200,
        verbose_name='视频链接',
        null=True,
        blank=True,
    )
    date = models.DateField(verbose_name='发布日期')

    def __str__(self):
        return self.title

    def get_banner_url(self):
        return self.banner.url if self.banner else ''

    def get_record_imgs(self):
        #all_list =RecordImg.objects.all().order_by('-date')
        imgs=self.imgs_set.all()
        json_list=[]
        for img in imgs:
            img_json=img.to_json()
            json_list.append(img_json)
        return json_list



    def to_json(self):
        this={
            'id':self.pk,
            'record_type':self.record_type,
            'title':self.title,
            'banner':self.get_banner_url(),
            'article_description':self.article_description,
            'content':self.content,
            'video':self.video,
            'publish_date':self.date,
            'record_imgs':self.get_record_imgs(),
        }
        return this


@python_2_unicode_compatible
class RecordImg(models.Model):
    record=models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name='imgs_set',
    )
    temp_img=models.ImageField(
        upload_to=pic_upload_path,
        verbose_name='摄影图片',
        null=True,
        blank=True,
    )
    remarks=models.CharField(
        max_length=20,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.temp_img.url if self.temp_img else ''

    def get_img_url(self):
        return self.temp_img.url if self.temp_img else ''

    def to_json(self):
        this={
            'id':self.pk,
            'imgurl':self.get_img_url(),
            'remarks':self.remarks,
        }
        return this