#coding:utf-8
import json
from django.views.generic import ListView
from api.lib.util import *
from api.lib.message import *


#2 会议页面列表
class Index( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_dict = {
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

