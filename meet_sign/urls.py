# -*- coding: utf-8 -*-


from django.conf.urls import url
from meet_sign.views import *

urlpatterns = [
   #用户登录，本次会议的地图、封面、赞助商
   # 用户是否已报名，
   url(r'^sign/get/attendee_info/$', AttendeeGet.as_view()), #获取参会者信息
   url(r'^sign/set/attendee_info/$', AttendeeSet.as_view()), #设置参会者信息
   url(r'^sign/set/attendee_logo/$', AttendeeSetLogo.as_view()), #设置参会者信息
   url(r'^sign/get_list/cost/$', CostGetList.as_view()), #获取费用表
   url(r'^sign/pay/check/$', PayCheck.as_view()), #获取费用表
   url(r'^sign/pay/get/info/$', PayGetInfo.as_view()), #获取费用表
   url(r'^sign/pay/order/$', PayOrder.as_view()), #获取费用表
   url(r'^sign/pay/callback/$', PayCallback.as_view()), #获取费用表
]