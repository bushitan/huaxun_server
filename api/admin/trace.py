# -*- coding: utf-8 -*-
from django.contrib import admin

from api.models.trace import *


class HistoryUserRoleAdmin(admin.ModelAdmin):
    pass
# admin.site.register(HistoryUserRole,HistoryUserRoleAdmin)



class RelArticleUserAdmin(admin.ModelAdmin):
    list_display = ('id','user','article',)
# admin.site.register(RelArticleUser,RelArticleUserAdmin)


class PayBillAdmin(admin.ModelAdmin):
    list_filter = ('id',)
    date_hierarchy = ('create_time')
    list_display = ('id','user_id','price','create_time',)
    search_fields = ('user__name','user__id',)
    readonly_fields = ['user','price','create_time',]
# admin.site.register(PayBill,PayBillAdmin)









#自定义  list_filter
# from datetime import date
# from django.utils.translation import gettext_lazy as _
#
# class DecadeBornListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('decade born')
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'decade'
#
#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('80s', _('in the eighties')),
#             ('90s', _('in the nineties')),
#         )
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#
#         if self.value() == '80s':
#             return queryset.filter(birthday__gte=date(1980, 1, 1),
#                                     birthday__lte=date(1989, 12, 31))
#         if self.value() == '90s':
#             return queryset.filter(birthday__gte=date(1990, 1, 1),
#                                     birthday__lte=date(1999, 12, 31))