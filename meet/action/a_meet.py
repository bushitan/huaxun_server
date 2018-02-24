#coding:utf-8
from meet.query.agenda import *
from meet.query.guest import *
from meet.query.q_meet import *
from meet.query.news import *
from meet.query.spot import *
from meet.query.swiper import *
class ActionMeet():
	def __init__(self):
		self.query_meet = QueryMeet()
	def GetCurrent(self):
		return self.query_meet.Get(status = MEET_START)
	def GetAgendaMeet(self,meet_id):
		return self.query_meet.Filter(father_id = meet_id,style = MEET_AGENDA)
	def GeSpotMeet(self,meet_id):
		return self.query_meet.Filter(father_id = meet_id,style = MEET_SPOT)




		# return self.query_agenda.Filter(*args,**kwargs)