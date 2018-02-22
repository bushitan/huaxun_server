#coding:utf-8
from django.db import models
from api.models.user import *
from meet.lib.util import *
import django.utils.timezone as timezone
from meet.lib.image_save import *
from meet.models import *


###7 图片库
##class ImageLibrary(models.Model):
##    name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
##    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
##    local_path = models.ImageField(u'图标',upload_to='img/')
##    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
##    class Meta:
##        verbose_name_plural = verbose_name = u'6.9 会议图库'
##
##    def __unicode__(self):
##        return '%s' % (self.id)
##
##    def save(self):
##        ImageSave(self)
###8 文章库
##class ArticleLibrary(models.Model):
##
##    click_rate = models.IntegerField(u'点击率',default=8965)
##    is_top = models.IntegerField(u'文章置顶',default=NO,choices=IS_TOP.items(),)
##    #封面
##    # cover_image = models.ForeignKey(ImageLibrary, verbose_name=u'选择封面图片',null=True,blank=True)
##    #文章内容
##    title = models.CharField(max_length=100, verbose_name=u'标题')
##    subtitle = models.CharField(max_length=100,verbose_name=u'子标题',default='',null=True,blank=True)
##    #摘要 发布时间
##    summary = models.CharField(max_length=100,verbose_name=u'摘要',default='',null=True,blank=True)
##    source = models.CharField(max_length=100,verbose_name=u'来源',default='',null=True,blank=True)
##    #正文
##    content = models.TextField(verbose_name=u'正文',null=True,blank=True)
##    content_width = models.IntegerField(verbose_name=u'正文显示宽度',default=750,null=True,blank=True)
##    is_show = models.IntegerField(u'是否显示文章',default=YES,choices=IS_SHOW.items(),)
##
##    issue_time = models.DateTimeField(u'文章发布时间', default = timezone.now)
##    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
##
##    #音频
##    audio_src = models.CharField(max_length=1000,verbose_name=u'音频地址(Url)',null=True,blank=True)
##    audio_poster = models.CharField(max_length=500,verbose_name=u'音频封面图(Url)',null=True,blank=True)
##    audio_name = models.CharField(max_length=100,verbose_name=u'音频名称',null=True,blank=True)
##    audio_author = models.CharField(max_length=100,verbose_name=u'音频作者',null=True,blank=True)
##
##    #视频
##    video_src = models.CharField(max_length=1000,verbose_name=u'视频地址(Url)',null=True,blank=True)
##
##    #地址，
##    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
##    work_date = models.CharField(max_length=200, verbose_name=u'工作时间',default="",null=True,blank=True)
##    phone = models.CharField(max_length=40, verbose_name=u'电话',default="",null=True,blank=True)
##    introduction = models.CharField(max_length=500, verbose_name=u'简介',default="",null=True,blank=True)
##    class Meta:
##        verbose_name_plural = verbose_name = u'6.4 内容'
##        ordering = ['-issue_time', '-is_top']
##        # ordering = ['rank', '-is_top', '-pub_time', '-create_time']
##
##    def __unicode__(self):
##            return self.title
##
##
##
### 小程序
####class Lite(models.Model):
####    name =  models.CharField(max_length=100, verbose_name=u'小程序名称',default="",null=True,blank=True)
####    app_id =  models.CharField(max_length=100, verbose_name=u'AppID',default="",null=True,blank=True)
####    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
###5 专栏
##class Page(models.Model):
####    lite = models.ForeignKey(ImageLibrary, verbose_name=u'所属小程序',null=True,blank=True)
##    name =  models.CharField(max_length=32, verbose_name=u'前台页面名称',default="",null=True,blank=True)
##    name_admin =  models.CharField(max_length=32, verbose_name=u'后台页面名称',default="",null=True,blank=True)
##    mark =  models.IntegerField(verbose_name=u'页面对应的标记',default=0) #每个页面对应的标记
##    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
##    # 点击链接的文章
##    class Meta:
##        verbose_name_plural = verbose_name = u'6.2 小程序模块'
##        ordering = ['-create_time']
##    def __unicode__(self):
##        return '%s' % (self.name_admin)
##
### 1 会议
##class Meet(models.Model):
##    father =  models.ForeignKey('Meet',verbose_name=u'父会议',null=True,blank=True)
##    name =  models.CharField(max_length=100, verbose_name=u'会议名称',null=True,blank=True)
##    des = models.TextField( verbose_name=u'描述',null=True,blank=True)
##    status = models.IntegerField(u'会务状态',default=MEET_PREPARE,choices=MEET_STATUS.items(),)
##    serial =  models.IntegerField(verbose_name=u'排序',default=0)
##    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
##    latitude = models.FloatField(verbose_name=u'精度',default=0)
##    longitude = models.FloatField(verbose_name=u'维度',default=0)
##    # issue_time = models.DateTimeField(u'发布时间', default = timezone.now)
##    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
##    class Meta:
##        verbose_name_plural = verbose_name = u'6.1 会议召开'
##        ordering = ['-serial']
##
##    def __unicode__(self):
##        return '%s' % (self.name)

#3  嘉宾
##class Guest(models.Model):
##    name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
##    logo_image = models.ForeignKey(ImageLibrary, verbose_name=u'商圈图片',null=True,blank=True)
##    company = models.CharField(max_length=40, verbose_name=u'公司',default="",null=True,blank=True)
##    introduction = models.CharField(max_length=500, verbose_name=u'个人简介',default="",null=True,blank=True)
##    meet =  models.ManyToManyField(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
##    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
##    class Meta:
##        verbose_name_plural = verbose_name = u'嘉宾'
##        ordering = ['-create_time']
##    def __unicode__(self):
##        return '%s' % (self.name)

#会与者
class Attendee(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
    company =  models.CharField(max_length=100, verbose_name=u'公司',default="",null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'电话',default="",null=True,blank=True)
    remark = models.CharField(max_length=100, verbose_name=u'备注',null=True,blank=True)
    order = models.ForeignKey('Order', verbose_name=u'所属订单',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.5.1 参会人员表'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.name)

#6 会议账单
class Bill(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'小程序-项目名称',default="",null=True,blank=True)
    name_admin =  models.CharField(max_length=100, verbose_name=u'后台-项目名称',default="",null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'描述',null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    unit_price = models.FloatField(u'单价',default=0)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'6.6 会议支付项目'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.name_admin)


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
    user = models.ForeignKey(User, verbose_name=u'用户名称',related_name='discount_user',)
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
    user = models.ForeignKey(User, verbose_name=u'用户',related_name='order_user',null=True,blank=True) 
    bill = models.ForeignKey(Bill, verbose_name=u'会议支付项目',null=True,blank=True)
    discount = models.ForeignKey(Discount, verbose_name=u'优惠券',null=True,blank=True)
    is_pay = models.IntegerField(u'支付状态',default=NO,choices=ORDER_PAY.items(),) 
    num = models.IntegerField(u'数量',default=0)
    total_price = models.FloatField(u'总价',default=0)
    remark = models.CharField(max_length=100, verbose_name=u'备注',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'6.5 订单'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)

###5 封面
##class Cover(models.Model):
##    name =  models.CharField(max_length=100, verbose_name=u'封面名称',default="",null=True,blank=True)
##    cover_image = models.ForeignKey(ImageLibrary, verbose_name=u'商圈图片',related_name='cover_image',null=True,blank=True)
##    page =  models.ForeignKey(Page,verbose_name=u'所属页面',null=True,blank=True) #所属会议
##    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
##    article =  models.ForeignKey(ArticleLibrary,verbose_name=u'点击文章',null=True,blank=True) #所属会议
##
##    style = models.IntegerField(u'封面类别',default=SPOT_CITY,choices=SPOT_TYPE.items(),)  #地点类型
##    # 会议使用
##    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
##    summary = models.CharField(max_length=100, verbose_name=u'摘要',null=True,blank=True)
##    des = models.CharField(max_length=100, verbose_name=u'详细描述',null=True,blank=True)
##    footer = models.CharField(max_length=100, verbose_name=u'时间',null=True,blank=True)
##    start_time = models.DateTimeField(u'开始时间', default = timezone.now)
##    end_time = models.DateTimeField(u'开始时间', default = timezone.now)
##
####    嘉宾
##    name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
##    logo_image = models.ForeignKey(ImageLibrary, verbose_name=u'嘉宾头像',related_name='logo_image',null=True,blank=True)
##    company = models.CharField(max_length=40, verbose_name=u'公司',default="",null=True,blank=True)
##    introduction = models.CharField(max_length=500, verbose_name=u'个人简介',default="",null=True,blank=True)
##    
##
##    
##    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
##    # 点击链接的文章
##    class Meta:
##        verbose_name_plural = verbose_name = u'6.3 封面'
##        ordering = ['-create_time']
##
##    def __unicode__(self):
##        return '%s' % (self.name)











