#coding:utf-8
from django.db import models
from api.lib.util import *
from api.models.user import *
from api.models.article import *
import datetime
import os


IS_BUY = {
    YES:u"买入",
    NO:u"卖出",
}

class Area(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',default="",null=True,blank=True)
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    
    class Meta:
        verbose_name_plural = verbose_name = u'3.2 区域'
        ordering = ['-serial']
    def __unicode__(self):
        return '%s' % (self.name)
    

#文章标签
class Roster(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户ID',null=True,blank=True)
    tag = models.ForeignKey(Tag, verbose_name=u'所属网站',related_name='father_tag',null=True,blank=True)
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    
    buy = models.ManyToManyField(Tag, verbose_name=u'求购' ,related_name='buy_tag',null=True,blank=True)
    sell = models.ManyToManyField(Tag, verbose_name=u'供应',related_name='sell_tag',null=True,blank=True)

    area = models.ForeignKey(Area, verbose_name=u'区域',related_name='father_tag',null=True,blank=True)
    
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'3.1 联系人名册'
        app_label = 'roster'
        ordering = ['-serial']
    def __unicode__(self):
        return '%s' % (self.user.name)

