#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_Agenda(M_Base):
    #用于封面展示的数据
    def _Pack(self,query_get):
        return {
            "agenda_id":query_get.id,
            "agenda_name":query_get.name,
            "article_id":query_get.article_id,

            "title": query_get.title,
            "summary":query_get.summary,
            "des":query_get.des,
            "footer":query_get.footer,
            # "start_time":query_get.start_time.strftime("%Y-%m-%d"),
            "start_time":query_get.start_time.strftime("%H:%M"),
            "end_time":query_get.end_time.strftime("%H:%M"),
            # "end_time":query_get.end_time.strftime("%h:%M"),
        }
    #获取列表
    def GetListByMeetId(self,meet_id):
        #TODO 把1维数组分成2维列表
        if meet_id == "" :
            return []
        _query = Agenda.objects.filter(meet_id=meet_id)
        if _query.exists() is False:
            return []
        return self._PackList(self._Pack,_query)
