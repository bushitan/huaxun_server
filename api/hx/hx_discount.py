#coding:utf-8

from api.hx.hx_base import *
from order.models import *
from api.lib.util import *

class HX_Discount(HX_Base):
	def __init__(self):
		pass
	def _PackDict(self,query_get):
		_dict = {
			"discount_id":query_get.id,
			"discount_name":query_get.template.name,
			"discount_fee":query_get.template.fee,
			"agreement_type":query_get.template.agreement_type,
			"use_condition":query_get.template.use_condition,
			"use_range":query_get.template.use_range,
			"start_time":query_get.start_time.strftime("%Y-%m-%d"),
			"end_time":query_get.end_time.strftime("%Y-%m-%d"),
		}
		return _dict

	# 1 我的优惠券列表
	def GetBySelf(self,user_id):
		_now = datetime.datetime.now()
		_discount_query = Discount.objects.filter(
			user_id = user_id ,
			is_used = DISCOUNT_IS_USED_FALSE,
			is_active = DISCOUNT_IS_ACTIVE_TRUE,
			# template__agreement_type = AGREEMENT_TYPE_MEMBER,
			# template__limit_fee__lte = _original_fee,  # 最低限制价格  小于等于 原始价格
			start_time__lt  = _now,
			end_time__gt = _now,
		)
		return  self._PackList( self._PackDict,_discount_query)

	# 2 会员支付——获取单张会员券
	def GetMemberByUser(self,user_id,tag_id,role_id):
		_now = datetime.datetime.now()
		_discount_query = Discount.objects.filter(
			user_id = user_id ,
			is_used = DISCOUNT_IS_USED_FALSE,
			is_active = DISCOUNT_IS_ACTIVE_TRUE,
			template__agreement_type = AGREEMENT_TYPE_MEMBER,
			# template__limit_fee__lte = _original_fee,  # 最低限制价格  小于等于 原始价格
			start_time__lt  = _now,
			end_time__gt = _now,
		)
		return  self._PackList( self._PackDict,_discount_query)

	# 3 点播支付——获取单张点播券
	def GetSingleByUser(self,user_id,):
		_now = datetime.datetime.now()
		_discount_query = Discount.objects.filter(
			user_id = user_id ,
			is_used = DISCOUNT_IS_USED_FALSE,
			template__agreement_type = AGREEMENT_TYPE_SINGLE_TIME,
			# template__limit_fee__lte = _original_fee,  # 最低限制价格  小于等于 原始价格
			start_time__lt  = _now,
			end_time__gt = _now,
		)
		return  self._PackList( self._PackDict,_discount_query)

