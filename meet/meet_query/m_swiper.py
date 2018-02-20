#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_Swiper(M_Base):
    #用于封面展示的数据
    def _Pack(self,query_get):
        return {
            "swiper_id":query_get.id,
            "swiper_name":query_get.name,
            "cover_url": query_get.cover_image.url if query_get.cover_image is not None else "",
            "article_id":query_get.article_id,
            "title": query_get.title,
            "summary":query_get.summary,
            "des":query_get.des,
            "footer":query_get.footer,
        }
    #获取列表
    def GetListByStyle(self,meet_id,style):
        #TODO 把1维数组分成2维列表
        _query = Swiper.objects.filter(meet_id = meet_id,style=style)
        if _query.exists()  is False:
            return []
        return self._PackList(self._Pack,_query)
