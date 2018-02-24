#coding:utf-8
class QueryBase(object):
	def __init__(self,model = None):
		self.model = model
		# print self.model
	def _PackList(self,_pack_fun,query_filter):
		_list = []
		for q in query_filter:
			_list.append( _pack_fun(q) )
		return _list

	def _PackDict(self,*args, **kwargs):
		pass

	def IsExists(self, *args, **kwargs):
		return self.model.objects.filter(*args, **kwargs).exists()

	def Add(self,*args,**kwargs):
		_m = self.model(*args,**kwargs)
		_m.save()
		return self._PackDict(_m)

	def Get(self,*args,**kwargs):
		if self.IsExists( *args, **kwargs) is False:
			return ""
		else:
			_m = self.model.objects.get(*args,**kwargs)
			return self._PackDict(_m)

	def GetQuery(self,*args,**kwargs):
		if self.IsExists( *args, **kwargs) is False:
			return ""
		else:
			_m = self.model.objects.get(*args,**kwargs)
			return _m

	def Filter(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		return self._PackList( self._PackDict,_m)

	def FilterQuery(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		return _m

	def Update(self,query_set,*args,**kwargs):
		query_set.update(*args,**kwargs)
		return self._PackList( self._PackDict,query_set)

	def Delete(self,*args,**kwargs):
		_m = self.model.delete(*args,**kwargs)
		_m.save()
		return True