# -*- coding: utf-8 -*-
from django.contrib import admin

from api.models.user import *
from roster.models import *
from api.lib.util import *


class MyAdminSite(admin.AdminSite):
    site_header = '华讯通小程序管理系统'  # 此处设置页面显示标题
    site_title = '华讯通小程序'  # 此处设置页面头部标题

admin_site = MyAdminSite(name='management')

def identify_pass(modeladmin, request, queryset):
    queryset.update(identify_status=3)
identify_pass.short_description = "审核通过"
def identify_refuse(modeladmin, request, queryset):
    queryset.update(identify_status=2)
identify_refuse.short_description = "审核不通过"



from django.contrib.contenttypes.admin import GenericTabularInline
class RosterInline(admin.StackedInline):          # 定义内联对象
    model = Roster
    extra = 0
    show_change_link = True
    suit_classes = 'suit-tab suit-tab-roster    '
##    max_num  = 1
    verbose_name = "联系人"
    verbose_name_plural = '商圈信息'
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter(is_main = YES)
        return super(RosterInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

#用户信息
class UserAdmin(admin.ModelAdmin):
    actions = [identify_pass,identify_refuse]
    search_fields = ('id','wx_id','name','company__name',)
    list_filter = ('identify_status',) #右边过滤器 'tag',
    # fields = ('logo','name','nick_name','phone','wx_id','company','identify_status','tag',)
    # fields = ('logo','name','nick_name','wx_id','company','phone',)
    fieldsets = (
        (u"微信", {
            'classes': ('suit-tab', 'suit-tab-user',),
            'fields': ['logo_tag','logo','nick_name','wx_id',]
        }),
        (u"会员信息", {
            'classes': ('suit-tab', 'suit-tab-roster',),
            'fields': ['logo_roster','roster_image','name','phone','company','introduction','address','latitude','longitude',]
        }),
    )
    list_display = ('id','logo_tag','logo_roster','name','wx_id','nick_name','phone','company',)
    list_display_links = ('id', 'logo_tag',) #点击进入列
    list_editable = ('name','phone',)
    list_per_page = ADMIN_PER_PAGE    
    raw_id_fields = ("company",'roster_image',)  #显示外键的搜索框
    # ,'level_tag'
    # radio_fields = {"company": admin.HORIZONTAL}# 外键的横向单选按钮
    # radio_fields = {"company": admin.VERTICAL} # 外键的纵向单选按钮
    # filter_horizontal = ( 'tag',)  #多对多的搜索栏
    inlines = [RosterInline] #插入花名册的信息
    suit_form_tabs = (('user', '小程序用户'), ('roster', u'商圈')) #tab分栏

    #显示头像图片
    def logo_tag(self, obj):
        if obj.logo != "":
            html = u'<img src="%s" style="width:48px;height:48px" />' %(obj.logo)
        else:
            html = u"用户未登录"
        return html
    logo_tag.short_description = '微信头像'
    logo_tag.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    #商圈的头像
    def logo_roster(self, obj):
        if obj.roster_image is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.roster_image.url)
        else:
            html = u"未添加商圈头像"
        return html
    logo_roster.short_description = u'商圈头像'
    logo_roster.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['logo_tag','logo_roster',]
admin.site.register(User,UserAdmin)

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('id','name',)

    list_display = ('id','name','employee_pre')
    list_display_links = ('id', 'name',) #点击进入列
    # fields = ('name','cover_pre',)
    fieldsets = (
        (u"企业名称", {'fields': ['name',]}),
        (u"下属员工", {'fields': ['cover_pre']}),
    )

    #准备员工信息
    def _getInfo(self,e):
        _dom_name =  u'%s' % (e.name) if e.name != ""  else ""
        #设置头像
        _dom_logo = u' <img src="%s" style="width:48px;height:48px" />' % (e.logo)  if e.logo != "" else ""
        #设置昵称
        _dom_nick_name =  u'%s' %(e.nick_name) if e.nick_name != ""  else ""
        return _dom_name,_dom_logo,_dom_nick_name

    # def get_fieldsets(self,request,obj=None):
    #     # fieldsets = super(CompanyAdmin, self).get_fieldsets(request, obj)
    #     # print fieldsets
    #     print 43895349
    #     print obj
    #     print 93578345743
    #     print request
    #     print 93578345743
    #     fieldsets = (
    #         (u"企业名称", {'fields': ['name',]}),
    #         (u"下属员工", {'fields': ['cover_pre']}),
    #     )
    #     return fieldsets



    def cover_pre(self, obj):
        _employee_query = User.objects.filter(company_id = obj.id)
        html = ""
        if len(_employee_query) == 0:
            html = u"该公司没有员工"
        else:
            for e in _employee_query:
                _dom_name, _dom_logo ,_dom_nick_name = self._getInfo(e)
                temp = u'''
                        <tr>

                            <td> <a href="/huaxun_2/admin/api/user/%s/">%s </a></td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>

                      </tr>

                '''%(e.id,e.id ,_dom_name, _dom_logo ,_dom_nick_name)
                html = html + temp
            base = u'''
                <div>
                     <table border="1">
                          <tr>
                            <th>ID</th>
                            <th>名称</th>
                            <th>微信头像</th>
                            <th>微信昵称</th>
                          </tr>
                          %s
                    </table>
                </div>
            '''%(html)
            html = base
        return html
    cover_pre.short_description = u'员工列表'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字

    def employee_pre(self, obj):
        _employee_query = User.objects.filter(company_id = obj.id)
        html = ""
        if len(_employee_query) == 0:
            html = u"该公司没有员工"
        else:
            for e in _employee_query:
                _dom_name, _dom_logo ,_dom_nick_name = self._getInfo(e)
                temp = u'''
                    <div>
                        <a href="/huaxun_2/admin/api/user/%s/">
                            ID：%s &nbsp;&nbsp;
                            %s &nbsp;&nbsp;
                            %s &nbsp;&nbsp;
                            %s &nbsp;&nbsp;
                        </a>
                    </div>
                '''%(e.id,e.id ,_dom_name, _dom_logo ,_dom_nick_name)
                html = html + temp
        return html
    employee_pre.short_description = u'员工列表'
    employee_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
admin.site.register(Company,CompanyAdmin)








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
