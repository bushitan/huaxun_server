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


#1 进入快讯，初始化
class CMSGetIndustry( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_dict = {
				"token":action_api.cms_get_all_industry()
			}
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