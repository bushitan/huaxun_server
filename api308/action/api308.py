# -*- coding: utf-8 -*-
import json,urllib2,urllib
import os,sys

appid = 'VxfXp4cu'
appsecret = 'dc5c7986daef50c1e02ab09b442ee34f'
class ActionAPI308():
	def _post(self,url,data):
		# req = urllib2.Request(url)
		# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		# response = opener.open(req)
		# _json =  json.loads(response.read())
		# return  _json
# post请求
# import urllib
# import urllib2
#
		data_json = json.dumps(data)
		# test_data_urlencode = urllib.urlencode(data)
		headerdata = {"Content-type": "application/json"}
		req = urllib2.Request( url, data_json ,headerdata)
		# print req
		res_data = urllib2.urlopen(req)
		print res_data
		res = res_data.read()
		print res
		return res
# print res

	def _get(self,url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		_json =  json.loads(response.read())
		return  _json


		# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		# response = opener.open(req)
		# _json =  json.loads(response.read())

	def _token_file(self):
		ABSPATH=os.path.abspath(sys.argv[0])
		ABSPATH=os.path.dirname(ABSPATH)
		ABSPATH=os.path.dirname(ABSPATH)
		token_file = os.path.dirname(ABSPATH) + '\\'  + "api_308_token.txt"
		return token_file

	#获取本地token
	def _get_token(self):
		with open(self._token_file(),'r') as f:
			load_dict = json.load(f)
		access_token = load_dict["data"]["access_token"]
		return access_token

	#创建token
	def create(self):
		_url = "https://api.308308.com/auth/token?app_id=%s&app_secret=%s" %(appid,appsecret)
		_json = self._post(_url)
		print _json
		with open(self._token_file(),'w') as f:
			json.dump(_json,f)
		return  self._get_token()

	# 刷新token
	def refresh_token(self):
		_url = "https://api.308308.com/auth/refresh_token?token=%s" %(self._get_token())
		_json = self._post(_url)
		print _json
		return

	# 校验token
	def check_token(self):
		_url = "https://api.308308.com/auth/check_token?token=%s" %(self._get_token())
		_json = self._post(_url)
		print _json
		return


	def _json_check(self):
		return


	# 获取行业
	def cms_get_all_industry(self):
		# return u'111'

		_url = "https://api.308308.com/cms/articles/get_all_industry?access_token=%s" %(self._get_token())
		_json = self._get(_url)
		print _json
		return _json

	# 获取行业下的目录
	def cms_get_categories_by_industry(self):
		# return u'112'
		_url = "https://api.308308.com/cms/articles/get_categories_by_industry?access_token=%s" %(self._get_token())
		_data = {
		  "industry_id":"1"
		}
		return self._post(_url,_data)

	# 获取目录下的封面列表
	def cms_get_articles_by_category(self):
		return u'112'
		_url = "https://api.308308.com/cms/articles/get_articles_by_category?access_token=%s" %(self._get_token())
		return self._get(_url)

	# 获取文章
	def cms_get_article (self):
		return u'112'
		_url = "https://api.308308.com/cms/articles/get_article?access_token=%s" %(self._get_token())
		return self._get(_url)


	############# 权限 #################
	def ca_has_privilege (self):
		return u'112'
		_url = "https://api.308308.com/cms/ca/has_privilege?access_token=%s" %(self._get_token())
		return self._get(_url)


	#########商圈###############

	# 获取行业子类标签列表
	def cms_get_product_type (self):
		return u'112'
		_url = "https://api.308308.com/cms/get_product_type?access_token=%s" %(self._get_token())
		return self._get(_url)

	#获取商圈数据
	def roster_get_list (self):
		return u'112'
		_url = "https://api.308308.com/cms/mall/get_malls?access_token=%s" %(self._get_token())
		return self._get(_url)



if __name__ == "__main__":
	a = ActionAPI308()
	# print a.create()
	# print a.cms_get_all_industry()
	print a.cms_get_categories_by_industry()
	pass
	# print WxHttp('')




	# u'access_token': u'48c59e94647edf87ce507acdadde737e', u'expire_in': 7200, u'refresh_token': u'e9311efe13ea5f5fb437709f0de62087