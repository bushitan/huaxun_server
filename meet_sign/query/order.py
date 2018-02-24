#coding:utf-8
from meet.lib.query_base import *
from meet_sign.models import *
class QueryOrder(QueryBase):
	def __init__(self):
		super(QueryOrder,self).__init__(Order)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
			"order_id":query_get.id,
			"is_alive":query_get.is_alive,
			"is_pay":query_get.is_pay,
			"wx_out_trade_no":query_get.wx_out_trade_no,
			"origin_price":query_get.origin_price,
			"pay_price":query_get.pay_price,
			"remark":query_get.remark,
			"create_time": query_get.create_time.strftime("%Y-%m-%d"),
		}

if __name__ == "__main__":
	import os,django
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huaxun_server.settings")
	django.setup()
	q = QueryOrder()
	print q.Filter(meet__status = MEET_START)