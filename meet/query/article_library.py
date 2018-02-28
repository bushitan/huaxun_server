#coding:utf-8

from meet.lib.query_base import *
from meet.models import *
class QueryArticleLibrary(QueryBase):
	def __init__(self):
		super(QueryArticleLibrary,self).__init__(ArticleLibrary)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
            "article_id": query_get.id,
            "style":query_get.style,
            "click_rate":query_get.click_rate,
            "title":query_get.title,
            "subtitle":query_get.subtitle,
            "content":query_get.content,
            "summary":query_get.summary,
            "source":query_get.source,
		}

if __name__ == "__main__":
	a = QueryArticleLibrary()
	print a.Filter()