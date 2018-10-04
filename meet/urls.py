# -*- coding: utf-8 -*-


from django.conf.urls import url
from meet.views import *

urlpatterns = [
   #用户登录，本次会议的地图、封面、赞助商
   url(r'^login/$', Login.as_view()),
   url(r'^index/$', MeetIndex.as_view()),  #获取日程
   url(r'^article/get/article_id/$', ArticleGetByArticleID.as_view()),  #文章详情
   url(r'^agenda/get_list/meet_id/$', AgendaGetListByMeetID.as_view()),  #日程列表
   url(r'^guest/get_list/meet_id/$', GuestGetListByMeetID.as_view()),  #嘉宾列表
   url(r'^news/get_list/meet_id/$', NewsGetListByMeetID.as_view()),  #新闻列表
   url(r'^spot/get_list/meet_id/$', SpotGetListByMeetID.as_view()),  #景点列表
   url(r'^catalog/get_list/$', CatalogGetList.as_view()),  #景点列表
   url(r'^main/get/meet_id/$', MainGetByID.as_view()),  #景点列表

]
