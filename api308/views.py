#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from action.api308 import *
from action.user import *
action_api = ActionAPI308()
action_user = ActionUser()
## 增加线程，90分钟刷新一次
## 小程序通过后台查询，
## 如果token过期，返回小程序404,让小程序重新发起查询

#1 进入快讯，初始化
class TokenCreate( ListView):
	def get(self, request, *args, **kwargs):
		try:
			a = action_api.create()
			_dict = {
				"token":a
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#2 获取所有行业
class CMSGetIndustry( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_dict = {
				"industry_list":action_api.cms_get_all_industry()
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#3 获取行业下的目录
class CMSGetCategoryList( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_industry_id = request.GET.get('industry_id',"")
			_dict = {
				"category_list":action_api.cms_get_categories_by_industry(_industry_id)
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#4 获取文章列表
class CMSGetArticleList( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_industry_id = request.GET.get('industry_id',"")
			_category_id = request.GET.get('category_id',"")
			_rows = request.GET.get('rows',"")
			_page_no = request.GET.get('page_no',"")
			_dict = action_api.cms_get_articles_by_category(_industry_id,_category_id,_rows,_page_no,"release_date","desc" )

			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )




# #1 进入快讯，初始化
# class TokenIndex( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_dict = {
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )