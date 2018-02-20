#coding:utf-8
from meet.meet_query.m_base import *
from django.utils.timezone import now, timedelta
from meet.models import *
class M_Article(M_Base):
    #用于封面展示的数据
    def _PackCover(self,query_get):
        return {
            "name":query_get.name,
            "type":query_get.type,

            "title":query_get.title,
            "summary":query_get.summary,
            "des":query_get.des,
            "footer":query_get.footer,
            "start_date":query_get.start_time.issue_time.strftime(u"%m月%d日"),  #开始日期
            "start_time":query_get.start_time.issue_time.strftime("%h:%M"),
            "end_time":query_get.end_time.issue_time.strftime("%h:%M"),
            "article_id": query_get.article_id,
        }

    def _PackArticle(self,query_get):
        return {
            "title":query_get.title,
            "des":query_get.des,
            "footer":query_get.footer,
            "date_time":query_get.start_time.issue_time.strftime(u"%m月%d日"),
            "start_time":query_get.start_time.issue_time.strftime("%h:%M"),
            "end_time":query_get.end_time.issue_time.strftime("%h:%M"),
            "article_id": query_get.article_id,
        }
    #获取列表
    def GetCoverListByPageMeet(self,page_id,meet_id):
        #TODO 把1维数组分成2维列表
        _query = ArticleCover.objects.filter(page_id = page_id,meet_id=meet_id)
        return self._PackList(self._PackCover,_query)


    #获取列表
    def GetArticleByArticleID(self,article_id):
        _query = ArticleLibrary.objects.get(article_id = article_id )
        return self._PackArticle(_query )




















