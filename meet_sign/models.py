#coding:utf-8
from meet.lib.util import *
from meet.models import *

IS_MALE = {
    YES:u"男",
    NO:u"女",
}
IS_PAYMENT = {
    IS_PAYMENT_FALSE:u"待支付",
    IS_PAYMENT_TRUE:u"已支付",
}
IS_ALIVE = {
    YES:u"激活",
    NO:u"失效",
}
# 会与者
class Attendee(models.Model):
    wx_union_id = models.CharField(max_length=50, verbose_name=u'微信UnionID',null=True,blank=True)
    wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
    session = models.CharField (max_length=128, verbose_name=u'Django的session',null=True,blank=True)
    uuid =  models.CharField(max_length=32, verbose_name=u'uuid标识',null=True,blank=True)

    name =  models.CharField(max_length=100, verbose_name=u'姓名1',default="",null=True,blank=True)
    male =  models.BooleanField( verbose_name=u'性别',default=YES,choices=IS_MALE.items())
    company =  models.CharField(max_length=100, verbose_name=u'企业名称',default="",null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'电话',default="",null=True,blank=True)
    position = models.CharField(max_length=100, verbose_name=u'职务',null=True,blank=True)
    remark = models.CharField(max_length=100, verbose_name=u'备注',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        # app_label = "meet"
        verbose_name_plural = verbose_name = u'6.5.1 参会人员表'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)

# 会议费用
class Cost(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'小程序-项目名称',default="",null=True,blank=True)
    name_admin =  models.CharField(max_length=100, verbose_name=u'后台-项目名称',default="",null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'费用说明',null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    unit_price = models.FloatField(u'单价',default=0)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'6.6 费用'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.name_admin)

class Sign(models.Model):
    attendee = models.ForeignKey(Attendee, verbose_name=u'用户',related_name='order_user',null=True,blank=True)
    cost = models.ForeignKey(Cost, verbose_name=u'会议支付项目',null=True,blank=True)
    is_alive = models.BooleanField( verbose_name=u'是否有效',default=YES,choices=IS_ALIVE.items())
    alive_time = models.DateTimeField(u'有效时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'6.6 参会报名'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)

class DiscountTemplate(models.Model):
    #会员
    name = models.CharField(max_length=100, verbose_name=u'优惠券名称',null=True,blank=True)
    use_condition = models.CharField(max_length=100, verbose_name=u'使用条件',null=True,blank=True)
    use_range = models.CharField(max_length=100, verbose_name=u'使用范围',null=True,blank=True)
    fee = models.FloatField( verbose_name=u'优惠价格',default=5)
    limit_fee = models.FloatField( verbose_name=u'最低使用价格',default=0)  #最低使用价格为0元
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.7 优惠券模板'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        # _id = self.id
        if self.id < 10 :
            _id = "0" + str(self.id)
        else:
            _id = str(self.id)
        return 'T%s : %s' % (_id,self.name)
    
def three_day_hence(): #优惠券默认3天有效期
    return timezone.now() + timezone.timedelta(days=3)

#优惠券
class Discount(models.Model):
    attendee = models.ForeignKey(Attendee, verbose_name=u'用户名称',null=True,blank=True)
    template = models.ForeignKey('DiscountTemplate', verbose_name=u'优惠券类型')
    #1 是否使用
    is_used = models.IntegerField(u'是否使用',default=YES,choices=IS_SHOW.items())
    is_active = models.IntegerField(u'是否作废',default=YES,choices=IS_SHOW.items())
    #2 使用时间
    start_time = models.DateTimeField(u'优惠开始时间', default = timezone.now)
    end_time = models.DateTimeField(u'优惠结束时间', default=three_day_hence )
    #3 使用区域

    create_time = models.DateTimeField(u'优惠券创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.8 优惠券'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        return '%s' % (self.id)


#6 会议订单
class Order(models.Model):
    #订单是否有效
    is_alive = models.IntegerField(u'订单状态',default=YES,choices=IS_ALIVE.items())
    #订单支付状态
    is_pay = models.IntegerField(u'支付状态',default=NO,choices=ORDER_PAY.items(),)
    #微信支付部分
    wx_out_trade_no = models.CharField(max_length=32, verbose_name=u'微信_商户订单号',null=True,blank=True)

    sign = models.ForeignKey(Sign, verbose_name=u'参会报名',null=True,blank=True)
    discount = models.ForeignKey(Discount, verbose_name=u'优惠券',null=True,blank=True)
    # num = models.IntegerField(u'数量',default=0)
    # total_price = models.FloatField(u'总价',default=0)
    origin_price = models.FloatField(u'原始价格',default=0)
    pay_price = models.FloatField(u'支付价格',default=0)
    remark = models.CharField(max_length=100, verbose_name=u'备注',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'6.5 订单'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)












