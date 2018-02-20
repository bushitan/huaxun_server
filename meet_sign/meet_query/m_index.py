#coding:utf-8
from meet.meet_query.m_base import *
from meet.models import *
class M_Index(M_Base):
    #用于封面展示的数据
    def _Pack(self,query_get):
        return {
            "page_id":query_get.id,
            "name":query_get.name,
            "name_admin": query_get.name_admin,
        }

    # 获取所有页面的id列表
    def GetPageListByLiteAppID(self,app_id):
        #TODO 把1维数组分成2维列表
        _query = Page.objects.filter(lite__app_id=app_id)
        return self._PackList(self._Pack,_query)
