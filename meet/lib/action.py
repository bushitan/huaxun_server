#coding:utf-8
from meet.meet_query.m_meet import *
from meet.meet_query.m_agenda import *
from meet.meet_query.m_guest import *
from meet.meet_query.m_news import *
from meet.meet_query.m_spot import *
from meet.meet_query.m_article import *
from meet.meet_query.m_swiper import *
meet = M_Meet()
article = M_Article()
agenda = M_Agenda()
guest = M_Guest()
news = M_News()
spot = M_Spot()
swiper = M_Swiper()
class Action():
	def MeetGetCurrent(self):
		return meet.GetCurrent()
	def MeetGetAgendaList(self,meet_id): #获取日程 - 会议
		return  meet.GetAgendaList(meet_id)
	def MeetGetSpotList(self,meet_id): #获取分会场 - 会议
		return  meet.GetSpotList(meet_id)
	def SiwperGetListByStyle(self,meet_id,style):
		return swiper.GetListByStyle(meet_id,style)
	def ArticleGetByArticleID(self,article_id):
		return article.GetArticleByArticleID(article_id)
	def AgendaGetListByMeetID(self,agenda_meet_list): #根据日程，获取列表
		agenda_list = []
		for m in agenda_meet_list:
			day = agenda.GetListByMeetId( m["meet_id"])
			agenda_list.append(day)
		return agenda_list
	def GuestGetListByMeetID(self,meet_id):
		return guest.GetListByMeetId(meet_id)
	def NewsGetListByMeetID(self,meet_id):
		return news.GetListByMeetId(meet_id)
	def SpotGetListByMeetID(self,spot_meet_list):
		_list = []
		for m in spot_meet_list:
			day = spot.GetListByMeetId( m["meet_id"])
			_list.append(day)
		return _list
		# return spot.GetListByMeetId(meet_id)