#coding:utf-8
from django.db import models
from api.models.user import *
from meet.lib.util import *
import django.utils.timezone as timezone
from meet.lib.image_save import *
IMAGE_COVER = 1
IMAGE_LOGO = 2
IMAGE_STYLE = {
    IMAGE_COVER:u"封面",
    IMAGE_LOGO:u"头像",
}
#7 图片库
class ImageLibrary(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
    style = models.IntegerField(u'类别',default=IMAGE_COVER,choices=IMAGE_STYLE.items(),)
    local_path = models.ImageField(u'图标',upload_to='img/',default='')
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.2 会议图库'

    def __unicode__(self):
        return '%s' % (self.id)

    def save(self):
        ImageSave(self,ImageLibrary)

#8 文章库
class ArticleLibrary(models.Model):

    style = models.IntegerField(u'文章类别',default=ARTICLE_STYLE_TEXT,choices=ARTICLE_STYLE.items(),)
    # style =  models.ForeignKey(ArticleStyle,verbose_name=u'页面类别',null=True,blank=True) #所属会议
    is_show = models.IntegerField(u'是否显示文章',default=YES,choices=IS_SHOW.items(),)
    click_rate = models.IntegerField(u'点击率',default=8965)
    is_top = models.IntegerField(u'文章置顶',default=NO,choices=IS_TOP.items(),)
    #封面
    # cover_image = models.ForeignKey(ImageLibrary, verbose_name=u'选择封面图片',null=True,blank=True)
    #文章内容
    title = models.CharField(max_length=100, verbose_name=u'标题')
    subtitle = models.CharField(max_length=100,verbose_name=u'子标题',default='',null=True,blank=True)
    #摘要 发布时间
    summary = models.CharField(max_length=100,verbose_name=u'摘要',default='',null=True,blank=True)
    source = models.CharField(max_length=100,verbose_name=u'来源',default='',null=True,blank=True)
    #正文
    content = models.TextField(verbose_name=u'正文',null=True,blank=True)
    content_width = models.IntegerField(verbose_name=u'正文显示宽度',default=750,null=True,blank=True)

    issue_time = models.DateTimeField(u'文章发布时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    #音频
    audio_src = models.CharField(max_length=1000,verbose_name=u'音频地址(Url)',null=True,blank=True)
    audio_poster = models.CharField(max_length=500,verbose_name=u'音频封面图(Url)',null=True,blank=True)
    audio_name = models.CharField(max_length=100,verbose_name=u'音频名称',null=True,blank=True)
    audio_author = models.CharField(max_length=100,verbose_name=u'音频作者',null=True,blank=True)

    #视频
    video_src = models.CharField(max_length=1000,verbose_name=u'视频地址(Url)',null=True,blank=True)

    #地址，IS_SHOW
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    work_date = models.CharField(max_length=200, verbose_name=u'工作时间',default="",null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'电话',default="",null=True,blank=True)
    introduction = models.CharField(max_length=500, verbose_name=u'简介',default="",null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'6.4 文章'
        ordering = ['-issue_time', '-is_top']
        # ordering = ['rank', '-is_top', '-pub_time', '-create_time']

    def __unicode__(self):
            return self.title



# 1 主会议
class Meet(models.Model):
    style = models.IntegerField(u'类别',default=MEET_AGENDA,choices=MEET_STYLE.items(),)
    name =  models.CharField(max_length=100, verbose_name=u'会议名称',null=True,blank=True)
    father =  models.ForeignKey('self',verbose_name=u'父会议',null=True,blank=True)
    des = models.TextField( verbose_name=u'描述',null=True,blank=True)
    status = models.IntegerField(u'会务状态',default=MEET_PREPARE,choices=MEET_STATUS.items(),)
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    latitude = models.FloatField(verbose_name=u'精度',default=0)
    longitude = models.FloatField(verbose_name=u'维度',default=0)
    # issue_time = models.DateTimeField(u'发布时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.1 主会议'
        ordering = ['-serial']

    def __unicode__(self):
        return '%s' % (self.name)


# 日程
class Swiper(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',default="",null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    article =  models.ForeignKey(ArticleLibrary,verbose_name=u'点击文章',null=True,blank=True) #所属会议

    style = models.IntegerField(u'会务状态',default=MEET_SWIPER_AGENDA,choices=MEET_SWIPER_STYLE.items(),)
    cover_image = models.ForeignKey(ImageLibrary, verbose_name=u'封面图片',null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    summary = models.CharField(max_length=100, verbose_name=u'摘要',null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'详细描述',null=True,blank=True)
    footer = models.CharField(max_length=100, verbose_name=u'页脚',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.2 轮播图'
        ordering = ['-create_time']

    def __unicode__(self):
        return '%s' % (self.name)


# 日程
class Agenda(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',default="",null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    article =  models.ForeignKey(ArticleLibrary,verbose_name=u'点击文章',null=True,blank=True) #所属会议

    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    summary = models.CharField(max_length=100, verbose_name=u'摘要',null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'详细描述',null=True,blank=True)
    footer = models.CharField(max_length=100, verbose_name=u'页脚',null=True,blank=True)
    start_time = models.DateTimeField(u'开始时间', default = timezone.now)
    end_time = models.DateTimeField(u'开始时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.1.1 目录 -- 日程'
        ordering = ['-create_time']

    def __unicode__(self):
        return '%s' % (self.name)

#  嘉宾
class Guest(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    article =  models.ForeignKey(ArticleLibrary,verbose_name=u'点击文章',null=True,blank=True) #所属会议
    logo_image = models.ForeignKey(ImageLibrary, verbose_name=u'嘉宾头像',null=True,blank=True)
    company = models.CharField(max_length=40, verbose_name=u'公司',default="",null=True,blank=True)
    introduction = models.CharField(max_length=2000, verbose_name=u'个人简介',default="",null=True,blank=True)

    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.1.2 目录 -- 嘉宾'
        ordering = ['-create_time']

    def __unicode__(self):
        return '%s' % (self.name)


# 日程
class News(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',default="",null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    article =  models.ForeignKey(ArticleLibrary,verbose_name=u'点击文章',null=True,blank=True) #所属会议

    cover_image = models.ForeignKey(ImageLibrary, verbose_name=u'封面图片',null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    summary = models.CharField(max_length=100, verbose_name=u'摘要',null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'详细描述',null=True,blank=True)
    footer = models.CharField(max_length=100, verbose_name=u'页脚',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.1.3 目录 -- 新闻'
        ordering = ['-create_time']

    def __unicode__(self):
        return '%s' % (self.name)

# 日程
class Spot(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',default="",null=True,blank=True)
    meet =  models.ForeignKey(Meet,verbose_name=u'所属会议',null=True,blank=True) #所属会议
    article =  models.ForeignKey(ArticleLibrary,verbose_name=u'点击文章',null=True,blank=True) #所属会议

    cover_image = models.ForeignKey(ImageLibrary, verbose_name=u'封面图片',null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    summary = models.CharField(max_length=100, verbose_name=u'摘要',null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'详细描述',null=True,blank=True)
    footer = models.CharField(max_length=100, verbose_name=u'页脚',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'6.1.4 目录 -- 景点'
        ordering = ['-create_time']

    def __unicode__(self):
        return '%s' % (self.name)





# 小程序
##class Lite(models.Model):
##    name =  models.CharField(max_length=100, verbose_name=u'小程序名称',default="",null=True,blank=True)
##    app_id =  models.CharField(max_length=100, verbose_name=u'AppID',default="",null=True,blank=True)
##    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
##TextField(verbose_name=u'正文',null=True,blank=True)



