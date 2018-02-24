#coding:utf-8

from meet.lib.query_base import *
from meet.models import *
class QueryGuest(QueryBase):
	def __init__(self):
		super(QueryGuest,self).__init__(Guest)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
            "guest_id":query_get.id,
            "guest_name":query_get.name,
            "article_id":query_get.article_id,
            "cover_url": query_get.logo_image.url if query_get.logo_image is not None else "",
            "company":query_get.company,
            "introduction":query_get.introduction,
		}

if __name__ == "__main__":
	a = QueryGuest()
	print a.Filter()