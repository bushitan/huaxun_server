# -*- coding: utf-8 -*-
from django.contrib import admin

from log.models import *
from api.lib.util import *

#角色信息表
class Article_ClickAdmin(admin.ModelAdmin):
    list_filter = ('is_read',) #右边过滤器
    list_display = ('id','user','article','is_read','create_time',)
    # list_editable = ('is_buy','title','phone',) #在list页面编辑
    list_per_page = ADMIN_PER_PAGE
admin.site.register(Article_Click,Article_ClickAdmin)
