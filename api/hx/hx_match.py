# -*- coding: utf-8 -*-
from match.models import *
from api.hx.hx_base import *
class HX_Match(HX_Base):
	def __init__(self):
		pass

	def _PackDict(self,query_get):
		_dict = {
			'match_id':query_get.id,
			'user_id':query_get.user_id,
			'is_buy' : query_get.is_buy,
			'title' : query_get.title,
			'content': query_get.content,
			'phone' : query_get.phone,
			'issue_time':query_get.issue_time.strftime("%Y.%m.%d %H:%M:%S"),
		}
		return _dict

	# 1 点击标签 —— 获取供求
	def GetByTag(self,tag_id,start_index,end_index):
		_query = Match.objects.filter(tag_id=tag_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)

	# 2 选择 “供” 或 “求” —— 筛选信息
	def GetByTagCheckBuy(self,tag_id,start_index,end_index,action):
		print action
		_query = Match.objects.filter(tag_id=tag_id,is_buy = action)[start_index:end_index]
		return self._PackList(self._PackDict,_query)

	# 3 选择 "我“ 获取用户自己的数据
	def GetByTagSelf(self,tag_id,start_index,end_index,user_id):
		_query = Match.objects.filter(tag_id=tag_id,user_id=user_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)

	# 4 用户发布供求
	def SetIssue(self,_user_id,tag_id,_is_buy,_title,_content,_phone):
		_match = Match(
			user_id = _user_id,
			tag_id = tag_id,
			is_buy = _is_buy,
			title = _title,
			content = _content,
			phone = _phone,
		)
		_match.save()
		return True

	# 5 用户删除自己的供求
	def DeleteByID(self,match_id,user_id):
		_query = Match.objects.get(user_id=user_id,id=match_id)
		_query.delete()








	# def _pack_list(self,query_filter):
	# 	_list = []
	# 	for q in query_filter:
	# 		_list.append( self._pack_dict(q) )
	# 	return _list
	#
	# def _pack_dict(self,query_get):
	# 	_dict = {
	# 		'match_id':query_get.id,
	# 		'user_id':query_get.user_id,
	# 		'is_buy' : query_get.is_buy,
	# 		'title' : query_get.title,
	# 		'content': query_get.content,
	# 		'phone' : query_get.phone,
	# 		'issue_time':query_get.issue_time.strftime("%Y.%m.%d %H:%M:%S"),
	# 	}
	# 	return _dict
	#
	# # 根据id 获取内容  TODO 不看了
	# def GetDictById(self,match_id):
	# 	_query = Match.objects.get(id=match_id)
	# 	return self._pack_dict(_query)
	#
	# # 根据start 和end  查询数组
	# def GetListByRange(self,start_index,start_end):
	# 	#
	# 	_query = Match.objects.all()[start_index:start_end]
	# 	return self._pack_list(_query)
	#
	# # 获取用户自己的数据
	# def GetListByUser(self,user_id):
	# 	_query = Match.objects.filter(user_id=user_id)
	# 	return self._pack_list(_query)
	#
	# # 删除信息
	# def DeleteDictByUser(self,match_id,user_id):
	# 	_query = Match.objects.get(user_id=user_id)
	# 	# _query.delete()
	#
	#
	# 	# _query.save()
	# 	# return self._pack_list(_query)

