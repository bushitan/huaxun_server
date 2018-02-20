# -*- coding: utf-8 -*-
from api.models.user import *
from api.hx.hx_base import *
import huaxun_server.settings as SETTINGS
app_id = SETTINGS.APP_ID
app_secret = SETTINGS.APP_SECRET

import json,urllib2

def WxHttp(js_code):
	_js_code = js_code
	_wx_url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code "  %(app_id,app_secret,_js_code )
	req = urllib2.Request(_wx_url)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	response = opener.open(req)
	_json =  json.loads(response.read())
	return  _json

class HX_User(HX_Base):
	def __init__(self):
		pass

	def _PackDict(self,query_get):
		_dict = {
			'user_id':query_get.id,
			'logo':query_get.logo,
			'nick_name' : query_get.nick_name,
		}
		return _dict

	def UserLogin(self,js_code, session):
		if User.objects.filter( session = session ).exists() is True:  #session存在，返回用户
			_user = User.objects.get( session = session)
		else:#session不存在，获取open_id判断
			_json = WxHttp(js_code)
			_open_id = _json["openid"]
			if User.objects.filter( wx_open_id = _open_id ).exists() is True: #open_id 存在，
				_user = User.objects.get( wx_open_id = _open_id)
			else: #open_id 不存在，增加用户
				_user = User(
					wx_open_id = _json["openid"],
					session =  _json["session_key"],
				)
				_user.save()
		return _user

	#用户上传微信信息
	def UserSetWxInfo(self, session ,logo_url ,nick_name):
		_user = User.objects.get( session = session)
		_user.logo = logo_url
		_user.nick_name = nick_name
		_user.save()
		return True

	# 用户填写花名册信息
	def UserSetRosterInfo(self,session):
		_user = User.objects.get( session = session)
		return True


	# 用户登录后获取头像等内容
	def UserGetSelfInfo(self,session):
		_query = User.objects.get( session = session)
		return self._PackDict(_query)












