#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from meet_sign.action.attendee import *
from meet_sign.action.cost import *
from meet_sign.action.pay import *
from meet.action.a_meet import *

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
			_s_company = request.GET.get('company',"")
			_s_phone = request.GET.get('phone',"")
			_att = ActionAttendee()
			_d_attendee = _att.SetInfo(
				_s_session,
				name = _s_name,
				company = _s_company,
				phone = _s_phone,
			)
			_dict = {
                'dict_attendee':_d_attendee
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

class AttendeeSetLogo( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_s_session = request.GET.get('meet_session',"")
			_s_logo = request.GET.get('logo',"")
			_s_nick_name = request.GET.get('nick_name',"")

			_att = ActionAttendee()
			_d_attendee = _att.SetInfo(
				_s_session,
				logo = _s_logo,
				nick_name = _s_nick_name,
			)
			_dict = {
                'dict_attendee':_d_attendee
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

class CostGetList( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_cost = ActionCost()
		super(CostGetList,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			# _s_meet_id = request.GET.get('meet_id',"")
			_current_meet = self.action_meet.GetCurrent()
			_l_cost = self.action_cost.GetListByCurrentMeet( _current_meet["meet_id"] )
			_dict = {
                'list_cost':_l_cost
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 查询当前会议的支付信息
class PayCheck( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_pay = ActionPay()
		super(PayCheck,self).__init__()
	def get(self, request, *args, **kwargs):
		# try:
			_s_session = request.GET.get('meet_session',"")
			_current_meet = self.action_meet.GetCurrent()
			_is_pay = self.action_pay.CheckIsPay(_s_session ,_current_meet["meet_id"] )
			_dict = {
				"is_pay":_is_pay,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)

# 查询当前会议的支付信息
class PayGetInfo( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_pay = ActionPay()
		super(PayGetInfo,self).__init__()
	def get(self, request, *args, **kwargs):
		# try:
			_s_session = request.GET.get('meet_session',"")
			_current_meet = self.action_meet.GetCurrent()
			_list_sign = self.action_pay.GetInfo(_s_session ,_current_meet["meet_id"] )
			print _list_sign
			_dict = {
				"list_sign":_list_sign,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)

# 生成支付签名，
class PayOrder( ListView):
	def __init__(self):
		self.action_pay = ActionPay()
		super(PayOrder,self).__init__()
	def get(self, request, *args, **kwargs):
		# try:
			_s_session = request.GET.get('meet_session',"")
			_s_cost_id = request.GET.get('cost_id',"")
			_s_discount_id = request.GET.get('discount_id',"")
			print 11111 ,_s_cost_id
			# _action_pay = ActionPay()
			_wx_sign = self.action_pay.WXPaySign(_s_session ,_s_cost_id)
			_dict = {
				"wx_sign":_wx_sign,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

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












