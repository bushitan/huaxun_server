#coding:utf-8

from django.db import transaction #事务

from api.hx.hx_role import *
from api.lib.wx_api import *


class HX_Order(HX_Base):
	def __init__(self):
		pass
	def _PackDict(self,query_get):
		_dict = {
			'order_id':query_get.id,
			'tag_id':query_get.tag_id if query_get.tag is not None else "",
			'tag_name':query_get.tag.name if query_get.tag is not None else "",
			'role_id':query_get.role_id if query_get.role is not None else "",
			'role_name':query_get.role.name if query_get.role is not None else "",
			'original_fee':query_get.original_fee,
			'payment_fee':query_get.payment_fee,
			# 'order_id':query_get.id,
			# 'tag_name':query_get.name,
			# 'father_id' : query_get.father_id if query_get.father is not None else "" ,
			# 'father_name' : query_get.father.name if query_get.father is not None else "" ,
		}
		return _dict
	# 1 用户点击 会员支付 —— 创建会员订单
	def AddMemberOrder(self,user_id,tag_id,role_id):
		is_member = True
		_order = self._GetByCheck(user_id,is_member)
		_order.agreement_type = AGREEMENT_TYPE_MEMBER
		# _order.original_fee = self._GetPayFee(user_id,tag_id,role_id)
		# _fee =
		_order.original_fee =  Role.objects.get(id = role_id).price #直接拿当前的价格
		_order.tag_id = tag_id
		_order.role_id = role_id
		_order.save()
		return self._PackDict(_order)

	# 2 用户点击 就看这篇 —— 创建会员订单
	def AddSingleOrder(self,user_id,article_id):
		is_member = False
		_article = Article.objects.get(id=article_id)
		_order = self._GetByCheck(user_id,is_member)
		_order.article = _article
		_order.agreement_type = AGREEMENT_TYPE_SINGLE_TIME
		_order.original_fee = _article.price
		_order.save()
		return self._PackDict(_order) , _article


	# 3 用户点击 确认支付 —— 将订单与优惠券融合
	# 3.1优惠券不存在，用原价
	# 3.2 优惠券存在，计算新价格
	# return 订单信息
	def PayPrepare(self,order_id,discount_id):
		_order =  Order.objects.get(id = order_id)
		#Todo 验证优惠券是否有效

		if discount_id == "": #优惠券不存在
			_order.payment_fee = _order.original_fee
		else: #优惠券存在
			_order.discount_id = discount_id
			_fee = _order.original_fee - _order.discount.template.fee
			if _fee < 0:
				_fee = 0  #价格为负数，变0
			_order.payment_fee = float(_fee)
		_order.save()
		# self.order = _order
		return _order

	#续费的订单准备
	def PayRenewPrepare(self,order_id,discount_id,renew_order_id):
		_order =  Order.objects.get(id = order_id)
		#Todo 验证优惠券是否有效
		_order.renew_order_id = renew_order_id
		if discount_id == "": #优惠券不存在
			_order.payment_fee = _order.original_fee
		else: #优惠券存在
			_order.discount_id = discount_id
			_fee = _order.original_fee - _order.discount.template.fee
			if _fee < 0:
				_fee = 0  #价格为负数，变0
			_order.payment_fee = float(_fee)
		_order.save()
		# self.order = _order
		return _order


	# 4-1 金额为0，直接支付成功
	# 4.1 原价为0
	# 4.2 使用优惠券后价格为0
	def PayComplete(self,order_id):
		_order = Order.objects.get(id = order_id)
		with transaction.atomic():
			_order.is_payment = IS_PAYMENT_TRUE
			if _order.discount is not None:
				print _order.discount_id
				_discount = Discount.objects.get(id = _order.discount_id )
				_discount.is_used = DISCOUNT_IS_USED_TRUE
				_discount.save()
			_order.save()
		return True

	# 4-2 金额不为0，调用微信支付
	def PayWX(self,user,order):
		_user = user
		_order = order
		_fee = str( int(_order.payment_fee *100) )  #把圆换算为分，并用整数表示
		_wx_pay = wx_pay( _user.wx_open_id , _order.wx_out_trade_no ,_fee , SETTINGS.PAY_CALLBACK_URL)
		_dict  =  _wx_pay.get_request_payment()
		return _dict

	# 续费支付二维码信息
	def PayRenewWX(self,user,order):
		_user = user
		_order = order
		_fee = str( int(_order.payment_fee *100) )  #把圆换算为分，并用整数表示
		_wx_pay = wx_pay( _user.wx_open_id , _order.wx_out_trade_no ,_fee , SETTINGS.PAY_RENEW_CALLBACK_URL)
		_dict  =  _wx_pay.get_request_payment()
		return _dict

	# 4-3 微信支付回调
	# 更改数据库为支付成功
	def PayWXCallback(self,_xml):
		xh = XMLHandler()
		xml.sax.parseString( _xml, xh)
		_xml_dict = xh.getDict()
		_out_trade_no = _xml_dict["out_trade_no"]
		_total_fee = _xml_dict["total_fee"]
		#返回结果
		_xml_resualt = '''
			<xml>
			  <return_code><![CDATA[%s]]></return_code>
			  <return_msg><![CDATA[%s]]></return_msg>
			</xml>
		'''

		if Order.objects.filter(wx_out_trade_no = _out_trade_no ).exists() is False:
			return _xml_resualt%("FAIL",u"订单不存在")
		_order = Order.objects.get(wx_out_trade_no = _out_trade_no )

		if _order.is_payment == IS_PAYMENT_TRUE:
			return _xml_resualt%("FAIL",u"已经支付")
		if str( int( _order.payment_fee * 100) ) != _total_fee:
			return _xml_resualt%("FAIL",u"金额不一致")

		#支付成功
		with transaction.atomic():
			_order.is_payment = IS_PAYMENT_TRUE # 订单状态->支付
			if _order.discount is not None:    # 优惠券非空 订单状态->支付
				print _order.discount_id
				_discount = Discount.objects.get(id = _order.discount_id )
				_discount.is_used = DISCOUNT_IS_USED_TRUE
				_discount.save()
			_order.save()
		return _xml_resualt%("SUCCESS",u"支付成功")


	# 4-3 续费微信返回
	def PayRenewWXCallback(self,_xml):
		xh = XMLHandler()
		xml.sax.parseString( _xml, xh)
		_xml_dict = xh.getDict()
		_out_trade_no = _xml_dict["out_trade_no"]
		_total_fee = _xml_dict["total_fee"]
		#返回结果
		_xml_resualt = '''
			<xml>
			  <return_code><![CDATA[%s]]></return_code>
			  <return_msg><![CDATA[%s]]></return_msg>
			</xml>
		'''

		if Order.objects.filter(wx_out_trade_no = _out_trade_no ).exists() is False:
			return _xml_resualt%("FAIL",u"订单不存在")
		_order = Order.objects.get(wx_out_trade_no = _out_trade_no )

		if _order.is_payment == IS_PAYMENT_TRUE:
			return _xml_resualt%("FAIL",u"已经支付")
		if str( int( _order.payment_fee * 100) ) != _total_fee:
			return _xml_resualt%("FAIL",u"金额不一致")

		#支付成功
		with transaction.atomic():
			# 对原有订单要作废处理
			if  Order.objects.filter(id = _order.renew_order_id ).exists():
				_renew_order = Order.objects.get(id = _order.renew_order_id )
				_renew_order.is_alive = NO
				_renew_order.save()
				#延长时间
				_order.end_time = _renew_order.end_time + datetime.timedelta(days = DAY_MEMBER)

			_order.is_payment = IS_PAYMENT_TRUE # 订单状态->支付
			if _order.discount is not None:    # 优惠券非空 订单状态->支付
				print _order.discount_id
				_discount = Discount.objects.get(id = _order.discount_id )
				_discount.is_used = DISCOUNT_IS_USED_TRUE
				_discount.save()
			_order.save()


		return _xml_resualt%("SUCCESS",u"支付成功")



	# 5 检测订单，用户每一次点击“会员支付”和“我就看这篇”，会创建新的未支付订单
	# 如果未支付订单已存在，则直接修改
	# 未支付，用当前的
	# 已支付，重新创建一个，并更新trade_no
	def _GetByCheck(self,user_id,is_member):
		#订单存在未支付，覆盖 else 创建新订单
		if Order.objects.filter(user_id = user_id,is_payment = IS_PAYMENT_FALSE).exists() is True:
			_order = Order.objects.get(user_id = user_id,is_payment = IS_PAYMENT_FALSE)
		else:
			_order = Order(user_id = user_id )
		_order.wx_out_trade_no = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + str(_order.id) + str(int(random.random() * 1000))
		_order.start_time = datetime.datetime.now()
		_during =  DAY_MEMBER if is_member is True else  DAY_SINGLE #点播3天，会员1年
		_order.end_time = datetime.datetime.now() + datetime.timedelta(days = _during)
		_order.create_time = datetime.datetime.now()
		return _order



























	# #获取当前等级的价格
	# #如果是VIP升级到SUPER_VIP，则要做价钱计算
	# def _GetPayFee(self,user_id,tag_id,role_id):
	#
	# 	_hx_role = HX_Role()
	# 	_fee = _hx_role.GetFeeByID(role_id)
	#
	# 	if int(role_id) == ROLE_SUPER_VIP_ID:
	# 		_now = datetime.datetime.now()
	# 		if Order.objects.filter(
	# 			user_id = user_id ,
	# 			is_payment = IS_PAYMENT_TRUE,
	# 			agreement_type = AGREEMENT_TYPE_MEMBER,
	# 			tag_id = tag_id,
	# 			role_id = ROLE_VIP_ID,
	# 			start_time__lt  = _now,
	# 			end_time__gt = _now,
	# 		).exists() is True:
	# 			_order = Order.objects.get(
	# 				user_id = user_id ,
	# 				is_payment = IS_PAYMENT_TRUE,
	# 				agreement_type = AGREEMENT_TYPE_MEMBER,
	# 				tag_id = tag_id,
	# 				role_id = ROLE_VIP_ID,
	# 				start_time__lt  = _now,
	# 				end_time__gt = _now,
	# 			)
	# 			during = _order.end_time - _now
	# 			vip_fee = Role.objects.get(id=ROLE_VIP_ID).price
	# 			_save_fee =  float(int( int(during.days) * vip_fee/365 ))
	# 			_fee = _fee - _save_fee
	# 	return _fee