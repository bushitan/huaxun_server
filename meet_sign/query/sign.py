#coding:utf-8
from meet_sign.query.base import *
from meet_sign.models import *
class QueryCost(Base):
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
			"name":query_get.name,
			"des":query_get.des,
			# "meet_name":query_get.meet.name if query_get.meet is not None else "",
			"unit_price": query_get.unit_price,
		}
	def QCurrentCostList(self):
		_query = Cost.objects.filter(meet__status = MEET_START)
		return self._PackList(self._PackDict,_query)

if __name__ == "__main__":
	import os,django
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huaxun_server.settings")
	django.setup()
	q = QueryCost()
	print q.QCurrentCostList()