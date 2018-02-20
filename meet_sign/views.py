#coding:utf-8

from django.views.generic import ListView


from api.lib.message import *
from api.models.user import *
from api.hx.hx_user import *
# from api.hx.hx_tag import *
# from api.hx.hx_role import *

class Index( ListView):
	pass

#1 用户登录，本次会议的地图、封面、赞助商
# 用户是否已报名，
class Login( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_js_code = request.GET.get('js_code',"")
			_session = request.GET.get('session',"")
			_session = request.GET.get('union_id',"")

			_hx_user = HX_User()
			_user = _hx_user.UserLogin(_js_code ,_session)

			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 获取日程列表
class AgendaGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#3 获取嘉宾列表
class GuestGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#4 嘉宾详情
class GuestGetByGuestID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#5 获取新闻列表
class NewsGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#6 获取文章
class ArticleGetByArticleID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#7 景点列表
class SpotGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#8 景点详情
class SpotGetBySpotID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#9 会议的设置级别
class BillGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#10 用户已经支付的订单
class OrderGetListByUserID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#11 用户报名支付
# 订购数量，订购bill类别
class OrderPay( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#12 用户支付结果
class OrderPayCallback( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                '12':'2131'
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )































