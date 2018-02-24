#coding:utf-8
from meet_sign.query.attendee import *
import json
import urllib2
class ActionAttendee():
	def __init__(self):
		self.query_attendee = QueryAttendee()
	def GetInfo(self,s_session):
		return self.query_attendee.Get(session = s_session)
	def SetInfo(self,s_session,**kwargs):
		_get = self.query_attendee.FilterQuery(session = s_session)
		return self.query_attendee.Update(_get,**kwargs)


if __name__ == "__main__":
	import os,django
	django.setup()
	b = ActionAttendee()
	print b.GetInfo('112')
	# b.SetInfo('112')