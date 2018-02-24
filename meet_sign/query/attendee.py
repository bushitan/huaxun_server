#coding:utf-8

from meet.lib.query_base import *
from meet_sign.models import *
class QueryAttendee(QueryBase):
	def __init__(self):
		super(QueryAttendee,self).__init__(Attendee)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
			"session":query_get.session,
			"uuid":query_get.uuid,
			"name":query_get.name,
			"male": query_get.male,
			"company":query_get.company,
			"phone":query_get.phone,
			"position":query_get.position,
			"remark":query_get.remark,
		}

if __name__ == "__main__":
	import os,django
	django.setup()
	a = QueryAttendee()
	# Attendee.objects.update()
	alist = a.FilterQuery(session='112')
	# print alist[0]
	print a.Update(alist,uuid="433")