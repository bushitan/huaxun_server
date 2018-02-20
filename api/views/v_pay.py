#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from api.hx.hx_discount import *
from api.hx.hx_order import *
from api.models.user import *
from api.hx.hx_role import *
from api.lib.util import *

# 根据tag和user，获取当前用户要支付的 标签列表
class PayGetTag( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session =  request.GET.get('session',""))
			_tag_id = request.GET.get('tag_id',"")
			_role = HX_Role()
			_top_role_value = _role.GetPreparePayByTag(_user.id,_tag_id)
			_role_list = _role.GetPayRoleList(_top_role_value) #获取要支付的 角色列表
			_vip_role = _role.GetRoleByValue(ROLE_LEVEL_2)
			_super_vip_role = _role.GetRoleByValue(ROLE_LEVEL_3)
			_dict = {
				"role_list":_role_list,
				"vip_role":_vip_role,
				"super_vip_role":_super_vip_role,
				"show_single_btn":True,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#1 创建订单
# 并获取 该订单符合的优惠券
class PayCreateOrder( ListView):
	def get(self, request, *args, **kwargs):
		try:

			# print "is_member_order:",_is_member_order
			_is_member_order = request.GET.get('is_member_order',"")
			_tag_id = request.GET.get('tag_id',"")
			_role_id = request.GET.get('role_id',"")
			_article_id = request.GET.get('article_id',"")
			_user = User.objects.get( session =  request.GET.get('session',""))

			_dict = {}
			#创建订单
			_hx_order = HX_Order()
			_hx_discount = HX_Discount()
			if _is_member_order == 'true':
				_order_dict = _hx_order.AddMemberOrder(_user.id,_tag_id,_role_id)
				_dict["discount_list"] = _hx_discount.GetMemberByUser(_user.id,_tag_id,_role_id) #获取会员优惠券
			else:
				_order_dict,_article = _hx_order.AddSingleOrder(_user.id,_article_id)
				_dict["article_title"] = _article.title
				_dict["discount_list"] = _hx_discount.GetSingleByUser(_user.id) #获取点播优惠券
			#TODO 点播订单

			#获取优惠券
			_user = User.objects.get( session =  request.GET.get('session',""))


			_dict["order_dict"] = _order_dict
			# _dict["discount_list"] = _discount_list
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#Todo UpdateOrder 附带Discount
# lite 确认支付按钮提交订单和优惠券
class PayConfirmOrder( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_order_id = request.GET.get('order_id',"")
			_discount_id = request.GET.get('discount_id',"")
			_user = User.objects.get( session =  request.GET.get('session',""))

			_hx_order = HX_Order()
			_order = _hx_order.PayPrepare(_order_id,_discount_id)
			if _order.payment_fee == 0: #金额为0，支付成功
				_dict = {"is_zero":True}
				_hx_order.PayComplete(_order.id)
			else: #存在金额，调取微信支付
				_dict = _hx_order.PayWX(_user,_order)
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#3 微信支付回调
class PayWxCallback( ListView):
	def post(self, request, *args, **kwargs):
		try:
			_xml_request =  request.body
			print _xml_request
			_hx_order = HX_Order()
			_xml_resualt = _hx_order.PayWXCallback(_xml_request)
			print _xml_resualt
			return HttpResponse( _xml_resualt,content_type="application/xml")
		except Exception,e :
			print e
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

	def get(self, request, *args, **kwargs):
		try:
			_dict = {
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#获取我的会员
class PayGetListMember( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session =  request.GET.get('session',""))
			# _order = HX_Order()
			# _member_list = _order.GetMemberBySelf(_user.id) #获取会员优惠券
			_role = HX_Role()
			_member_list = _role.GetMemberListByUser(_user.id) #获取会员优惠券


			_dict = {
				"member_list":_member_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#获取我的所有优惠券
class PayGetListDiscount( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session =  request.GET.get('session',""))
			_hx_discount = HX_Discount()
			_discount_list = _hx_discount.GetBySelf(_user.id) #获取会员优惠券
			_dict = {
				"discount_list":_discount_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



#TODO 2018 - 2 - 4 增加
from ..action.action_pay import *
actionPay = ActionPay()
#1 获取协议
class PayGetProtocolByID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			protocol_dict = actionPay.GetProtocolByID()
			_dict = {
				"protocol_dict":protocol_dict,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 创建续费的微信支付验证对象
class PayConfirmRenew( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_renew_order_id = request.GET.get('renew_order_id',"")
			_order_id = request.GET.get('order_id',"")
			_discount_id = request.GET.get('discount_id',"")
			_user = User.objects.get( session =  request.GET.get('session',""))

			_hx_order = HX_Order()
			_order = _hx_order.PayRenewPrepare(_order_id,_discount_id,_renew_order_id)
			if _order.payment_fee == 0: #金额为0，支付成功
				_dict = {"is_zero":True}
				_hx_order.PayComplete(_order.id)
			else: #存在金额，调取微信支付
				_dict = _hx_order.PayRenewWX(_user,_order)
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#3 续费支付返回
class PayWxCallbackRenew( ListView):
	def post(self, request, *args, **kwargs):
		try:
			_xml_request =  request.body
			print _xml_request
			_hx_order = HX_Order()
			_xml_resualt = _hx_order.PayRenewWXCallback(_xml_request)
			print _xml_resualt
			return HttpResponse( _xml_resualt,content_type="application/xml")
		except Exception,e :
			print e
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )






#4
# class PayZeroCallback( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_hx_order = HX_Order()
# 			if _o.payment_fee == 0:
# 				_dict = {"is_zero":"true"}
# 				_order.PayComplete()
# 			_dict = {
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )