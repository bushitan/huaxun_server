#coding:utf-8
from meet.lib.query_base import *
from meet_sign.models import *
class QueryCost(QueryBase):
	def __init__(self):
		super(QueryCost,self).__init__(Cost)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
			"name":query_get.name,
			"des":query_get.des,
			# "meet_name":query_get.meet.name if query_get.meet is not None else "",
			"unit_price": query_get.unit_price,
		}

if __name__ == "__main__":
	import os,django
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huaxun_server.settings")
	django.setup()
	q = QueryCost()
	print q.Filter(meet__status = MEET_START)