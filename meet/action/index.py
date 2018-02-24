#coding:utf-8
from meet.meet_query.m_meet import *
class ActionCurrent():
	def __init__(self):
		self.query_meet = M_Meet()
	def GetIndex(self):
		return self.query_meet.GetCurrent()