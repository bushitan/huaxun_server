#coding:utf-8
from django.db import models
from api.models.user import *
from api.lib.util import *
from api.models.article import *
import datetime
import os


IS_BUY = {
    YES:u"买入",
    NO:u"卖出",
}


#文章标签
class Match(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户名称',null=True,blank=True)
    tag = models.ForeignKey(Tag,verbose_name=u'标签',null=True,blank=True)
    is_buy = models.IntegerField(u'买入/卖出',default=YES,choices=IS_BUY.items(),)
    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    content = models.TextField(verbose_name=u'简讯内容',null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    issue_time = models.DateTimeField(u'文章发布时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'供求信息'
        # app_label = 'api'
        ordering = ['-issue_time']
    def __unicode__(self):
        return '%s' % (self.title)
