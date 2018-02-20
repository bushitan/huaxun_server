#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_Guest(M_Base):
    #用于封面展示的数据
    def _Pack(self,query_get):
        return {
            "guest_id":query_get.id,
            "guest_name":query_get.name,
            "article_id":query_get.article_id,
            "cover_url": query_get.logo_image.url if query_get.logo_image is not None else "",
            "company":query_get.company,
            "introduction":query_get.introduction,
        }
    #获取列表
    def GetListByMeetId(self,meet_id):
        if meet_id == "" :
            return []
        _query = Guest.objects.filter(meet_id=meet_id)
        if _query.exists() is False:
            return []
        return self._PackList(self._Pack,_query)
