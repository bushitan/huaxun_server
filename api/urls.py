# -*- coding: utf-8 -*-


from django.conf.urls import url
from api.views. v_article import *
from api.views. v_match import *
from api.views. v_my import *
from api.views. v_pay import *
from api.views. v_roster import *


urlpatterns = [

   url(r'^article/index/$', ArticleIndex.as_view()),
   url(r'^article/get_list/tag/$', ArticleGetListByTag.as_view()),
   url(r'^article/get/id/$', ArticleGetById.as_view()),
   url(r'^article/get_list/search/$', ArticleGetListBySearch.as_view()),
   url(r'^article/get_list/meet/$', ArticleGetListByMeet.as_view()),
   url(r'^article/check/single/$', ArticleCheckBySingle.as_view()),

   url(r'^match/set/issue/$', MatchSetIssue.as_view()),
   url(r'^match/get_list/tag/$', MatchGetListByTag.as_view()),
   url(r'^match/get_list/self/$', MatchGetListBySelf.as_view()),
   url(r'^match/delete/self/$', MatchDeleteBySelf.as_view()),

   url(r'^my/login/$', MyLogin.as_view()),
   url(r'^my/set/wx/$', MySetWXInfo.as_view()),
   # url(r'^my/set/roster/$', MySetRosterInfo.as_view()),
   url(r'^my/get/self/$', MyGetSelfInfo.as_view()),

   url(r'^pay/get/tag/$', PayGetTag.as_view()),
   # url(r'^pay/get_discount/tag_role$', PayGetDiscountByTagRole.as_view()),
   url(r'^pay/create/order/$', PayCreateOrder.as_view()),
   url(r'^pay/get_list/member/$', PayGetListMember.as_view()),
   url(r'^pay/get_list/discount/$', PayGetListDiscount.as_view()),

   url(r'^pay/confirm/order/$', PayConfirmOrder.as_view()),
   url(r'^pay/callback/wx/$', PayWxCallback.as_view()),
   #TODO 2018-2-4 增加连接
   url(r'^pay/confirm/renew/$', PayConfirmRenew.as_view()),
   url(r'^pay/callback/wx_renew/$', PayWxCallbackRenew.as_view()),

   url(r'^pay/get/protocol/$', PayGetProtocolByID.as_view()),






   # url(r'^pay/callback/zero$', PayZeroCallback.as_view()),

   url(r'^roster/get_list/tag/$', RosterGetListByTag.as_view()),
   url(r'^roster/get/id/$', RosterGetByID.as_view()),
   url(r'^roster/get_list/search/$', RosterGetListBySearch.as_view()),
   url(r'^roster/get_list/match/$', RosterGetListByMatch.as_view()),
   url(r'^roster/get_list/area/$', RosterGetListByArea.as_view()),
   url(r'^roster/get/self/$', RosterGetBySelf.as_view()),
   url(r'^roster/set/self/$', RosterSetBySelf.as_view()),
   url(r'^roster/get_area_list/$', RosterGetAreaList.as_view()),






   # url(r'^index/$', Index.as_view()),
   # url(r'^tag/$', GetTag.as_view()),
   # url(r'^tag/article/$', GetArticleByTag.as_view()),
   # url(r'^article/$', GetArticle.as_view()),
   # url(r'^article/search/$', GetArticleSearch.as_view()),
   # url(r'^article/read_trace/$', GetReadTrace.as_view()),
   #
   # #解锁方式
   # # url(r'^check/pay/$', CheckPay.as_view()),
   # url(r'^check/phone/$', Index.as_view()),
   #
   # #生成支付页面
   # url(r'^order/create_payment_page/$', PaymentPage.as_view()), #创建订单
   # #创建订单
   # url(r'^order/pre_member/$', PreMemberOrder.as_view()), #预备会员订单
   # url(r'^order/pre_single/$', PreSingleOrder.as_view()), #预备点播订单
   # #订单支付结果
   # url(r'^order/confirm_member/$', ConfirmMemberOrder.as_view()), #使用订单及优惠券确认。
   # url(r'^order/wx_notify/$', CallBackWxNotify.as_view()), #微信支付成功回调
   #
   # #订单查询
   # url(r'^order/get_order/$', GetOrder.as_view()),   #获取订单
   # url(r'^order/get_member/$', GetMember.as_view()), #获取会员
   # url(r'^order/get_discount/$', GetDiscount.as_view()), #获取优惠券
   #
   #
   # url(r'^user/login/$', UserLogin.as_view()),  #用户登录 ，这两个应该合在一起
   # url(r'^user/set/login_info/$', SetLoginInfo.as_view()),  #用户登录 ，这两个应该合在一起
   # url(r'^user/set/phone_info/$', SetPhoneInfo.as_view()),  #用户登录 ，这两个应该合在一起
   #
   # # url(r'^user/add_trace/$', UserAddTrace.as_view()),  #用户登录 ，这两个应该合在一起
   # url(r'^user/trace/$', GetUserTrace.as_view()),  #用户登录 ，这两个应该合在一起
   # url(r'^user/info/$', GetUserInfo.as_view()),  #用户登录 ，这两个应该合在一起
   # url(r'^data/$', AllData.as_view()),  #用户登录 ，这两个应该合在一起
   #
   # # # 花名册
   # # url(r'^roster/index/$', RosterIndex.as_view()),  #用户登录 ，这两个应该合在一起
   # # url(r'^roster/detail/$', RosterDetail.as_view()),  #用户登录 ，这两个应该合在一起
   # #
   # # # 供求信息
   # # url(r'^news/all/$', AllNewsList.as_view()),   #获取订单
   # # url(r'^news/set/by_user/$', SetNewsByUser.as_view()),   #获取订单
   # # url(r'^news/get/detail/$', GetNewsDetail.as_view()),   #获取供求信息
   # # url(r'^news/get/list_by_user/$', GetNewsListByUser.as_view()),   #获取用户获取列表
   # # url(r'^news/delete/by_user/$', DeleteNewsByUser.as_view()),   #获取用户删除
   #
   # # 会议
   # url(r'^meet/index/$', MeetIndex.as_view()),   #获取订单
   # # url(r'^meet/get_article/$', AllNewsList.as_view()),   #获取订单



]
