# -*- coding: utf-8 -*-
from django.contrib import admin

from roster.models import *
from api.lib.util import *

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
            return queryset.filter(tag =  self.value() )
        else :
            return queryset
        
#角色信息表
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','name','serial')
    list_editable = ('name','serial',) 
    
admin.site.register(Area,AreaAdmin)

    
#角色信息表
class RosterAdmin(admin.ModelAdmin):
    list_filter = (DecadeBornListFilter,) #右边过滤器
    list_display = ('user','user_logo','user_roster_image','tag','serial','buy_tag','sell_tag','area',)
    fields = ['user','tag','serial','buy','sell','area',]
    list_display_links = ( 'user','user_logo',) #点击进入列
##    list_editable = ('serial','tag',) #在list页面编辑
    list_per_page = ADMIN_PER_PAGE
    raw_id_fields = ("user",)
    filter_horizontal = ( 'sell','buy', )
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter(is_main = YES)
        return super(RosterAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "buy" or db_field.name == "sell":
            kwargs["queryset"] = Tag.objects.filter(is_match = YES)
        return super(RosterAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
     #显示头像图片
    def user_logo(self, obj):
        if obj.user is None :
            html = u"用户未登录"
            return html
        if obj.user.logo != "" :
            html = u'<div style="width:48px;height:48px"><img src="%s" width="48" height="48" style="width:48px;height:48px" /></div>' %(obj.user.logo)
        else:
            html = u"用户未登录"
        return html
    user_logo.short_description = '微信头像'
    user_logo.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字

    def user_roster_image(self, obj):
        if obj.user.roster_image  is not None:
            html = u'<div style="width:48px;height:48px"><img src="%s" width="48" height="48" style="width:48px;height:48px" /></div>' %(obj.user.roster_image.url)
        else:
            html = u"未添加商圈头像"
        return html
    user_roster_image.short_description = '商圈头像'
    user_roster_image.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字

    def buy_tag(self, obj):        
        return "\n".join([p.name for p in obj.buy.all()])
    buy_tag.short_description = '求购'
    def sell_tag(self, obj):        
        return "\n".join([p.name for p in obj.sell.all()])
    sell_tag.short_description = '供应'
    readonly_fields = ['user_logo','user_roster_image','buy_tag','sell_tag',]
    
admin.site.register(Roster,RosterAdmin)


