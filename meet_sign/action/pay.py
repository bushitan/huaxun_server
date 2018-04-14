#coding:utf-8
from meet_sign.query.attendee import *
from meet_sign.query.order import *
from meet_sign.query.sign import *
from meet.lib.wx_pay import *
import json
import urllib2
import random
from django.db import transaction #事务

APP_ID = "wx3efaa3a88f42df6b"
APP_SECRET = "2b4f979499f140c061f123a110accfce"
MACH_ID = "1488713872"
MACH_KEY = "283fc3d9d4b8ba3b58601145466d4417"
PAY_CALLBACK_URL = "https://xcx.308308.com/huaxun_2/meet/sign/pay/callback/"

class ActionPay():
	def __init__(self):
		self.query_attendee = QueryAttendee()
		self.query_order = QueryOrder()
		self.query_sign = QuerySign()

	def CheckIsPay(self,s_sesson,meet_id):
		# self.query_attendee.Get(session=s_sesson)
		return self.query_sign.IsExists(
			attendee__session = s_sesson,
			cost__meet_id = meet_id,
			is_alive = YES,
		)
	def GetInfo(self,s_sesson,meet_id):
		# self.query_attendee.Get(session=s_sesson)
		return self.query_sign.Filter(
			attendee__session = s_sesson,
			cost__meet_id = meet_id,
			is_alive = YES,
		)
	def WXPaySuccess(self,xml_request):
		xh = XMLHandler()
		xml.sax.parseString( xml_request, xh)
		_xml_dict = xh.getDict()
		_out_trade_no = _xml_dict["out_trade_no"]
		_total_fee = _xml_dict["total_fee"]
		_xml_resualt = '''
			<xml>
			  <return_code><![CDATA[%s]]></return_code>
			  <return_msg><![CDATA[%s]]></return_msg>
			</xml>
		'''
		with transaction.atomic():
			_q_order = self.query_order.FilterQuery( wx_out_trade_no = _out_trade_no )
			if len(_q_order) == 0:
				return xml_request%("FAIL",u"订单不存在")
			else:
				self.query_order.Update(_q_order, is_pay = YES)
				_sign_is = _q_order[0].sign_id

				_q_sign = self.query_sign.FilterQuery( id =_sign_is )
				self.query_sign.Update(_q_sign,is_alive = YES)
				# return True
				return xml_request%("SUCCESS",u"支付成功" + str(_out_trade_no))
		#返回结果

	# 创建微信支付的签名
	# 1、将  与会者 和 花费项目 绑定为sign中，alive未激活
	# 2、创建未支付的order订单
	# 3、生成微信支付sign
	def WXPaySign(self,s_session,s_cost_id):
		with transaction.atomic():
			#1 添加报名表
			_d_sign =  self._CreateSignNoAlive(s_session,s_cost_id)
			#2 添加订单
			_d_order = self._CreateOrderNoPay(_d_sign)
			#3 生成微信支付签名
			_total_fee = str( int( _d_order['pay_price'] *100) )

			_wx_pay = WXPay(
				APP_ID,
				APP_SECRET,
				MACH_ID,
				MACH_KEY,
				_d_sign['attendee_wx_open_id'] ,
				_d_order['wx_out_trade_no'] ,
				_total_fee ,
				PAY_CALLBACK_URL
			)
			_dict  =  _wx_pay.get_request_payment()
			return _dict

	# 创建未支付的订单
	def _CreateOrderNoPay(self,d_sign):
		if self.query_order.IsExists(
			sign_id = d_sign["sign_id"],
			is_pay = NO,
			is_alive = YES,
		) is True:
			return self.query_order.Get(
				sign_id = d_sign["sign_id"],
				is_pay = NO,
				is_alive = YES,
			)
		else:
			_trade = str(
				datetime.datetime.now().strftime("%Y%m%d%H%M%S")) \
				+ str(d_sign["sign_id"]) \
				+ str(int(random.random() * 1000)
		  	)
			return self.query_order.Add(
				sign_id = d_sign["sign_id"],
				is_pay = NO,
				is_alive = YES,
				wx_out_trade_no = _trade,
				origin_price = d_sign["cost_unit_price"],
				pay_price = d_sign["cost_unit_price"],
		  	)
	# 获取  与会者 和 花费项目 绑定为sign中，alive未激活
	def _CreateSignNoAlive(self,s_session,cost_id):
		_att = self.query_attendee.GetQuery(session = s_session)
		if self.query_sign.IsExists(
			attendee_id = _att.id,
			cost_id = cost_id,
			is_alive = NO,
		) is True:
			return self.query_sign.Get(
				attendee_id = _att.id,
				cost_id = cost_id,
				is_alive = NO,
			)
		else:
			return self.query_sign.Add(
				attendee_id = _att.id,
				cost_id = cost_id,
				is_alive = NO,
		  	)


if __name__ == "__main__":
	import os,django
	django.setup()
	b = ActionPay()
	# print b.WXPaySign('112',2)
	# print b.CheckIsPay("aScV8V3uN8gEvN2cRnlIqA==","1")
	_xml = '''
		<xml>
		 	<out_trade_no>201804141617491526</out_trade_no>
		  	<total_fee>0.01</total_fee>
		</xml>
	'''
	print b.WXPaySuccess(
		_xml

	)
	# b.SetInfo('112')