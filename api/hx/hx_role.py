#coding:utf-8
import datetime
from order.models import *
from api.hx.hx_base import *
from api.models.user import *


## role 与order 很相近，用户的权限，都在order中
class HX_Role(HX_Base):
	def __init__(self):
		pass

	#  会员角色的详细信息
	def _PackRoleDict(self,query_get):
		_dict = {
			'role_id':query_get.id,
			"role_name":query_get.name,
			"role_value":query_get.value,
			"role_price":query_get.price,
			"image_url":query_get.image_url,
			# "start_time":query_get.start_time,
			# "start_time":query_get.start_time,
		}
		return _dict
	#  用户购买的会员列表
	def _PackOrderDict(self,query_get):
		_dict = {
			'order_id':query_get.id,
			'user_id':query_get.user_id,
			"role_id":query_get.role_id,
			"role_name":query_get.role.name,
			"role_value":query_get.role.value,
			"tag_id":query_get.tag_id,
			"father_tag_id":query_get.tag.father_id,
			"start_time":query_get.start_time.strftime("%Y.%m.%d"),
			"end_time":query_get.end_time.strftime("%Y.%m.%d"),
			"remain_time":( query_get.end_time - datetime.datetime.now() ).days,
			'tag_name':query_get.tag.name,
		}
		return _dict
	def CompareRole(self,user_id,article_id):
		pass

	# 1 获取系统定义的角色的价格
	def GetFeeByID(self,role_id):
		_role = Role.objects.get(role_id)
		return _role.price

	# 2 点击文章检测——用户是否已经点播
	def CheckSinglePermissionByUser(self,user_id,article_id):
		_now = datetime.datetime.now()
		return	Order.objects.filter(
			user_id = user_id,
			article_id= article_id,
			agreement_type = AGREEMENT_TYPE_SINGLE_TIME,
			is_payment = IS_PAYMENT_TRUE ,
			start_time__lt  = _now,
			end_time__gt = _now,
		).exists()

	# 3 获取用户的会员状态
	def GetMemberListByUser(self,user_id):
		_now = datetime.datetime.now()
		_order_query = Order.objects.filter(
			user_id = user_id,
			agreement_type = AGREEMENT_TYPE_MEMBER,
			is_payment = IS_PAYMENT_TRUE ,
			start_time__lt  = _now,
			end_time__gt = _now,
			is_alive = YES,
		)
		return  self._PackList(self._PackOrderDict,_order_query)

	# 4-1 支付页面，根据用户的角色等级，决定pack组件显示
	# 普通会员 显示 “资讯会员” 和 “短信会员”，
	# 短信会员 显示 “资讯会员”
	# 资讯会员不进入这个页面
	def GetPayRoleList(self,_top_role_value):
		_role_query = Role.objects.filter( value__gt = _top_role_value )    #获取value>1的
		return  self._PackList(self._PackRoleDict,_role_query)

	# 4-2 根据value查角色详情，做为列表传入前台
	def GetRoleByValue(self,value):
		_role_query = Role.objects.get( value = value )    #获取value>1的
		return  self._PackRoleDict(_role_query)

	# 4-3 判断用户在该tag下的最高角色
	def GetPreparePayByTag(self,user_id,tag_id):
		_now = datetime.datetime.now()
		_order_query = Order.objects.filter(
			user_id = user_id,
			tag_id = tag_id,
			agreement_type = AGREEMENT_TYPE_MEMBER,
			is_payment = IS_PAYMENT_TRUE ,
			start_time__lt  = _now,
			end_time__gt = _now,
			is_alive = YES,
		)
		_temp_value = ROLE_LEVEL_1
		# _name_list = []
		# _value_list = []
		for o in _order_query:
			if int(o.role.value) > int(_temp_value):
				_temp_value = o.role.value
		# if 	_temp_value == ROLE_LEVEL_2:
		# 	_name_list.append()
		return _temp_value
		# print _order_query






	# # 检测，当tag_id 一致
	# # 1 、当tag_id 一致 role条件满足  return True
	# # 2 、当tag_id 一致 role不满足 记录_value
	# # 3、 当tag_id 不一致   返回value
  	# def CheckMemberPermissionByUser(self,_user,_article):
	# 	_u_role_list = self.GetMemberListByUser(_user.id)
	# 	_dict ={ #初始化返回等级，用户为1级
	# 		"user_role_value": ROLE_LEVEL_1,
	# 		"article_role_value":_article["role_value"] ,
	# 	}
	# 	for u in _u_role_list :
	# 		#当用户的tag_id 与  文章的父类id一直
	# 		if u['tag_id'] == _article['father_tag_id']:
	# 			if  u["role_value"] >= _article["role_value"] : 	#比较 role的级别
	# 				return True
	# 			else:
	# 				_dict["user_role_value"] = u["role_value"] #用户
	# 	return _dict #用户没有购买过VIP或超级VIP
	#
	# # 检测结果
	# def CheckResponse(self,session,content):
	# 	if content.has_key('article_check'):
	#
	# 		_user = User.objects.get( session = session)
	# 		_article = content['article_dict']
	# 		if _article['role_value'] == ROLE_LEVEL_1: #普通权限 返回
	# 			return True
	# 		if self.CheckSinglePermissionByUser(_user.id,_article['article_id']) is True: #检测是否点播
	# 			return True  #已经点播
	# 		# return self.CheckMemberPermissionByUser(_user,_article)
	# 		_permission_dict =  self.CheckMemberPermissionByUser(_user,_article)
	# 		if _permission_dict is True:
	# 			return True # 有权限
	# 		else:
	# 			_permission_dict["article_id"] = _article["article_id"]
	# 			_permission_dict["father_tag_id"] = _article["father_tag_id"]
	# 			return MESSAGE_RESPONSE_FAIL(_permission_dict)
	#
	# 				# print 123,u['tag_id'],_article['father_tag_id']
	#
	#
	# 		# _article = content['article_dict']
	# 		# _article_role_id = _article.role_id
	# 		# _article_tag_id = _article.tagb_id
	#
	#
	# 	return True














