#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_Article(M_Base):
    def _Pack(self,query_get):
        return {
            "article_id": query_get.id,
            "click_rate":query_get.click_rate,
            "title":query_get.title,
            "subtitle":query_get.subtitle,
            "summary":query_get.summary,
            "source":query_get.source,
##            "date_time":query_get.start_time.issue_time.strftime(u"%m月%d日"),
##            "start_time":query_get.start_time.issue_time.strftime("%h:%M"),
##            "end_time":query_get.end_time.issue_time.strftime("%h:%M"),
        }

    #获取列表
    def GetArticleByArticleID(self,article_id):
        if article_id == "" :
            return ""
        _query = ArticleLibrary.objects.filter(id = article_id)
        if _query.exists() is False:
            return ""
        return self._Pack( _query[0] )




















