#coding:utf-8

from django.views.generic import ListView


from api.lib.message import *
from api.models.user import *
from api.hx.hx_article import *
from api.hx.hx_tag import *
from api.hx.hx_role import *

#1 进入快讯，初始化
class ArticleIndex( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_hx_article = HX_Article()
			_article_list = _hx_article.GetArticleByTag(_tag_id,_start_index,_end_index)
			_swiper_list = _hx_article.GetSwiper()
			_banner_list = _hx_article.GetBanner(_tag_id)
			_hx_tag = HX_Tag()
			_tag_list = _hx_tag.GetMatrix()

			_dict = {
				"article_list":_article_list,
				"swiper_list":_swiper_list,
				"banner_list":_banner_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#2 点击标签，获取文章
class ArticleGetListByTag( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_tag_id = request.GET.get('tag_id',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_hx_article = HX_Article()
			_article_list = _hx_article.GetArticleByTag(_tag_id,_start_index,_end_index)
			_dict = {
				'article_list':_article_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#3 点击文章,
#  无权限，跳转缴费
#  有权限，预览
class ArticleGetById( ListView):
	def get(self, request, *args, **kwargs):
		try:
			# _session = request.GET.get('session',"")
			# _user = User.objects.get( session =  request.GET.get('session',""))
			_article_id = request.GET.get('article_id',"")

			# _hx_role = HX_Role()
			# if _hx_role.CompareRole(_user.id,_article_id) is False:
			# 	_dict = {
			# 		"check_status":False,
			# 	}
			# else:
			_hx_article = HX_Article()
			_article_list = _hx_article.GetArticleByID(_article_id)

			_dict = {
				# "role_check":True,
				# "session":_session,
				# "check_status": True,
				"article_dict":_article_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#4 搜索文章
# arg:start_time ,end_time ,tag_id ,title ,start_index ,end_index

class ArticleGetListBySearch( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_tag_id = request.GET.get('tag_id',"")
			_keyword_title = request.GET.get('keyword_title',"")
			_start_time = request.GET.get('start_time',"")
			_end_time = request.GET.get('end_time',"")
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_hx_article = HX_Article()
			_article_list = _hx_article.GetSearch(_keyword_title,_start_index,_end_index,_start_time ,_end_time)

			_dict = {
				"check_status": True,
				"article_list":_article_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


#5 获取会议列表
class ArticleGetListByMeet( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_start_index = request.GET.get('start_index',"")
			_end_index = request.GET.get('end_index',"")
			_hx_article = HX_Article()
			_article_list = _hx_article.GetMeet(_start_index,_end_index)
			_dict = {
				'article_list':_article_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#5 检测文章是否已经点播
class ArticleCheckBySingle( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_user = User.objects.get( session =  request.GET.get('session',""))
			_article_id = request.GET.get('article_id',"")
			_role = HX_Role()
			if _role.CheckSinglePermissionByUser(_user.id,_article_id):
				_dict = {"is_single":True}
			else:
				_dict = {"is_single":False}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
