#coding:utf-8
from meet.lib.query_base import *
from meet_sign.models import *
class QuerySign(QueryBase):
	def __init__(self):
		super(QuerySign,self).__init__(Sign)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
			"sign_id":query_get.id,
			"attendee_id":query_get.attendee_id,
			"attendee_wx_open_id":query_get.attendee.wx_open_id if query_get.attendee is not None else '' ,
			"cost_id":query_get.cost.name,
			"cost_unit_price":query_get.cost.unit_price if query_get.cost is not None else 0,
			"is_alive":query_get.is_alive,
		}

	def UpdatePaySuccess(self,sign_id):
		_query = Sign.objects.get(id = sign_id)
		_query.is_alive = YES
		_query.save()
		return _query


	# # 创建支付订单，获取已经创建的登陆状态，没有，则新增
	# def APayPrepare(self,attendee_id,cost_id):
	# 	if self.IsExists(
	# 		attendee_id = attendee_id,
	# 		cost_id = cost_id,
	# 	) is True:
	# 		return self.QDict(
	# 			attendee_id = attendee_id,
	# 			cost_id = cost_id,
	# 		)
	# 	else:
	# 		return self.ADict(
	# 			attendee_id = attendee_id,
	# 			cost_id = cost_id,
	# 			is_alive = NO,
	# 	  	)

if __name__ == "__main__":
	import os,django
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huaxun_server.settings")
	django.setup()
	q = QuerySign()
	# print q.QCurrentCostList()