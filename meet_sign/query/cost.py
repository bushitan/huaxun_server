#coding:utf-8
from meet_sign.query.base import *
from meet_sign.models import *
class QueryAttendee(Base):
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
	def Set(self,*args,**kwargs):
		_dict = Attendee(*args,**kwargs)
		_dict.save()
		return self._PackDict(_dict)
	def GetDict(self, *args, **kwargs):
			_query = Attendee.objects.get(*args,**kwargs)
			return self._PackDict(_query)
	def IsExists(self, *args, **kwargs):
		return Attendee.objects.filter(*args, **kwargs).exists()