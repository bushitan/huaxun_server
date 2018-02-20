# -*- coding: utf-8 -*-


from django.conf.urls import url
from roster.views import *

urlpatterns = [
   # 花名册初始化
   url(r'^roster/index/$', RosterIndex.as_view()),  #用户登录 ，这两个应该合在一起
   # 查询：花名册细节 根据 用户id
   url(r'^roster/get/detail_by_user/$', RosterGetDictByID.as_view()),
   # 查询:所属员工 根据  公司、行业标签
   url(r'^roster/get/user_by_tag_company$', RosterGetListByTagCompany.as_view()),
   url(r'^roster/search/$', RosterSearch.as_view()),

]