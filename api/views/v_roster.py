#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from api.hx.hx_roster import *

#1 根据tag查列表
class RosterGetListByTag( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_roster = HX_Roster()
			_roster_list = _roster.GetListByTagRange(_tag_id ,_start_index ,_end_index)
			_dict = {
				'article_list':_roster_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#2 搜索公司名字
class RosterGetListBySearch( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_session = request.GET.get('session',"")
			_keyword_title = request.GET.get('keyword_title',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_tag_id = request.GET.get('tag_id',"")

			_roster = HX_Roster()
			_roster_list = _roster.SearchByCompany(_keyword_title,_start_index,_end_index,_tag_id)
			_dict = {
				'article_list':_roster_list,
			}

			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 按标签，查看搜索的
class RosterGetListByMatch( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_session = request.GET.get('session',"")
			_is_buy = request.GET.get('is_buy',"")
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")

			_roster = HX_Roster()
			if int(_is_buy) == YES:
				_roster_list = _roster.SearchByBuy(_tag_id,_start_index,_end_index)
			else:
				_roster_list = _roster.SearchBySell(_tag_id,_start_index,_end_index)
			_dict = {
				'article_list':_roster_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 按标签，查看搜索的
class RosterGetListByArea( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_session = request.GET.get('session',"")
			_area_id = request.GET.get('area_id',"")
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")

			_roster = HX_Roster()

			_roster_list = _roster.SearchByArea(_area_id,_tag_id,_start_index,_end_index)
			_dict = {
				'article_list':_roster_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#3 获取区域列表
class RosterGetAreaList( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_roster = HX_Roster()
			_area_list = _roster.GetAreaList()
			_dict = {
				'area_list':_area_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#2 查看花名册详细信息
class RosterGetByID( ListView):
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



#3 上传花名册信息
class RosterSetBySelf( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_session = request.GET.get('session',"")
			#TODO 花名册的内容
			_name = request.GET.get('user_name',"")
			_introduction = request.GET.get('introduction',"")
			_phone = request.GET.get('phone',"")
			_address =  request.GET.get('address',"")
			_latitude =  request.GET.get('latitude',"")
			_longitude =  request.GET.get('longitude',"")

			_roster = HX_Roster()
			_roster.SetByUser(_session,_name,_introduction,_phone ,_address ,_latitude ,_longitude)
			_dict = {
				"msg":u"更新花名册成功"
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#4 查看花名册详细信息
# 用户填写花名册时，先查看自己的信息
class RosterGetBySelf( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session =  request.GET.get('session',""))
			_roster = HX_Roster()
			_roster_dict = _roster.GetDictByUser(_user.id)
			_dict = {
				'roster_dict':_roster_dict,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

