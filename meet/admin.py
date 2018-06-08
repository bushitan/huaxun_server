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


class MeetAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (u"主会议", {
    #         'classes': ('suit-tab', 'suit-tab-meet',),
    #         'fields': ['father','name','des','status','serial','address','latitude','longitude',]
    #     }),
    # )
    # inlines = [SubInline] #插入花名册的信息
    list_display = ("id","name","des","father","style"  )
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
