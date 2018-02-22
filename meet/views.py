#coding:utf-8

from django.views.generic import ListView


from api.lib.message import *
from api.models.user import *
from api.hx.hx_user import *

from meet.lib.action import *
action = Action()
# from meet.meet_query.m_meet import *
# from meet.meet_query.m_agenda import *
# from meet.meet_query.m_guest import *
# from meet.meet_query.m_news import *
# from meet.meet_query.m_spot import *
# from meet.meet_query.m_article import *
# from api.hx.hx_tag import *
# from api.hx.hx_role import *
from meet.action.login import *
from meet.action.index import *

class Index( ListView):
	pass

#1 用户登录，本次会议的地图、封面、赞助商
# 用户是否已报名，
class Login( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_s_js_code = request.GET.get('js_code',"")
			_s_session = request.GET.get('session',"")
			# _union_id = request.GET.get('union_id',"")

			# _hx_user = HX_User()
			# _user = _hx_user.UserLogin(_js_code ,_session)

			_m = MeetLogin()
			_index = MeetIndex()
			print _index
			_dict = {
                'dict_user':_m.CheckSession(_s_js_code ,_s_session),
				'dict_current_meet':_index.GetIndex()
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 获取日程列表
class MeetIndex( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_current_meet = action.MeetGetCurrent()
			if _current_meet == "":
				_dict = {'current_meet':"",}
			else:
				_agenda_swiper_list = action.SiwperGetListByStyle( _current_meet['meet_id'],MEET_SWIPER_AGENDA)
				_news_swiper_list = action.SiwperGetListByStyle(_current_meet['meet_id'],MEET_SWIPER_NEWS)
				_dict = {
					'current_meet':_current_meet,
					'agenda_swiper_list': _agenda_swiper_list,
					'news_swiper_list': _news_swiper_list,
				}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#3 获取文章
class ArticleGetByArticleID( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_article_id = request.GET.get('article_id',"")
			_article_dict = action.ArticleGetByArticleID(_article_id)
			_dict = {
				'article_dict':_article_dict
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#4 获取日程列表
class AgendaGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_meet_id = request.GET.get('meet_id',"")
			_agenda_meet_list = action.MeetGetAgendaList(_meet_id)
			_agenda_matrix = action.AgendaGetListByMeetID(_agenda_meet_list)
			_dict = {
				"tag_list":_agenda_meet_list,
                'cover_matrix':_agenda_matrix
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#5 获取嘉宾列表
class GuestGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_meet_id = request.GET.get('meet_id',"")
			_cover_list = action.GuestGetListByMeetID(_meet_id)
			_dict = {
                'article_list':_cover_list
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#6 获取新闻列表
class NewsGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_meet_id = request.GET.get('meet_id',"")
			_cover_list = action.NewsGetListByMeetID(_meet_id)
			_dict = {
                'article_list':_cover_list
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#7 景点列表
class SpotGetListByMeetID( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_meet_id = request.GET.get('meet_id',"")
			_tag_list = action.MeetGetSpotList(_meet_id)
			_cover_matrix = action.SpotGetListByMeetID(_tag_list)
			_dict = {
				"tag_list":_tag_list,
                'cover_matrix':_cover_matrix
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )






			# _user = User.objects.get( session =  request.GET.get('session',""))
			# _meet_id = request.GET.get('meet_id',"")

















