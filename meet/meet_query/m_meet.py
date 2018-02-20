#coding:utf-8
from meet.meet_query.m_base import *
from meet.models import *
class M_Meet(M_Base):
    #用于封面展示的数据
    
    def _Pack(self,query_get):
        return {
            "meet_id":query_get.id,
            "meet_name": query_get.name,
            "des": query_get.des, 
            "status": query_get.status, 
            "serial": query_get.serial, 
            "address": query_get.address, 
            "latitude": query_get.latitude, 
            "longitude": query_get.longitude, 
        }
    def GetCurrent(self):
        _query = Meet.objects.filter(status = MEET_START) #最新的主会议
        if _query.exists() is False:
            return ""
        return self._Pack(_query[0])
    def GetAgendaList(self,meet_id):
        _query = Meet.objects.filter(father_id = meet_id,style = MEET_AGENDA) #最新的主会议
        return self._PackList(self._Pack,_query)
    def GetSpotList(self,meet_id):
        _query = Meet.objects.filter(father_id = meet_id,style = MEET_SPOT) #最新的主会议
        return self._PackList(self._Pack,_query)
    
##    # 获取所有页面的id列表
##    def GetPageListByLiteAppID(self,app_id):
##        #TODO 把1维数组分成2维列表
##        _query = Page.objects.filter(lite__app_id=app_id)
##        return self._PackList(self._Pack,_query)
