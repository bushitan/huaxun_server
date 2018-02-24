#coding:utf-8
from meet.query.agenda import *
from meet.query.guest import *
from meet.query.q_meet import *
from meet.query.news import *
from meet.query.spot import *
from meet.query.swiper import *
from meet.query.article_library import *
class ActionCover():
	def __init__(self):
		self.query_agenda = QueryAgenda()
		self.query_guest = QueryGuest()
		self.query_news = QueryNews()
		self.query_spot = QuerySpot()
		self.query_swiper = QuerySwiper()
		self.query_article = QueryArticleLibrary()

	def GetSwiperAgenda(self,meet_id):
		return self.query_swiper.Filter( meet_id = meet_id,style=MEET_SWIPER_AGENDA)
	def GetSwiperNews(self,meet_id):
		return self.query_swiper.Filter( meet_id =  meet_id ,style=MEET_SWIPER_NEWS)

	def GetAgenda(self,agenda_meet_list):
		agenda_list = []
		for m in agenda_meet_list:
			agenda_list.append(
				self.query_agenda.Filter( meet_id =  m["meet_id"])
			)
		return agenda_list

	def GetGuest(self,meet_id):
		return self.query_guest.Filter( meet_id =  meet_id)

	def GetNews(self,meet_id):
		return self.query_news.Filter( meet_id =  meet_id)

	def GetSpot(self,spot_meet_list):
		_list = []
		for m in spot_meet_list:
			day = self.query_spot.Filter( meet_id = m["meet_id"])
			_list.append(day)
		return _list

	def GetArticleContent(self,article_id):
		return self.query_article.Get(id = article_id)