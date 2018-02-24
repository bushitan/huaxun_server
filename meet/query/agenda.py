#coding:utf-8

from meet.lib.query_base import *
from meet.models import *
class QueryAgenda(QueryBase):
	def __init__(self):
		super(QueryAgenda,self).__init__(Agenda)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
            "agenda_id":query_get.id,
            "agenda_name":query_get.name,
            "article_id":query_get.article_id,

            "title": query_get.title,
            "summary":query_get.summary,
            "des":query_get.des,
            "footer":query_get.footer,
            "start_time":query_get.start_time.strftime("%H:%M"),
            "end_time":query_get.end_time.strftime("%H:%M"),
		}

if __name__ == "__main__":
	a = QueryAgenda()
	print a.Filter()