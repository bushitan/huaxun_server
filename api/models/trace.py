#coding:utf-8
from django.db import models
# from order.models import *

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

ARTICLE_SHOW = {
    1:u"显示",
    0:u"隐藏",
}
PAY_MODE = {
    0: u"普通用户",
    1: u'黄金会员',
    2: u'超级会员',
    3: u"点播付费",
}


CREATE_TYPE = {
    0:u"人工",
    1:u"系统",
}


MODEL_ACTION = {
    0:u"更改",
    1:u"增加",
    2:u"删除",
}

class HistoryUserRole(models.Model):
    action = models.IntegerField(u'开通方式',default=0,choices=MODEL_ACTION.items())
    # trace_user_role = models.ForeignKey(Order, verbose_name=u'用户名称',null=True,blank=True)
    user = models.ForeignKey('User', verbose_name=u'用户名称',null=True,blank=True)
    role =  models.ForeignKey('Role', verbose_name=u'角色名称',null=True,blank=True)
    create_type = models.IntegerField(u'开通方式',default=0,choices=CREATE_TYPE.items())
    start_time = models.DateTimeField(u'合同开始时间', null=True,blank=True)
    end_time = models.DateTimeField(u'合同结束时间', null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', null=True,blank=True)
    history_create_time =  models.DateTimeField(u'历史记录创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'4.1 合同变更记录'
        ordering = ['-history_create_time']
        app_label = 'api'

def list_all_member(self):
    for name,value in vars(self).items():
        print('%s=%s'%(name,value))


# class RelArticleTag(models.Model):
#     tag = models.ForeignKey(Tag, verbose_name=u'目录')
#     article = models.ForeignKey(Article, verbose_name=u'文章')
#     create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
#     class Meta:
#         verbose_name_plural = verbose_name = u'文章分类'
#         app_label = string_with_title('api', u"API接口")


#浏览记录  or  收藏
class RelArticleUser(models.Model):
    user = models.ForeignKey('User', verbose_name=u'用户')
    article = models.ForeignKey('Article', verbose_name=u'文章')
    create_time = models.DateTimeField(u'创建时间', auto_now=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'4.2 浏览记录'
        ordering = ['-create_time']
        app_label = 'api'


LEVEL_MODE = {
    0: u"普通用户",
    1: u'黄金会员',
    2: u'超级会员',
    # 3: u"点播付费",
}
#点播支付记录
class PayBill(models.Model):
    user = models.ForeignKey('User', verbose_name=u'用户',null=True,blank=True)
    # pay_mode = models.IntegerField(u'会员等级',default=0,choices=LEVEL_MODE.items(),)
    price = models.FloatField(verbose_name=u'支付单价',null=True,blank=True)
    # remain_num = models.IntegerField(verbose_name=u'剩余播放次数',null=True,blank=True)
    # start_time = models.DateTimeField(u'合同开始时间', null=True,blank=True)
    # end_time = models.DateTimeField(u'合同结束时间', null=True,blank=True)
    create_time = models.DateTimeField(u'订单创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'4.3 支付记录'
        ordering = ['-create_time']
        app_label = 'api'





# from django.db import models

# Create your models here.
# class Test(models.Model):
#     name = models.CharField(max_length=20)
#
# class Test_Tag(models.Model):
#     # contact = models.ForeignKey(Test_Contact)
#     name    = models.CharField(max_length=50)
#     def __unicode__(self):
#         return self.name
#
# class Test_Contact(models.Model):
#     name   = models.CharField(max_length=200)
#     age    = models.IntegerField(default=0)
#     email  = models.EmailField()
#     contact_many = models.ManyToManyField(Test_Tag)
#     def __unicode__(self):
#         return self.name
#
