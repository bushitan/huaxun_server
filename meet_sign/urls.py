# -*- coding: utf-8 -*-


from django.conf.urls import url
from meet.views import *

urlpatterns = [
   #用户登录，本次会议的地图、封面、赞助商
   # 用户是否已报名，
   url(r'^login/$', Login.as_view()),

   url(r'^agenda/get_list/meet_id/$', AgendaGetListByMeetID.as_view()),  #获取日程

   url(r'^guest/get_list/meet_id/$', GuestGetListByMeetID.as_view()),  #嘉宾列表
   url(r'^guest/get/guest_id/$', GuestGetByGuestID.as_view()),  #嘉宾详情

   url(r'^news/get_list/meet_id/$', NewsGetListByMeetID.as_view()),  #新闻列表

   url(r'^article/get/article_id/$', ArticleGetByArticleID.as_view()),  #嘉宾详情

   url(r'^spot/get_list/meet_id/$', SpotGetListByMeetID.as_view()),  #用户登录 ，这两个应该合在一起
   url(r'^spot/get/spot_id/$', SpotGetBySpotID.as_view()),  #用户登录 ，这两个应该合在一起


   url(r'^bill/get_list/meet_id/$', BillGetListByMeetID.as_view()),  #获取本次会议的费用
   url(r'^order/get_list/user_id/$', OrderGetListByUserID.as_view()),  #获取用户的订单
   url(r'^order/pay/$', OrderPay.as_view()),  #用户支付
   url(r'^order/pay_callback/$', OrderPayCallback.as_view()),  #用户支付结果
]