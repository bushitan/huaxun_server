#coding:utf-8
from django.db import models
from api.models.trace import *
from api.lib.util import *
from api.models.user import *
from api.models.article import *

ARTICLE_SHOW = {
    1:u"显示",
    0:u"隐藏",
}

CREATE_TYPE = {
    0:u"人工",
    1:u"系统",
}

AGREEMENT_TYPE = {
    AGREEMENT_TYPE_MEMBER:u"会员合同",
    AGREEMENT_TYPE_SINGLE_TIME:u"点播合同",
}


IS_PAYMENT = {
    IS_PAYMENT_FALSE:u"待支付",
    IS_PAYMENT_TRUE:u"已支付",
}
IS_ALIVE = {
    YES:u"激活",
    NO:u"失效",
}
class Order(models.Model):
    renew_order = models.ForeignKey('Order', verbose_name=u'续费的单号',null=True,blank=True)
    user = models.ForeignKey(User, verbose_name=u'用户名称',null=True,blank=True)

    #订单是否有效
    is_alive = models.IntegerField(u'订单状态',default=YES,choices=IS_ALIVE.items())
    #订单支付状态
    is_payment =  models.IntegerField(u'支付状态',default=IS_PAYMENT_FALSE,choices=IS_PAYMENT.items())

    #微信支付部分
    wx_out_trade_no = models.CharField(max_length=32, verbose_name=u'微信_商户订单号',null=True,blank=True)
    #合同标志
    agreement_type = models.IntegerField(u'合同类型',default=AGREEMENT_TYPE_MEMBER,choices=AGREEMENT_TYPE.items())


    #优惠券
    discount = models.ForeignKey('Discount', verbose_name=u'优惠券',null=True,blank=True)
    original_fee = models.FloatField( verbose_name=u'原价',null=True,blank=True)
    payment_fee = models.FloatField( verbose_name=u'支付价',null=True,blank=True)
    create_time = models.DateTimeField(u'订单创建时间', null=True)

     #会员
    tag = models.ForeignKey(Tag, verbose_name=u'网站标签',null=True,blank=True)
    role =  models.ForeignKey(Role, verbose_name=u'角色名称',null=True,blank=True)
    #点播
    article = models.ForeignKey(Article, verbose_name=u'文章',null=True,blank=True)
    play_num = models.IntegerField(verbose_name=u'剩余播放次数',null=True,blank=True)
    #订单服务时间
    start_time = models.DateTimeField(u'合同开始时间', null=True,blank=True)
    end_time = models.DateTimeField(u'合同结束时间', null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'3.1 订单'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        return '%s' % (self.id)

DISCOUNT_IS_USED = {
    DISCOUNT_IS_USED_FALSE : u'未使用',
    DISCOUNT_IS_USED_TRUE  : u'已使用',
}

DISCOUNT_IS_ACTIVE_FALSE = 0
DISCOUNT_IS_ACTIVE_TRUE = 1
DISCOUNT_IS_ACTIVE = {
    DISCOUNT_IS_ACTIVE_FALSE: u'作废',
    DISCOUNT_IS_ACTIVE_TRUE : u'有效',
}

import django.utils.timezone as timezone
import datetime
def three_day_hence(): #优惠券默认3天有效期
    return timezone.now() + timezone.timedelta(days=3)
#优惠券
class Discount(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户名称')
    template = models.ForeignKey('DiscountTemplate', verbose_name=u'优惠券类型')
    #1 是否使用
    is_used = models.IntegerField(u'是否使用',default=DISCOUNT_IS_USED_FALSE,choices=DISCOUNT_IS_USED.items())
    is_active = models.IntegerField(u'是否作废',default=DISCOUNT_IS_ACTIVE_TRUE,choices=DISCOUNT_IS_ACTIVE.items())
    #2 使用时间
    start_time = models.DateTimeField(u'优惠开始时间', default = timezone.now)
    end_time = models.DateTimeField(u'优惠结束时间', default=three_day_hence )
    #3 使用区域

    create_time = models.DateTimeField(u'优惠券创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'3.2 优惠券'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        return '%s' % (self.id)



# DISCOUNT_STYLE = {
#     DISCOUNT_STYLE_MEMBER:u"会员优惠券",
#     DISCOUNT_STYLE_SINGLE_TIME:u"点播惠券",
# }
#优惠券魔板
class DiscountTemplate(models.Model):
    #会员
    name = models.CharField(max_length=100, verbose_name=u'优惠券名称',null=True,blank=True)
    use_condition = models.CharField(max_length=100, verbose_name=u'使用条件',null=True,blank=True)
    use_range = models.CharField(max_length=100, verbose_name=u'使用范围',null=True,blank=True)

    # 会员 or 点播
    agreement_type = models.IntegerField(u'优惠券类别',default=AGREEMENT_TYPE_MEMBER,choices=AGREEMENT_TYPE.items())
    fee = models.FloatField( verbose_name=u'优惠价格',default=5)
    limit_fee = models.FloatField( verbose_name=u'最低使用价格',default=0)  #最低使用价格为0元
    #使用区域
    tag = models.ForeignKey(Tag, verbose_name=u'允许使用网站标签',null=True,blank=True)
    #使用角色
    role =  models.ForeignKey(Role, verbose_name=u'允许使用角色',null=True,blank=True)
    create_time = models.DateTimeField(u'合同创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'3.3 优惠券模板'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        # _id = self.id
        if self.id < 10 :
            _id = "0" + str(self.id)
        else:
            _id = str(self.id)
        return 'T%s : %s' % (_id,self.name)