#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from meet_sign.action.attendee import *
from meet_sign.action.cost import *
from meet_sign.action.pay import *

class AttendeeGet( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_s_session = request.GET.get('meet_session',"")
			_att = ActionAttendee()
			_d_attendee = _att.GetInfo(_s_session)
			_dict = {
				'dict_attendee':_d_attendee
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
class AttendeeSet( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_s_session = request.GET.get('meet_session',"")
			_s_name = request.GET.get('name',"")
			_att = ActionAttendee()
			_d_attendee = _att.SetInfo(
				_s_session,
				name = _s_name,
			)
			_dict = {
                'dict_attendee':_d_attendee
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

class CostGetList( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_s_meet_id = request.GET.get('meet_id',"")
			_cost = ActionCost( )
			_l_cost = _cost.GetListByCurrentMeet( int(_s_meet_id) )
			_dict = {
                'list_cost':_l_cost
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 生成支付签名，
class PayOrder( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_s_session = request.GET.get('session',"")
			_s_cost_id = request.GET.get('cost_id',"")
			_s_discount_id = request.GET.get('discount_id',"")
			_action_pay = ActionPay()
			_wx_sign = _action_pay.WXPaySign(_s_session ,_s_cost_id)
			_dict = {
				"wx_sign":_wx_sign,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#3 微信支付回调
class PayCallback( ListView):
	def post(self, request, *args, **kwargs):
		try:
			_xml_request =  request.body
			_action_pay = ActionPay()
			_xml = _action_pay.WXPaySuccess(_xml_request)
			return HttpResponse( _xml,content_type="application/xml")
		except Exception,e :
			print e
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )












