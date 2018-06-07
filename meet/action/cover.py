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


	def GetMap(self):
		# 26.5589000000,106.7039300000
		return {
			# "latitude": 23.1066805,
			# "longitude": 113.3245904,
			"latitude": 26.5589000000,
			"longitude": 106.7039300000,
        	"phoneNumber":"0851-86878888",
        	"name":"贵阳林城万宜酒店",
        	"address":"贵阳市南明区遵义路326号(临近火车站)",
		}
		# return self.query_spot.Filter( )[0]

	def GetSpot(self,spot_meet_list):
		_list = []
		for m in spot_meet_list:
			day = self.query_spot.Filter( meet_id = m["meet_id"])
			_list.append(day)
		return _list

	def GetArticleContent(self,article_id):
		return self.query_article.Get(id = article_id)