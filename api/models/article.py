#coding:utf-8
from django.db import models

from api.lib.util import *

from api.lib.qi_niu import *
import datetime
import os
BASE_DIR = os.path.dirname( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

# SHOW = 1
# HIDDEN = 0
# IS_SHOW = {
#     SHOW:u"显示",
#     HIDDEN:u"隐藏",
# }

TOP_TRUE = 1
TOP_FALSE = 0
IS_TOP = {
    YES:u"置顶",
    NO:u"不置顶",
}

PAY_MODE = {
    0: u"普通用户",
    1: u'黄金会员',
    2: u'超级会员',
    3: u"点播付费",
}

#角色表
class Role(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    value = models.IntegerField(u'权限等级',default=1)
    price = models.FloatField(u'会员价格',default=0,null=True,blank=True)
    image_url = models.CharField(max_length=500, verbose_name=u'会员图片',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'1.3 会员角色'
        app_label = 'api'
        ordering = ['-value']
        permissions = (
            ("open_discussion", "Can create a discussion"),
            ("reply_discussion", "Can reply discussion"),
            ("close_discussion", "Can remove a discussion by setting its status as closed"),
        )
    def __unicode__(self):
        return '%s' % (self.name)

IS_SHOW = {
    YES:u"显示",
    NO:u"隐藏",
}
#文章标签
class Tag(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'小程序显示名称',null=True,blank=True)
    name_admin =  models.CharField(max_length=100, verbose_name=u'后台显示名称',null=True,blank=True)
    father =  models.ForeignKey('Tag',verbose_name=u'父目录',null=True,blank=True)
    des = models.TextField( verbose_name=u'描述',null=True,blank=True)
    is_show = models.IntegerField(u'是否在首页显示标签',default=YES,choices=IS_SHOW.items(),)
    
    is_main  = models.IntegerField(u'行业',default=NO,choices=IS_SHOW.items(),)
    is_index  = models.IntegerField(u'首页',default=NO,choices=IS_SHOW.items(),)
    is_match  = models.IntegerField(u'供求',default=NO,choices=IS_SHOW.items(),)
    is_ad  = models.IntegerField(u'广告',default=NO,choices=IS_SHOW.items(),)
    is_swiper  = models.IntegerField(u'轮播',default=NO,choices=IS_SHOW.items(),)
    is_image_map  = models.IntegerField(u'图库',default=NO,choices=IS_SHOW.items(),)
    is_meet  = models.IntegerField(u'会议',default=NO,choices=IS_SHOW.items(),)
    is_roster  = models.IntegerField(u'商圈',default=NO,choices=IS_SHOW.items(),)
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'1.3 标签'
        app_label = 'api'
        ordering = ['-serial']

    def __unicode__(self):
        return '%s' % (self.name_admin)


class ImageMap(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
    local_path = models.ImageField(u'图标',upload_to='img/')
    tag = models.ForeignKey('Tag',verbose_name=u'标签',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'1.5 图库'
        app_label = 'api'
        
    def __unicode__(self):
        return '%s' % (self.id)

    def save(self):
        

        #ID 为空，新增图片
        if self.id is None:
            super(ImageMap, self).save() #先保存一遍
            QNUploadImage(self)

        #未保存前，获取原来的地址
        m = ImageMap.objects.get(id = self.id)
        _old_path = m.local_path.path if m.local_path != "" else ""
        print "2:",_old_path
        super(ImageMap, self).save()

        #保存后，获取新地址
        _new_path = self.local_path.path if self.local_path !="" else ""
        print "3:",_new_path


        #地址没变化，直接保存
        if  _old_path == _new_path:
            return
        else:
            QNUploadImage(self)
            
##        #获取本地地址
##        _local_path = self.local_path.path
##        print logger,_local_path
##        _now = datetime.datetime.now()
##        _name = "hx_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
##        _style = _local_path.split(".")[-1] # 拼接类别
##        _file_name = _name + "." + _style # 拼接图片名字
##        self.url =  "http://qiniu.308308.com/" + _file_name #存储的链接
##        self.name = _file_name
##        # #上传七牛
##        _qiniu = QiNiu()
##        print self.local_path.url
##        print self.local_path.name
##        _qiniu.put( "" , _file_name , _local_path )
##        super(ImageMap, self).save()

#更新图片
def QNUploadImage(self):
        #获取本地地址
        _local_path = self.local_path.path
        _now = datetime.datetime.now()
        _name = "hx_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
        _style = _local_path.split(".")[-1] # 拼接类别
        _file_name = _name + "." + _style # 拼接图片名字
        self.url =  "http://qiniu.308308.com/" + _file_name #存储的链接
        self.name = _file_name
        # #上传七牛
        _qiniu = QiNiu()
        print self.local_path.url
        print self.local_path.name
        _qiniu.put( "" , _file_name , _local_path )
        super(ImageMap, self).save()


IS_BANNER = {
    YES:u"广告文章",
    NO:u"一般文章",
}
import django.utils.timezone as timezone
class Article(models.Model):

    click_rate = models.IntegerField(u'点击率',default=568)
    is_top = models.IntegerField(u'文章置顶',default=NO,choices=IS_TOP.items(),)
    is_banner =  models.IntegerField(u'是否广告文章',default=NO,choices=IS_BANNER.items(),)  #他如果是广告
    #封面
    is_show_title= models.IntegerField(u'内容是否显示标题',default=YES,choices=IS_SHOW.items(),)
    cover = models.CharField(max_length=1000, verbose_name=u'封面图片',null=True,blank=True)
    cover_image = models.ForeignKey(ImageMap, verbose_name=u'选择封面图片',null=True,blank=True)
    #文章内容
    title = models.CharField(max_length=100, verbose_name=u'标题')
    subtitle = models.CharField(max_length=100,verbose_name=u'子标题',default='',null=True,blank=True)
    #摘要 发布时间
    summary = models.CharField(max_length=100,verbose_name=u'摘要',default='',null=True,blank=True)
    source = models.CharField(max_length=100,verbose_name=u'来源',default='',null=True,blank=True)
    #正文
    content = models.TextField(verbose_name=u'正文',null=True,blank=True)
    content_width = models.IntegerField(verbose_name=u'正文显示宽度',default=750,null=True,blank=True)
    is_show = models.IntegerField(u'是否显示文章',default=YES,choices=IS_SHOW.items(),)
    issue_time = models.DateTimeField(u'文章发布时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    #音频
    is_show_audio = models.IntegerField(u'是否显示音频',default=NO,choices=IS_SHOW.items(),)
    audio_src = models.CharField(max_length=1000,verbose_name=u'音频地址(Url)',null=True,blank=True)
    audio_poster = models.CharField(max_length=500,verbose_name=u'音频封面图(Url)',null=True,blank=True)
    audio_name = models.CharField(max_length=100,verbose_name=u'音频名称',null=True,blank=True)
    audio_author = models.CharField(max_length=100,verbose_name=u'音频作者',null=True,blank=True)
    #视频
    is_show_video = models.IntegerField(u'是否显示视频',default=NO,choices=IS_SHOW.items(),)
    video_src = models.CharField(max_length=1000,verbose_name=u'视频地址(Url)',null=True,blank=True)

    #标签、权限
    tag = models.ForeignKey('Tag',verbose_name=u'标签',null=True,blank=True)
    role = models.ForeignKey(Role, verbose_name=u'浏览权限',default=1,)
    #点播价格
    price = models.FloatField(u'普通点播单价',default=6,null=True,)

    #文章跳转那妞
    is_show_navigate = models.IntegerField(u'是否跳转到小程序',default=NO,choices=IS_SHOW.items(),)
    navigate_appid = models.CharField(max_length=100, verbose_name=u'appid',null=True,blank=True)
    navigate_path = models.CharField(max_length=100, verbose_name=u'页面路径',null=True,blank=True)
    navigate_data = models.CharField(max_length=100, verbose_name=u'传递数据',null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'1.1 文章'
        ordering = ['-issue_time', '-is_top']
        app_label = 'api'
        # ordering = ['rank', '-is_top', '-pub_time', '-create_time']

    def __unicode__(self):
            return self.title



IS_SWIPER = {
    YES:u"头条广告",
    NO:u"一般广告",
}

#文章标签
class Banner(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    article = models.ForeignKey('Article', verbose_name=u'所属文章',null=True,)  #自身目录
    tag = models.ForeignKey('Tag', verbose_name=u'所属标签',null=True,)  #自身目录
    cover = models.CharField(max_length=300, verbose_name=u'封面图片',null=True,blank=True)
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    is_swiper = models.IntegerField(u'是否头条广告',default=NO,choices=IS_SWIPER.items(),)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'1.2 广告条'
        app_label = 'api'
        ordering = ['-serial']

    def __unicode__(self):
        return '%s' % (self.name)
    # def save(self):

        # 1 Add 未填cover
        # 2 Add 已填cover
        # 3 change 未填cover
        # 4 delete 未填cover



        # if Article.objects.filter(id=self.id).exists() is True:
        #     _article = Article.objects.get(id=self.id)
        #     _old_url = _article.cover.url
        #     print _old_url
        #     super(Article, self).save()
        #     print 111
        #     if self.cover == "":  #删除封面
        #         return
		#
		#
        #     _local_img = os.path.join(BASE_DIR ,self.cover.url)  #拼接本地地址
        #     _now = datetime.datetime.now()
        #     _name = "hx_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
        #     _url  = _local_img
        #     _style = _url.split(".")[-1] # 拼接类别
        #     _file_name = _name + "." + _style # 拼接图片名字
        #     self.cover =  "http://img.12xiong.top/" + _file_name #存储的链接
        #     # print _file_name
        #     # print self.cover
        #     #上传七牛
        #     _qiniu = QiNiu()
        #     _qiniu.put( "" , _file_name , _local_img )
        #     super(Article, self).save()
        # else:
        #     print 'not alive'
        #     super(Article, self).save()
        #     print self.cover.url
        #     _local_img = os.path.join(BASE_DIR ,self.cover.url)  #拼接本地地址
        #     _now = datetime.datetime.now()
        #     _name = "hx_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
        #     _url  = _local_img
        #     _style = _url.split(".")[-1] # 拼接类别
        #     _file_name = _name + "." + _style # 拼接图片名字
        #     self.cover =  "http://img.12xiong.top/" + _file_name #存储的链接
        #     print _file_name
        #     print self.cover
        #     _qiniu = QiNiu()
        #     _qiniu.put( "" , _file_name , _local_img )
        #     super(Article, self).save()

# 可用保存代码
# _local_img = os.path.join(BASE_DIR ,self.cover.url)  #拼接本地地址
# _now = datetime.datetime.now()
# _name = "hx_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
# _url  = _local_img
# _style = _url.split(".")[-1] # 拼接类别
# _file_name = _name + "." + _style # 拼接图片名字
# self.cover =  "http://img.12xiong.top/" + _file_name #存储的链接
# # print _file_name
# # print self.cover
# #上传七牛
# _qiniu = QiNiu()
# _qiniu.put( "" , _file_name , _local_img )
# super(Article, self).save()
