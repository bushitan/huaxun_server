# -*- coding: utf-8 -*-

# from django.http import HttpResponse
# import json
from api.lib.message import *
# from api.models.user import *
# from api.hx.hx_role import *
from meet_sign.models import *
import json

class SessionMiddleware(object):
	def process_request(self, request):
		try:
		#检查是否有session值传入
		#有，则判断是否存在
			_items = request.GET.dict()
			if _items.has_key("meet_session"):  	#session字段存在
				session = request.GET.get('meet_session',"") #获取session
				if  Attendee.objects.filter( session = session).exists() is False: #用户不存在
					if _items.has_key("js_code") is False: # js_code为登陆验证字段，若不存在，返回登陆失败
						return MESSAGE_RESPONSE_LOGIN_OUT()
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

	def process_response(self, request, response):
		# print "process_response"
		# _session = request.GET.get('session',"") #获取session
		#
		# try: #不是json格式，不解析
		# 	_content = json.loads(response.content)
		# 	if _content.has_key('check'):
		# 		_role = HX_Role()
		# 		_resualt = _role.CheckResponse(_session,_content)
		# 		if _resualt is True:
		# 			return response
		# 		else :
		# 			return _resualt
		# except:
		# 	return response
		return response


		# print 1,type(_content),_content['role_check']

			# print 112231
		# print response.GET.get('role_check',"") #获取session
		# print response.GET.get('article_dict',"") #获取session
# print request.GET.lists()
# print request.GET.items()
# print request.GET.values()
# print request.GET.dict()