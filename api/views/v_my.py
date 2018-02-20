#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from api.hx.hx_user import *
from api.hx.hx_tag import *
from api.hx.hx_role import *

#1 用户进入小程序，
# 获取session
# 获取tag_list
class MyLogin( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_js_code = request.GET.get('js_code',"")
			_session = request.GET.get('session',"")
			_hx_user = HX_User()
			_user = _hx_user.UserLogin(_js_code ,_session)

			_hx_tag = HX_Tag()
			_tag_matrix = _hx_tag.GetMatrix()#获取标签矩阵
			_tag_father_list = _hx_tag.GetFatherList() #获取父类列表

			_role = HX_Role()
			_user_member_list = _role.GetMemberListByUser(_user.id)	#获取已注册会员数据
			# _user_member_list = []
			_dict = {
				"session":_user.session,
				"user_id":_user.id,
				"logo":_user.logo,
				"nick_name":_user.nick_name,
				"tag_matrix":_tag_matrix,
				"tag_father_list":_tag_father_list,
				"user_member_list":_user_member_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2
class MySetWXInfo( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_session = request.GET.get('session',"")
			_logo_url = request.GET.get('logo_url',"")
			_nick_name = request.GET.get('nick_name',"")
			#TODO 用户地址
			_hx_user = HX_User()
			_hx_user.UserSetWxInfo(
				_session,
				_logo_url,
				_nick_name
			)
			_dict = {
				 "msg":u"上传用户信息成功"
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#3 上传花名册信息
# class MySetRosterInfo( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_session = request.GET.get('session',"")
# 			#TODO 花名册的内容
# 			_logo_url = request.GET.get('logo_url',"")
# 			_dict = {
# 				"msg":u"更新花名册成功"
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#4 用户登录后获取头像，昵称
class MyGetSelfInfo( ListView):
	def get(self, request, *args, **kwargs):
		try:

			_session = request.GET.get('session',"")
			_dict = {
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )