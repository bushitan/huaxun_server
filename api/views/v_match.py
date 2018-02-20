#coding:utf-8

from django.views.generic import ListView

from api.lib.message import *
from api.hx.hx_match import *

#1 首页文章初始化
class MatchGetListByTag( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_action = request.GET.get('action',"")
			_hx_match = HX_Match()
			print _action
			if _action == "":
				_match_list = _hx_match.GetByTag(_tag_id ,_start_index ,_end_index)
			elif _action == str(SELF): #查询自己的
				_user = User.objects.get( session = request.GET.get('session',""))
				_match_list = _hx_match.GetByTagSelf(_tag_id ,_start_index ,_end_index,_user.id)
			else:
				_match_list = _hx_match.GetByTagCheckBuy(_tag_id ,_start_index ,_end_index,_action)
			_dict = {
				"article_list":_match_list
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 发布供求信息
class MatchSetIssue( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_tag_id = request.GET.get('tag_id',"")
			_is_buy = request.GET.get('is_buy',"")
			_title = request.GET.get('title',"")
			_content = request.GET.get('content',"")
			_phone = request.GET.get('phone',"")
			_user = User.objects.get( session = request.GET.get('session',""))

			_hx_match = HX_Match()
			_hx_match.SetIssue(
				_user.id,
				_tag_id,
				_is_buy,
				_title,
				_content,
				_phone
			)
			_dict = {
				"msg":u"添加简讯成功"
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#3 删除供求信息
#arg：match_id ，user_id
class MatchDeleteBySelf( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session = request.GET.get('session',""))
			_match_id = request.GET.get('match_id',"")

			_hx_match = HX_Match()
			_hx_match.DeleteByID(_match_id,_user.id)
			_dict = {
				"msg":u"删除简讯成功"
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#4 查询自己的发布的供求信息你
#arg：match_id ，user_id
class MatchGetListBySelf( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session = request.GET.get('session',""))
			_dict = {}
			# _hx_match = HX_Match()
			# _match_list = _hx_match.GetListBySelf(_user.id)
			# _dict = {
			# 	"article_list":_match_list
			# }
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )