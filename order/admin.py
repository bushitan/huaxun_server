# -*- coding: utf-8 -*-
from django.contrib import admin

from order.models import *
from api.lib.util import *

    # fieldsets = (
    #     (u"用户", {'fields': ['user',]}),
    #     (u"支付", {'fields': ['is_payment','wx_out_trade_no']}),
    #     (u"合同", {'fields': ['agreement_type',('tag','role'),('article','play_num'),('start_time','end_time')]}),
    #     (u"优惠打折", {'fields': ['discount',('original_fee','payment_fee')]}),
    #     (u"订单创建时间", {'fields': ['create_time']}),
    # )

    # list_display = ('id','user','is_payment','wx_out_trade_no','original_fee','payment_fee','agreement_type','tag','role','article','play_num','start_time','end_time','create_time','is_alive',)

# from api.admin.article import *
# DecadeBornListFilter
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('=user__id',)
    list_display = ('id','user','is_payment','wx_out_trade_no','original_fee','payment_fee','agreement_type','tag','role','article','start_time','end_time','renew_order','is_alive',)
    fieldsets = (
        (u"用户", {'fields': ['user',]}),
        (u"状态", {'fields': ['is_payment','is_alive',]}),
        # (u"续费的订单", {'fields': ['renew_order']}),
        (u"合同", {'fields': ['agreement_type',('tag','role'),('start_time','end_time')]}),
        (u"订单创建时间", {'fields': ['create_time']}),
    )
    raw_id_fields = ("discount","user",)
    list_filter = ('is_payment','agreement_type','role','tag',) #右边过滤器
    list_per_page = ADMIN_PER_PAGE
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter(is_main = YES)
        return super(OrderAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Order,OrderAdmin)


class DiscountAdmin(admin.ModelAdmin):
    search_fields = ('=user__id',)
    list_display = ('id','user','template','is_used','start_time','end_time','is_active',) #'object_link',
    fieldsets = (
        (u"用户", {'fields': ['user',]}),
        (u"是否作废", {'fields': ['is_active',]}),
        (u"模板", {'fields': [('template',)]}),
        (u"有效期", {'fields': [('start_time','end_time'),]}),
        # (u"订单创建时间", {'fields': ['create_time']}),
    )
    # raw_id_fields = ("template",)
    list_filter = ('is_used','is_active','template',) #右边过滤器
    list_editable = ('template',)                 #在list页面直接编辑
    list_per_page = ADMIN_PER_PAGE
    def object_link(self, obj):
        url = '../discounttemplate/'
        # tag = "\n".join([p.name for p in obj.tag.all()])
        tag = '1'
        return u'<a href={url} target="_blank">修改优惠券模板</a>'.format(url=url,tag=tag)
    object_link.short_description = '跳转页面'
    object_link.allow_tags = True
    list_select_related = True
    readonly_fields = ['is_used']
    raw_id_fields = ('user',)  #选择封面图片
    # list_display = ('id','user','is_payment','original_fee','payment_fee','create_time')
admin.site.register(Discount,DiscountAdmin)


class DiscountTemplateAdmin(admin.ModelAdmin):
    list_display = ('id','use_condition','use_range','name','tag','agreement_type','fee','limit_fee',)
    fieldsets = (
        (u"名称", {'fields': ['name','use_condition','use_range',]}),
        (u"优惠价格", {'fields': ['agreement_type','fee',]}),
        # (u"使用条件", {'fields': ['limit_fee','tag',]}),
        # (u"创建时间", {'fields': ['create_time',]}),
        # (u"订单创建时间", {'fields': ['create_time']}),

    )
    list_filter = ('agreement_type','tag',) #右边过滤器
    # list_editable = ('name','use_condition','use_range','agreement_type','fee','limit_fee','tag',)
admin.site.register(DiscountTemplate,DiscountTemplateAdmin)
