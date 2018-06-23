# -*- coding: utf-8 -*-
import json,urllib2,urllib
import os,sys

appid = 'VxfXp4cu'
appsecret = 'dc5c7986daef50c1e02ab09b442ee34f'

class ActionAPI308():
	def _post(self,url,data):
		data_json = json.dumps(data)
		headerdata = {"Content-type": "application/json"}
		req = urllib2.Request( url, data_json ,headerdata)
		# print req
		res_data = urllib2.urlopen(req)
		# print res_data
		res = res_data.read()
		return res

	def _get(self,url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		_json =  json.loads(response.read())
		return  _json

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

	## 1. 获取API访问令牌
	def create(self):
		_url = "https://api.308308.com/auth/token?app_id=%s&app_secret=%s" %(appid,appsecret)
		_json = self._get(_url)
		print _json
		with open(self._token_file(),'w') as f:
			json.dump(_json,f)
		return  self._get_token()

	## 4 通过openid获取用户信息
	def user_get_info_by_openid(self,open_id):
		_url = "https://api.308308.com/cms/ca/get_info_by_openid?access_token=%s" %(self._get_token())
		_data = {
		  "open_id":open_id
		}
		return self._post(_url,_data)


	## 5 用户绑定
	def user_bind(self,open_id,account,password):
		_url = "https://api.308308.com/cms/ca/bind?access_token=%s" %(self._get_token())
		_data = {
			"openid": open_id,
			"account": account,
			"password": password
		}
		return self._post(_url,_data)

	## 6.用户注册
	def user_register(self,open_id,mobile,code,industry_id):
		_url = "https://api.308308.com/cms/ca/register?access_token=%s" %(self._get_token())
		_data = {
			"openid": open_id,
			"mobile": mobile,
			"code" : code,
			"industry_id":industry_id
		}
		return self._post(_url,_data)

	## 7.套餐购买
	def user_buy_package(self,uid,industry_id,member_type,validation_from,validation_to):
		_url = "https://api.308308.com/cms/ca/buy_package?access_token=%s" %(self._get_token())
		_data = {
			"uid": uid,
			"industry_id":industry_id,
			"member_type":member_type,
			"validation_from" : validation_from,
			"validation_to" : validation_to
		}
		return self._post(_url,_data)

	# 8 获取行业
	def cms_get_all_industry(self):
		# return u'111'
		_url = "https://api.308308.com/cms/articles/get_all_industry?access_token=%s" %(self._get_token())
		_json = self._get(_url)
		return _json

	# 9 获取行业下的目录
	def cms_get_categories_by_industry(self,industry_id):
		# return u'112'
		_url = "https://api.308308.com/cms/articles/get_categories_by_industry?access_token=%s" %(self._get_token())
		_data = {
		  "industry_id":industry_id
		}
		return self._post(_url,_data)

	# 10 获取指定行业对应栏目下的文章列表
	def cms_get_articles_by_category(self,
									 industry_id,category_id,
									 rows,page_no,
									 sort,order):
		_url = "https://api.308308.com/cms/articles/get_articles_by_category?access_token=%s" %(self._get_token())
		_data = {
			"industry_id": industry_id,
			"category_id": category_id,
			"rows": rows,
			"page_no":page_no,
			"sort": sort,
			"order": order
		}
		return self._post(_url,_data)

	# 11 获取指定的文章
	def cms_get_article (self,uid,article_id):
		_url = "https://api.308308.com/cms/articles/get_article?access_token=%s" %(self._get_token())
		_data = {
			  "uid" : uid,
			  "article_id": article_id
			}
		return self._post(_url,_data)


	############# 权限 #################
	## 12 判断有无权限
	def ca_has_privilege (self,uid,industry_id,bussiness_type,bussiness_id):
		_url = "https://api.308308.com/cms/ca/has_privilege?access_token=%s" %(self._get_token())
		_data ={
			"uid" : uid,
			"industry_id":industry_id,
			"bussiness_type": bussiness_type,
			"bussiness_id" : bussiness_id
		}
		return self._post(_url,_data)


	#########商圈###############

	## 13 获取行业子类标签列表
	def cms_get_product_type (self,industry_id):
		_url = "https://api.308308.com/cms/get_product_type?access_token=%s" %(self._get_token())
		_data = {
		   "industry_id":industry_id
		}
		return self._post(_url,_data)


	## 17. 获取商圈数据
	def roster_get_list (self,
						 industry_id,category_id,
						 rows,page_no,
						 sort,order,
						 company_name,contact_name,uid):

		_url = "https://api.308308.com/cms/mall/get_malls?access_token=%s" %(self._get_token())
		_data = {
			"industry_id": industry_id,
			"rows": rows,
			"page_no":page_no,
			"sort": sort,
			"order": order,
			"company_name": company_name,
			"contact_name": contact_name,
			"uid":uid
		}
		_data = {
		  "sort": "",
		  "order": "",
		  "rows": "10",
		  "page_no": "1",
		  "industry_id": "1",
		  "company_name": "广西华思特国际贸易有限公司",
		  "contact_name": "张三",
			"uid": "1232"
		}
		print _url
		print _data
		return self._post(_url,_data)



if __name__ == "__main__":
	a = ActionAPI308()
	# print a.create()
	# print a.user_get_info_by_openid( "oNUgxv608YVIclrLMz_0egqocXcI")
	# print a.user_bind( "oNUgxv608YVIclrLMz_0egqocXcI","zhangsan","12345678")
	# print a.user_register( "oNUgxv608YVIclrLMz_0egqocXcI","13800000000","1234",1)
	print a.user_buy_package( "10092",1,1,"2018-05-23 12:09:12","2019-05-23 12:09:12")
	# print a.cms_get_all_industry()
	# print a.cms_get_categories_by_industry(2)
	# print a.cms_get_articles_by_category(1,3,20,1,"release_date","desc" )
	# print a.cms_get_article(10921,220634)
	# print a.ca_has_privilege(10921,1,"BUSSINESS_TYPE_ARTICLE",123)
	# print a.cms_get_product_type(1)
	# print a.roster_get_list(1,3,20,1,"release_date","desc" ,u'广西华思',u"张三",1232)
	# print a.cms_get_categories_by_industry()
	# pass
	# print WxHttp('')




	# u'access_token': u'48c59e94647edf87ce507acdadde737e', u'expire_in': 7200, u'refresh_token': u'e9311efe13ea5f5fb437709f0de62087