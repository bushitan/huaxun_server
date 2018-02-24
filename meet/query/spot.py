#coding:utf-8

from meet.lib.query_base import *
from meet.models import *
class QuerySpot(QueryBase):
	def __init__(self):
		super(QuerySpot,self).__init__(Spot)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
            "spot_id":query_get.id,
            "spot_name":query_get.name,
            "cover_url": query_get.cover_image.url if query_get.cover_image is not None else "",
            "article_id":query_get.article_id,
            "title": query_get.title,
            "summary":query_get.summary,
            "des":query_get.des,
            "footer":query_get.footer,
		}

if __name__ == "__main__":
	a = QuerySpot()
	print a.Filter()