# -*- coding: utf-8 -*-
from django.contrib import admin

# from api.model.user import *
from api.models.article import *
from django.utils.html import *

from api.lib.util import *

from api.lib.qi_niu import *
import huaxun_server.settings as SETTING
# from django.contrib.admin import SimpleListFilter
from django.db.models import Q
import os
BASE_DIR = os.path.dirname( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )


# 文章 按行业大类过滤
#自定义  list_filter
from django.utils.translation import gettext_lazy as _
class DecadeBornListFilter(admin.SimpleListFilter):
    title = _('选择行业')
    parameter_name = 'father_tag'
    def lookups(self, request, model_admin):
        # 查行业大类的标签名
        _father_tag = Tag.objects.filter(is_main = YES)
        _tup_list = ()
        for f in _father_tag:
            _key = f.id
            _value = str( f.name_admin.encode('UTF-8') )
            _tup = ( (str(_key),_(_value)),)
            _tup_list = _tup_list + _tup
        return _tup_list

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(tag__father =  self.value() )
        else :
            return queryset

##Tag.objects.filter(name_admin__icontains = u'图库')

class ImageTagListFilter(admin.SimpleListFilter):
    title = _('选择行业')
    parameter_name = 'father_tag'
    def lookups(self, request, model_admin):
        # 查行业大类的标签名
        _father_tag = Tag.objects.filter(is_image_map = YES)
        _tup_list = ()
        for f in _father_tag:
            _key = f.id
            _value = str( f.name_admin.encode('UTF-8') )
            _tup = ( (str(_key),_(_value)),)
            _tup_list = _tup_list + _tup
        return _tup_list

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(tag_id =  self.value() )
        else :
            return queryset




#角色信息表
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
admin.site.register(Role,RoleAdmin)


# from django.contrib.contenttypes.admin import GenericTabularInline
# class ChoiceInline(admin.StackedInline):          # 定义内联对象
#     model = Article
#     raw_id_fields = ("cover_image",)
#     extra = 0
#     max_num  = 1
#     classes = ['collapse']
#     # verbose_name = "321321"
#     verbose_name_plural = 'dshfs'
#     show_change_link = True
#
# inlines = [ChoiceInline]
    # fieldsets = (
    #     (u"", {'fields': ['content_width','content',]}),
    #     (u"点播单价", {'fields': ['price',]}),
    # )

class TagAdmin(admin.ModelAdmin):
    fieldsets = (
     (u"列表封面", {'fields': ['name_admin','name','serial','father',]}),
      (u"栏目显示", {'fields': ['is_main','is_swiper','is_index','is_match','is_ad','is_meet','is_roster','is_image_map',]}),
    )
    list_display = ('id','name_admin','name','serial','is_main','is_index','is_match','is_ad','is_meet','is_roster','is_image_map','father',)
    # list_editable = ('name_admin','name','is_main','is_index','is_match','is_show','serial','father',)
    list_editable = ('name_admin','serial',)

    #父类标签，只能选择指定了父类的
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "father":
            kwargs["queryset"] = Tag.objects.filter(is_main = YES)
        return super(TagAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Tag,TagAdmin)


#角色信息表
class ImageMapAdmin(admin.ModelAdmin):
    list_display = ('id','cover_pre','cover_copy','tag',)
    fields = ['name','cover_pre','cover_copy','local_path','tag',]
    list_display_links = ('id', 'cover_pre',) #点击图片进入
    list_editable = ('tag',)
    list_filter = (ImageTagListFilter,)
    list_per_page = 80
    #只显示图库的标签
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter(is_image_map = YES)
        return super(ImageMapAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def cover_pre(self, obj):
        if obj.url != "":
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    #readonly_fields = ['name','cover_pre',]

    def cover_copy(self, obj):
        copy = u'''
                <script type="text/javascript">
                    function copy%s()
                        {
                            var Url2=document.getElementById("%s").innerText;
                            var oInput = document.createElement('input');
                            oInput.value = Url2;
                            document.body.appendChild(oInput);
                            oInput.select(); // 选择对象
                            document.execCommand("Copy"); // 执行浏览器复制命令
                            oInput.className = 'oInput';
                            oInput.style.display='none';
                        };;
                </script>
                <div  id="%s" style="width:200px;word-wrap:break-word ; display:none">%s</div>
                <input type="button" onClick="copy%s()" value="点击复制代码" />
            ''' %(obj.id,obj.id,obj.id,obj.url,obj.id)
        return copy
    cover_copy.short_description = u'图片链接'
    cover_copy.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['name','cover_pre','cover_copy',]

admin.site.register(ImageMap,ImageMapAdmin)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('=tag__name','title','id')
    # fields = ['cover','title','summary','content','tag','is_show','role','price',]
    # fields = ['cover','title','summary','role','content','tag',]
    fieldsets = (
        (u"状态", {
            'classes': ('suit-tab', 'suit-tab-base',),
            'fields': ['is_show',]}),
        (u"列表封面",{
            'classes': ('suit-tab', 'suit-tab-base',),
             'fields': ['is_show_title','cover_pre','cover_image','title','subtitle',]}),
        (u"摘要",{
            'classes': ('suit-tab', 'suit-tab-base',),
             'fields': ['summary','source','issue_time',]}),
        (u"文章内容",{
            'classes': ('suit-tab', 'suit-tab-base',),
         'fields': ['content_width','content',]}),
        (u"点播单价",{
            'classes': ('suit-tab', 'suit-tab-base',),
            'fields': ['price',]}),
        (u"详情",{
            'classes': ('suit-tab', 'suit-tab-base',),
             'fields': ['tag','is_top','role','click_rate','is_banner',]}),
        (u"音频",{
            'classes': ('suit-tab', 'suit-tab-video',),
             'fields': ['is_show_audio',('audio_src','audio_poster'),('audio_name','audio_author',)],},),
        (u"视频",{
            'classes': ('suit-tab', 'suit-tab-video',),            
            'fields': ['is_show_video','video_src'],}), #'classes': ['collapse']
        (u"跳转其他小程序",{
            'classes': ('suit-tab', 'suit-tab-video',),
            'fields': ['is_show_navigate',("navigate_appid","navigate_path","navigate_data",)],},),
        # (u"详情", {'fields': ['price','vip_price','super_vip_price']}),
    )
    #list_editable = ('role','is_banner','tag',) #在list页面编辑
    list_display = ('id','cover_pre','title','tag','role','is_top','is_banner','is_show',)
    # list_editable = ('role','price','is_top','is_banner','is_show','tag','issue_time',) #在list页面编辑
    # list_display = ('id','cover_pre','title','role','price','is_top','is_show','is_banner','tag','issue_time',)
    list_filter = ('is_banner','role',DecadeBornListFilter,'tag',) #右边过滤器
    list_per_page = ADMIN_PER_PAGE
    list_display_links = ('id', 'cover_pre','title',) #点击进入列
    raw_id_fields = ('cover_image',)  #选择封面图片
    def cover_pre(self, obj):
        if obj.cover_image is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover_image.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
    suit_form_tabs = (('base', u'基础内容'), ('video', u'音视频'))
    class Media:
        js = ('/huaxun/static/tinymce/tinymce.min.js',
              '/huaxun/static/tinymce/textareas.js')
        # js = (
        #     '/huaxun/static/ue/ueditor.config.js' ,
        #     '/huaxun/static/ue/ueditor.all.min.js',
        #     '/huaxun/static/ue/ueditorCustomConfig.js'
        # )
    # filter_horizontal = ( 'tag', )
    # filter_vertical = ( 'tag', )
    #文章只会放在首页的标签里
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter(Q(is_index = YES )| Q(is_ad =YES) | Q(is_swiper = YES) | Q(is_meet = YES) )
        return super(ArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
        dom = obj.content

        #边框
        import re
        _style = 'style="border: 1px solid #E8E8E8;"'
        _str_style = re.compile(_style)
        _str_table = re.compile('<table')
        _str_colgroup = re.compile('<colgroup')
        _str_tr = re.compile('<tr')
        _str_td = re.compile('<td')
        b = _str_style.sub('',dom)
        b = _str_table.sub('<table '+_style,b)
        b = _str_colgroup.sub('<colgroup '+_style,b)
        b = _str_tr.sub('<tr '+_style ,b)
        b = _str_td.sub('<td '+_style,b)

        #处理特殊字符
        _re_str = re.compile('&radic;')
        b = _re_str.sub(u'勾',b)
        _re_str = re.compile('&rdquo;')
        b = _re_str.sub('"',b)
        _re_str = re.compile('&ldquo;')
        b = _re_str.sub('"',b)
        _re_str = re.compile('&mdash;')
        b = _re_str.sub('-',b)

        obj.content = b
        obj.save()


        # print obj.cover
        # print obj.cover.url
        # print  os.path.join(BASE_DIR,"media" ,obj.cover.url)
        # _local_img = os.path.join(BASE_DIR,"media" ,obj.cover.url)
        # print _local_img
        # print os.path.exists(_local_img) ,'is live'
        # #上传七牛
        # # _qiniu = QiNiu()
        # # _qiniu.put("hx_","123.png",_local_img )

        # print os.path.exists(_local_img) ,'is live2'

admin.site.register(Article,ArticleAdmin)




#角色信息表
class BannerAdmin(admin.ModelAdmin):
    list_filter = ('tag','is_swiper',) #右边过滤器
    list_display = ('id','name','article','tag','cover','serial','is_swiper',)
    list_editable = ('name','article','tag','cover','serial','is_swiper',) #在list页面编辑
    list_per_page = ADMIN_PER_PAGE
    raw_id_fields = ('article',)
# admin.site.register(Banner,BannerAdmin)

