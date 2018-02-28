#coding:utf-8
from meet_sign.query.attendee import *
from meet.lib.util import *
import json
import urllib2
app_id = MEET_APP_ID
app_secret = MEET_APP_SECRET
class ActionLogin():
	def __init__(self):
		self.query_attendee = QueryAttendee()
	def CheckSession(self,s_js_code, s_session):
		if self.query_attendee.IsExists(session = s_session) is True:  #session存在，返回用户
			_d_attendee = self.query_attendee.Get(session = s_session)
		else:#session不存在，获取open_id判断
			# _json = WxHttp(_js_code)
			_json = self._GetOpenID(s_js_code)
			_open_id = _json["openid"]
			if self.query_attendee.IsExists( wx_open_id = _open_id ) is True: #open_id 存在，
				_d_attendee = self.query_attendee.Get( wx_open_id = _open_id)
			else: #open_id 不存在，增加用户
				_d_attendee = self.query_attendee.Add(
					wx_open_id = _json["openid"],
					session =  _json["session_key"],
				)
		return _d_attendee
	def _GetOpenID(self,js_code):
		_js_code = js_code
		_wx_url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code "  %(app_id,app_secret,_js_code )
		req = urllib2.Request(_wx_url)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(req)
		_json =  json.loads(response.read())
		return  _json