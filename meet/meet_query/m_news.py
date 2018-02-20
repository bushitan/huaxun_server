#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_News(M_Base):
    #用于封面展示的数据
    def _Pack(self,query_get):
        return {
            "news_id":query_get.id,
            "news_name":query_get.name,
            "cover_url":query_get.cover_image.url if query_get.cover_image is not None else "",
            "article_id":query_get.article_id,
            "title": query_get.title,
            "summary":query_get.summary,
            "des":query_get.des,
            "footer":query_get.footer,
        }
    #获取列表
    def GetListByMeetId(self,meet_id):
        if meet_id == "" :
            return []
        _query = News.objects.filter(meet_id=meet_id)
        if _query.exists() is False:
            return []
        return self._PackList(self._Pack,_query)
