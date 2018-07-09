#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from action.api308 import *
from action.user import *
action_api = ActionAPI308()
action_user = ActionUser()

# 计时器
def time_token():
    import threading
    def fun_timer():
        print('Hello Timer!')
        action_api.create()
        global timer
        timer = threading.Timer(1024, fun_timer)
        timer.start()
    timer = threading.Timer(0, fun_timer)
    timer.start()
time_token()
## 增加线程，90分钟刷新一次
## 小程序通过后台查询，
## 如果token过期，返回小程序404,让小程序重新发起查询

#1 进入快讯，初始化
# class TokenCreate( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			a = action_api.create()
# 			_dict = {
# 				"token":a
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

	#1 用户登录
class TokenLogin( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_js_code = request.GET.get('js_code',"")
			_session = request.GET.get('session',"")
			print _js_code
			openid,session = action_api.token_login(_js_code,_session)
			# openid,session = "ozTYA0Qvq6nBc9Fs167X29kW25G0","wybOqIPZWgyTI1TJClK0jQ=="
			token = action_api.token_get()
			_dict = {
				"openid":openid,
				"session":session,
				"token":token,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#1 获取token
class TokenGet( ListView):
	def get(self, request, *args, **kwargs):
		try:
			a = action_api.token_get()
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