# -*- coding: utf-8 -*-

from roster.models import *
from api.hx.hx_base import *
from django.db import transaction #事务
from django.db.models import Q
class HX_Roster(HX_Base):
	def __init__(self):
		pass

	def _PackDict(self,query_get):
		_dict = {
			'roster_id' : query_get.id,
			'user_logo' : query_get.user.logo if query_get.user.roster_image is None else  query_get.user.roster_image.url,
			'user_name' : query_get.user.name,
			'company_name': query_get.user.company.name if query_get.user.company is not None else '' ,
			'introduction': query_get.user.introduction ,
			'phone': query_get.user.phone ,
			'address': query_get.user.address ,
			'latitude': query_get.user.latitude ,
			'longitude': query_get.user.longitude ,
			'buy': u"、".join([p.name for p in query_get.buy.all()]) ,
			'sell': u"、".join([p.name for p in query_get.sell.all()]) ,
			'area':  query_get.area.name if query_get.area is not None else '' ,
		}
		return _dict
        def _PackAreaDict(self,query_get):
                _dict = {
                        'area_id':query_get.id,
                        'area_name':query_get.name,
                }
                return _dict

        
	# 1 未搜索下拉滚动——查询花名册
	# 要把所有的人严格排序
	def GetListByTagRange(self,tag_id,start_index,end_index):
		_query = Roster.objects.filter(tag_id = tag_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)

	# 2 点击头像——根据ID获取详细内容
	def GetDictById(self,roster_id):
		_query = Roster.objects.get(id = roster_id)
		return self._PackDict(_query)

	# 3 点击搜索、下拉滚动——根据公司名字搜索
	def SearchByCompany(self,key_word,start_index,end_index,tag_id):
		print  111
		_query = Roster.objects.filter( Q(user__company__name__contains= key_word)| Q(user__name__contains = key_word) ,tag_id=tag_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)



	# 3 按求购的标签查询花名册
	def SearchByBuy(self,tag_id,start_index,end_index):
		_query = Roster.objects.filter(buy__id= tag_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)

	# 3 按求购的标签查询花名册
	def SearchBySell(self,tag_id,start_index,end_index):
		_query = Roster.objects.filter(sell__id= tag_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)


	# 4 按区域的标签查询花名册
	def SearchByArea(self,area_id,tag_id,start_index,end_index):
		_query = Roster.objects.filter(area_id=area_id,tag_id= tag_id)[start_index:end_index]
		return self._PackList(self._PackDict,_query)


	# 5 获取所有区域
	def GetAreaList(self):
		_query = Area.objects.all()
		return self._PackList(self._PackAreaDict,_query)



	# 4 “我”中进入“我的名片”
	def GetDictByUser(self,user_id):
		if  Roster.objects.filter(user_id = user_id).exists() is False:
			_roster = Roster(user_id = user_id)
			_roster.save()
		else:
			_roster = Roster.objects.get(user_id = user_id)
		return self._PackDict(_roster)

	# 5 “我的名片”，用户点击“保存”——上传我的信息
	def SetByUser(self,session,name,introduction,phone,address ,latitude ,longitude):
		with transaction.atomic():
			_user = User.objects.get( session =  session)
			# _roster =  Roster.objects.get(user_id = _user.id)
			_user.name = name
			_user.introduction = introduction
			_user.phone = phone
			_user.address = address
			_user.latitude = latitude
			_user.longitude = longitude
			_user.save()
			# _roster.save()
			return True


	# def GetListByTag
	# def SetDictByUser(self,user_id):
	# 	pass
		# return True
	# 根据id 获取内容
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
	# 	_query.delete()
	# 	_query.save()
		# return self._pack_list(_query)

