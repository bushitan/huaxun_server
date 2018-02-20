# #coding:utf-8
#
# from django.views.generic import ListView
#
# from match.models import *
# from api.models.user import *
# from api.lib.message import *
# from api.hx.hx_match import HX_Match
# #1 首页文章初始化
# class MatchIndex( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_session = request.GET.get('session',"")
# 			_user = User.objects.get( session = _session)
#
# 			# 先查询前20条
# 			_start_index = 0
# 			_range = 50
# 			_match = HX_Match()
# 			_index_list = _match.GetListByRange(_start_index,_start_index + _range)
# 			_dict = {
# 				"user_id":_user.id,
# 				"article_list":_index_list
# 			}
# 			print _dict
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#
# # 获取供求信息详情
# class MatchGetDetailById( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_match_id = 1
# 			_match = HX_Match()
# 			_match_dict = _match.GetDictById(_match_id)
#
# 			_dict = {
# 				"match_dict":_match_dict,
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#
#
# #1 首页文章初始化
# class MatchSetDetailByUser( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_session = request.GET.get('session',"")
# 			_is_buy = request.GET.get('is_buy',"")
# 			_title = request.GET.get('title',"")
# 			_content = request.GET.get('content',"")
# 			_phone = request.GET.get('phone',"")
#
# 			_user = User.objects.get( session = _session)
# 			_news = Match(
# 				user_id = _user.id,
# 				is_buy = _is_buy,
# 				title = _title,
# 				content = _content,
# 				phone = _phone,
# 			)
# 			_news.save()
# 			_dict = {
# 				"msg":u"添加简讯成功"
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#
#
#
#
# #1 首页文章初始化
# class MatchGetListByUser( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_session = request.GET.get('session',"")
# 			_user = User.objects.get( session = _session)
# 			_match = HX_MatchPro()
# 			_match_list = _match.GetListByUser(_user.id)
# 			_dict = {
# 				"match_list":_match_list
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#
#
# #1 首页文章初始化
# class MatchDeleteByIdUser( ListView):
# 	def get(self, request, *args, **kwargs):
# 		try:
# 			_session = request.GET.get('session',"")
# 			_match_id = request.GET.get('match_id',"")
# 			_user = User.objects.get( session = _session)
# 			_match = HX_MatchPro()
# 			_match.DeleteDictByUser(_match_id,_user.id)
# 			_dict = {
# 				"msg":u"删除成功"
# 			}
# 			return MESSAGE_RESPONSE_SUCCESS(_dict)
# 		except Exception,e :
# 			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
