#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_Agenda(M_Base):
    #用于封面展示的数据
    def _Pack(self,query_get):
        return {
            "guest_id":query_get.guest_id,
            "name":query_get.name,
            "logo_url": query_get.logo_image.url if query_get.logo_image is not None else "",
            "company":query_get.company,
            "introduction":query_get.introduction,
        }
    #获取列表
    def GetListByMeetId(self,meet_id):
        #TODO 把1维数组分成2维列表
        _query = Guest.objects.filter(meet__id=meet_id)
        return self._PackList(self._Pack,_query)

    # def GetByGuestId(self,guest_id):
    #     #TODO 把1维数组分成2维列表
    #     _query = Guest.objects.get(id=guest_id)
    #     return self._PackList(self._Pack(_query))
