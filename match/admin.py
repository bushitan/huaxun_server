# -*- coding: utf-8 -*-
from django.contrib import admin

from match.models import *
from api.lib.util import *

#角色信息表
class MatchAdmin(admin.ModelAdmin):
    list_filter = ('is_buy',) #右边过滤器
    list_display = ('id','is_buy','user','tag','title','content','phone','issue_time','create_time',)
    # list_editable = ('is_buy','user','tag','title','phone','issue_time',) #在list页面编辑
    # list_editable = ('is_buy','user','tag','title','phone','issue_time',) #在list页面编辑
    list_per_page = ADMIN_PER_PAGE

    raw_id_fields = ("user",)  #显示外键的搜索框
admin.site.register(Match,MatchAdmin)
