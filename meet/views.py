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
from meet.action.cover import *
from meet.action.a_meet import *

class Index( ListView):
	pass

#1 用户登录，本次会议的地图、封面、赞助商
# 用户是否已报名，
class Login( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_login = ActionLogin()
		super(Login,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_s_js_code = request.GET.get('js_code',"")
			_s_session = request.GET.get('meet_session',"")
			# _union_id = request.GET.get('union_id',"")
			_dict = {
                'dict_user':self.action_login.CheckSession(_s_js_code ,_s_session),
				'dict_current_meet':self.action_meet.GetCurrent()
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 获取日程列表
class MeetIndex( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_cover = ActionCover()
		super(MeetIndex,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_current_meet = self.action_meet.GetCurrent()
			if _current_meet == "":
				_dict = {'current_meet':"",}
			else:
				_dict = {
					'current_meet':_current_meet,
					'agenda_swiper_list': self.action_cover.GetSwiperAgenda( _current_meet['meet_id']),
					'news_swiper_list': self.action_cover.GetSwiperNews( _current_meet['meet_id']),
				}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#3 获取文章
class ArticleGetByArticleID( ListView):
	def __init__(self):
		self.action_cover = ActionCover()
		super(ArticleGetByArticleID,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_article_id = request.GET.get('article_id',"")
			_dict = {
				'article_dict':self.action_cover.GetArticleContent(_article_id)
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#4 获取日程列表
class AgendaGetListByMeetID( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_cover = ActionCover()
		super(AgendaGetListByMeetID,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_meet_id = request.GET.get('meet_id',"")
			_agenda_meet_list = self.action_meet.GetAgendaMeet(_meet_id)
			_agenda_matrix = self.action_cover.GetAgenda(_agenda_meet_list)
			_dict = {
				"tag_list":_agenda_meet_list,
                'cover_matrix':_agenda_matrix
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#5 获取嘉宾列表
class GuestGetListByMeetID( ListView):
	def __init__(self):
		self.action_cover = ActionCover()
		super(GuestGetListByMeetID,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                'article_list':self.action_cover.GetGuest(_meet_id)
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#6 获取新闻列表
class NewsGetListByMeetID( ListView):
	def __init__(self):
		self.action_cover = ActionCover()
		super(NewsGetListByMeetID,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_meet_id = request.GET.get('meet_id',"")
			_dict = {
                'article_list':self.action_cover.GetNews(_meet_id)
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#7 景点列表
class SpotGetListByMeetID( ListView):
	def __init__(self):
		self.action_meet = ActionMeet()
		self.action_cover = ActionCover()
		super(SpotGetListByMeetID,self).__init__()
	def get(self, request, *args, **kwargs):
		try:
			_meet_id = request.GET.get('meet_id',"")
			_tag_list = self.action_meet.GeSpotMeet(_meet_id)
			_cover_matrix = self.action_cover.GetSpot(_tag_list)
			_dict = {
				"tag_list":_tag_list,
                'cover_matrix':_cover_matrix
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
















