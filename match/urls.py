# -*- coding: utf-8 -*-


from django.conf.urls import url
from match.views import *

urlpatterns = [
   # # 撮合模块初始化
   # url(r'^match/index/$', MatchIndex.as_view()),
   # # 上传：信息细节 根据 用户
   # url(r'^match/set/detail_by_user/$', MatchSetDetailByUser.as_view()),
   # # 查询：信息细节  根据 信息ID
   # url(r'^match/get/detail_by_id/$', MatchGetDetailById.as_view()),
   # # 查询：所拥有信息列表  根据 用户
   # url(r'^match/get/list_by_user/$', MatchGetListByUser.as_view()),
   # # 删除：信息 根据 信息ID和用户
   # url(r'^match/delete/by_id_user/$', MatchDeleteByIdUser.as_view()),

]
