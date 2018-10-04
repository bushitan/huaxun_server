     #coding:utf-8
from django.contrib import admin

# Register your models here.
from meet.models import *
# from django.contrib.contenttypes.admin import GenericTabularInline
# from meet.lib.meet_fieldsets import *
# _meetAmin = MeetAdmin()
from meet.lib.admin_fieldsets import ArticleFieldsets
print 

class ImageLibraryAdmin(admin.ModelAdmin):
    fields = ['name','cover_pre','url','style','local_path',]
    list_display = ('id','cover_pre','url',)
    list_editable = ('url',)
    list_display_links = ('id', 'cover_pre',) #点击图片进入
    def cover_pre(self, obj):
        if obj.url != "":
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
admin.site.register(ImageLibrary,ImageLibraryAdmin)

# from django import forms
# class ArticleForm(forms.ModelForm):


class ArticleLibraryAdmin(admin.ModelAdmin):
    list_display = ('id','style','title','subtitle','issue_time','is_show',)
    # fieldsets = _meetAmin.GetArticleFieldsets()
    # inlines = [CoverInline] #
    suit_form_tabs = (('content', '内容'), ('cover', u'封面')) #tab分栏
    fieldsets = (
        (u"展示", {
            'fields': ['is_show','style','click_rate',]
        }),
        (u"标题", {
            'fields': ['title','subtitle','summary','source',]
        }),
        (u"正文", {
            'fields': ['content','content_width','summary','source',]
        }),
        (u"地址", {
            'fields': ['address','work_date','phone','introduction',]
        }),
    )
    # radio_fields = {"style": admin.HORIZONTAL}
    # def get_form(self, request, obj=None, *args, **kwargs):
    #     if obj is not None:
    #         self.fieldsets = ArticleFieldsets(obj.style )
    #     return super(ArticleLibraryAdmin, self).get_form(request, obj, **kwargs)
    class Media:
        js = ('/huaxun/static/tinymce/tinymce.min.js',
              '/huaxun/static/tinymce/textareas.js')
admin.site.register(ArticleLibrary,ArticleLibraryAdmin)



# 文章 按行业大类过滤
#自定义  list_filter
from django.utils.translation import gettext_lazy as _
class SonMeetFilter(admin.SimpleListFilter):
    title = _('选择会议')
    parameter_name = 'father_tag'
    def lookups(self, request, model_admin):
        # 查行业大类的标签名
        _father_tag = Meet.objects.filter(father = None)
        _tup_list = ()
        for f in _father_tag:
            _key = f.id
            _value = str( f.name.encode('UTF-8') )
            _tup = ( (str(_key),_(_value)),)
            _tup_list = _tup_list + _tup
        return _tup_list

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(father =  self.value() )
        else :
            return queryset

class MeetAdmin(admin.ModelAdmin):
    fieldsets = (
        (u"会议列表",{"fields": ["name","style","father","cover_pre","cover_image","status","des","serial","create_time"]}),
        (u"地图酒店信息",{"fields":["hotel","phone","address","latitude","longitude",]}),
    )

    # inlines = [SubInline] #插入花名册的信息
    list_filter = ("style",SonMeetFilter,)
    list_display = ("id","name","cover_pre","father","style","serial","status"  )
    # fields = ["name","style","father","cover_pre","cover_image","status","des","serial","address","latitude","longitude","create_time" ]
    def cover_pre(self, obj):
        if obj.cover_image is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover_image.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
    raw_id_fields = ("cover_image",)
    # suit_form_tabs = (('meet', '主会议'), ('sub', u'子会议')) #tab分栏
admin.site.register(Meet,MeetAdmin)

class SwiperAdmin(admin.ModelAdmin):
    pass
admin.site.register(Swiper,SwiperAdmin)

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('name','meet','title','summary','des','footer','start_time','end_time',)
    list_editable = ('meet',)
    pass
admin.site.register(Agenda,AgendaAdmin)



class GuestAdmin(admin.ModelAdmin):

    fields = ['cover_pre','logo_image','name','meet','article','company','introduction',]
    list_display = ('id','cover_pre','name','meet','article','company','introduction',)
    raw_id_fields = ('logo_image',)
    def cover_pre(self, obj):
        if obj.logo_image is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.logo_image.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
    list_display_links = ('id', 'cover_pre',) #点击图片进入
admin.site.register(Guest,GuestAdmin)


class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (u"标题",{"fields":["cover_pre","cover_image","title","summary","des","footer","create_time",]}),
        (u"内容",{"fields":["meet","article",]}),
    )
    list_display = ('id',"cover_pre",'meet','title','meet','article',)
    raw_id_fields = ("cover_image",)
    def cover_pre(self, obj):
        if obj.cover_image is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover_image.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]


admin.site.register(News,NewsAdmin)


class SpotAdmin(admin.ModelAdmin):
    # fields = ['cover_pre','cover_image','title','meet',]
    list_display = ('id','cover_pre','title','meet',)
    raw_id_fields = ('cover_image',)
    def cover_pre(self, obj):
        if obj.cover_image is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover_image.url)
        else:
            html = u"未添加封面"
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
    list_display_links = ('id', 'cover_pre',) #点击图片进入
admin.site.register(Spot,SpotAdmin)

# raw_id_fields = ('cover_image',)







    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "page": #过滤文章page显示样式
    #         kwargs["queryset"] = Page.objects.filter(is_cover = NO)
    #     return super(ArticleLibraryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    # def get_fieldsets(self,request,obj):
    #     if obj.page is None:
    #         return _meetAmin.GetArticleFieldsets()
    #     f = obj.page.fieldsets
    #     if f == "" :
    #         return _meetAmin.GetArticleFieldsets()
    #     else:
    #         return _meetAmin.Str2Tuple(f)




##2
# class CoverInline(admin.StackedInline):
#     model = Cover
#     extra = 0
#     suit_classes = 'suit-tab suit-tab-cover'
#     verbose_name = ""
#     verbose_name_plural = '封面'
#     def get_fieldsets(self,request,obj=None):
#         return _meetAmin.GetCoverFieldsets()
# ##    def get_fieldsets(self,request,obj):
# ##        print self
# ##        print obj,"obj"
# ##        print obj.page
# ##        print obj.page.id
# ##        if obj.page is None:
# ##            return _meetAmin.GetCoverFieldsets()
# ##        f = obj.page.fieldsets
# ##        if f == "" :
# ##            return _meetAmin.GetCoverFieldsets()
# ##        else:
# ##            return _meetAmin.Str2Tuple(f)
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "page": #过滤文章page显示样式
#             kwargs["queryset"] = Page.objects.filter(is_cover = YES)
#         return super(CoverInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
