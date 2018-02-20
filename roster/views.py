#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from api.hx.hx_roster import HX_Roster

#2 会议页面列表
class RosterIndex( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_session = request.GET.get('session',"")
			_start_index = int(request.GET.get('start_index',""))
			_range = 20 #默认查询范围
			_tag_id = 16 #默认目录
			_roster = HX_Roster()
			_roster_list = _roster.GetListByTagRange(_tag_id ,_start_index ,_start_index+_range)
			_dict = {
				'roster_list':_roster_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#根据标签查
class RosterGetListByTagCompany( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_session = request.GET.get('session',"")
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_range = 20 #默认查询范围
			_roster = HX_Roster()
			_roster_list = _roster.GetListByTagRange(_tag_id ,_start_index ,_start_index+_range)
			_dict = {
				'roster_list':_roster_list,
			}

			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#获取详细内容
class RosterGetDictByID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_roster_id = request.GET.get('roster_id',"")
			_roster = HX_Roster()
			_roster_dict = _roster.GetDictById(_roster_id)
			_dict = {
				'roster_dict':_roster_dict,
			}

			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#获取详细内容
class RosterSearch( ListView):
	def get(self, request, *args, **kwargs):
		try:

			_session = request.GET.get('session',"")
			_key_word = request.GET.get('key_word',"")
			_roster = HX_Roster()
			_roster_list = _roster.SearchByCompany(_key_word)
			_dict = {
				'roster_list':_roster_list,
			}

			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
