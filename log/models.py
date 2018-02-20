#coding:utf-8
from django.db import models
from api.models.user import *
from api.models.article import *
from api.lib.util import *
import datetime
import os

IS_READ = {
    YES:u"已浏览",
    NO:u"待付费",
}
#文章标签
class Article_Click(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户名称',null=True,blank=True)
    article = models.ForeignKey(Article, verbose_name=u'点击文章',null=True,blank=True)
    is_read = models.IntegerField(u'已浏览/待付费',default=YES,choices=IS_READ.items(),)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'文章点击统计'
        # app_label = 'api'
        ordering = ['-create_time']
    # def __unicode__(self):
    #     return '%s' % (self.title)
