#coding:utf-8
from meet_sign.query.cost import *
import json
import urllib2
class ActionCost():
	def __init__(self):
		self.query_cost = QueryCost()
	def GetListByCurrentMeet(self,meet_id):
		return self.query_cost.Filter(meet__id = meet_id)



if __name__ == "__main__":
	import os,django
	django.setup()
	b = ActionCost()
	print b.GetListByCurrentMeet('1')
	# b.SetInfo('112')