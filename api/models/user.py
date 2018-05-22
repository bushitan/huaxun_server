#coding:utf-8
from django.db import models
from api.models.article import *

class string_with_title(str):
    """ 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,
    所以修改str类的title方法就可以实现.
    """
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

# USER_LEVEL = {
#     0: u"普通用户",
#     1: u'黄金会员',
#     2: u'超级会员',
# }
IDENTIFY_STATUS = {
    0: u"未提交",
    1: u'已提交',
    2: u'审核不通过',
    3: u'审核通过',
}
class User(models.Model):
    # models.ImageField()
    logo = models.CharField(max_length=500, verbose_name=u'头像地址',default="",null=True,blank=True)
    # logo = models.ImageField(max_length=150, verbose_name=u'logo链接',null=True,blank=True)
    name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
    nick_name =  models.CharField(max_length=100, verbose_name=u'微信昵称',null=True,blank=True)
    wx_id =  models.CharField(max_length=100, verbose_name=u'微信号',null=True,blank=True)

    wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
    wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
    wx_expires_in = models.FloatField( verbose_name=u'微信SessionKey过期时间',null=True,blank=True)
    session = models.CharField (max_length=128, verbose_name=u'Django的session',null=True,blank=True)
    expires = models.FloatField( verbose_name=u'Django的session过期时间',null=True,blank=True)
    uuid =  models.CharField(max_length=32, verbose_name=u'uuid标识',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)

    # role = models.ForeignKey('Role', verbose_name=u'VIP等级') #
    # level = models.IntegerField(u'会员等级',default=0,choices=USER_LEVEL.items(),null=True,blank=True)
    # vip_time = models.IntegerField(u'剩余天数',null=True,blank=True)

    identify_status = models.IntegerField(u'线下认证状态',default=0,choices=IDENTIFY_STATUS.items(),null=True,blank=True)

    # tag = models.ManyToManyField('Tag',verbose_name=u'所属网站群',null=True,blank=True)

    # roster_logo = models.CharField(max_length=500, verbose_name=u'商圈头像',default="",null=True,blank=True)
    roster_image = models.ForeignKey(ImageMap, verbose_name=u'商圈图片',null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'手机',default="",null=True,blank=True)
    company = models.ForeignKey('Company',verbose_name=u'所在公司',null=True,blank=True)
    introduction = models.CharField(max_length=500, verbose_name=u'个人简介',default="",null=True,blank=True)
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    latitude = models.FloatField(verbose_name=u'精度',default=0)
    longitude = models.FloatField(verbose_name=u'维度',default=0)

    class Meta:
        verbose_name_plural = verbose_name = u'1.5 用户_基本信息'
        app_label = 'api'
        # app_label = string_with_title(u'api', u"23421接口")

    def __unicode__(self):
        return '%s' % (self.id)

#企业信息
class Company(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    #area = models.ForeignKey(Area, verbose_name=u'区域',related_name='father_tag',null=True,blank=True)
    
    class Meta:
        verbose_name_plural = verbose_name = u'1.6 用户_企业信息'
        app_label = 'api'

    def __unicode__(self):
        return '%s' % (self.name)
