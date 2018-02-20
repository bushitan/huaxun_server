#coding:utf-8

from api.models.article import *
from api.lib.util import *
from api.hx.hx_base import *

class HX_Tag(HX_Base):
	def __init__(self):
		pass
	def _PackDict(self,query_get):
		_dict = {
			'tag_id':query_get.id,
			'tag_name':query_get.name,
			'father_id' : query_get.father_id if query_get.father is not None else "" ,
			'father_name' : query_get.father.name if query_get.father is not None else "" ,
			"is_main":query_get.is_main,
			"is_index":query_get.is_index,
			"is_match":query_get.is_match,
		}
		return _dict
	# 1 获取所有father
	def GetFatherList(self):
		_tag_query = Tag.objects.filter(father_id = None,is_main = YES)
		return self._PackList(self._PackDict,_tag_query)
	# 2 根据father_id 获取 son列表
	def GetSonListByFather(self,father_id):
		_tag_query = Tag.objects.filter(father_id = father_id)
		return self._PackList(self._PackDict,_tag_query)

	# 3 将所有要显示的father ，son（快讯显示子栏目） ，match（供求显示子栏目）
	def GetMatrix(self):
		_tag_father = self._PackList(self._PackDict , Tag.objects.filter(is_main = YES))
		_tag_tree = []
		for f in _tag_father:
			f["son_list"] = []
			f["match_list"] = []
			_tag_tree.append(f)

		_tag_index = self._PackList(self._PackDict , Tag.objects.filter(is_index = YES))
		for s in _tag_index:
			if s['father_id'] != "": #
				for f in _tag_tree: #遍历father
					if s['father_id'] == f['tag_id']: #子类father_id 与 父类 tag_id 一致
						f["son_list"].append(s)

		_tag_match = self._PackList(self._PackDict , Tag.objects.filter(is_match = YES))
		for s in _tag_match:
			if s['father_id'] != "": #
				for f in _tag_tree: #遍历father
					if s['father_id'] == f['tag_id']: #子类father_id 与 父类 tag_id 一致
						f["match_list"].append(s)
		return _tag_tree

