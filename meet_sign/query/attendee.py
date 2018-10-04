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
			"logo":query_get.logo,
			"name":query_get.name,
			"nick_name":query_get.nick_name,
			"male": query_get.male,
			"phone":query_get.phone,
			"company":query_get.company,
			"taxpayer_number":query_get.taxpayer_number,
			"company_address":query_get.company_address,
			"bank_account":query_get.bank_account,
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