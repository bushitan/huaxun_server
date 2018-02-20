#coding:utf-8

from api.models.article import *
from api.models.trace import *
from api.lib.util import *
from api.hx.hx_base import *
from django.utils.timezone import now, timedelta

class HX_Article(HX_Base):
	def __init__(self):
		pass

	#用于封面展示的数据
	def _PackCover(self,query_get):
		_dict = {
			"article_id":query_get.id,
			"role_value":query_get.role.value,
			"cover":query_get.cover_image.url if query_get.tag is not None else "",
			#"cover":query_get.cover,
			"title":query_get.title, # 七牛云自动缩略图
			"issue_time":query_get.issue_time.strftime("%Y-%m-%d"),
			"click_rate":query_get.click_rate,
			"is_banner":query_get.is_banner, #是广告
		}
		return _dict

	#获取文章详细内容
	def _PackContent(self,_article):
		_article_content = {
			"status":"true",
			"article_id":_article.id,

			"father_tag_id":_article.tag.father_id if _article.tag.father is not None else "",
			"tag_id":_article.tag_id,
			"role_id":_article.role_id,
			"role_value":_article.role.value,

			#综合
			"click_rate":_article.click_rate,
			"is_top":_article.is_top,

			#封面标题
			"is_show_title": _article.is_show_title,
			"cover" :_article.cover_image.url if _article.tag is not None else "",
			#"cover":_article.cover,
			"title":_article.title, # 七牛云自动缩略图
			"subtitle":_article.subtitle,

			#摘要 发布时间
			"summary":_article.summary,
			"source":_article.source,
			"issue_time":_article.issue_time.strftime("%Y-%m-%d"),

			#正文
			"content_width":_article.content_width,
			"content":_article.content,

			#音频
			'is_show_audio': _article.is_show_audio,
			'audio_poster': _article.audio_poster,
			'audio_name': _article.audio_name,
			'audio_author': _article.audio_author,
			'audio_src': _article.audio_src,

			#视频
			'is_show_video': _article.is_show_video,
			'video_src': _article.video_src,

			#小程序跳转
			"is_show_navigate":_article.is_show_navigate,
		}
		return _article_content

	# 1 首页初始化前5个滚动栏——获取滚动栏
	def GetSwiper(self):
		_swiper_query = Article.objects.filter(tag_id = TAG_SWIPER,is_show=YES)[:5]
		return self._PackList(self._PackCover,_swiper_query)

	# 2 首页初始化前10个广告——获取广告
	# arg1：广告
	# arg2：同一父目录
	def GetBanner(self,son_tag_id):
		_fatehr_tag_id = Tag.objects.get(id = son_tag_id).father_id #子标签所属父标签
		ad_tag = Tag.objects.filter(father_id = _fatehr_tag_id ,is_ad = YES )  #广告标签
		if ad_tag.exists() is False:
			return []
		_banner_query = Article.objects.filter(tag=ad_tag[0].id,is_show=YES)[:10]
		# _banner_query = Article.objects.filter(tag_id = TAG_BANNER ,is_ad = YES)[:10]
		return self._PackList(self._PackCover,_banner_query)

	# 3 点击标签——获取文章列表
	def GetArticleByTag(self,tag_id,start_index,end_index):
##		_query1 = Article.objects.filter(tag_id=tag_id,is_show=YES)
		_query = Article.objects.filter(tag_id=tag_id,is_show=YES)[start_index:end_index]
		return self._PackList(self._PackCover,_query)

	# 4 根据ID——获取文章
	def GetArticleByID(self,article_id):
		_query = Article.objects.get(id=article_id)
		return self._PackContent(_query)

	# 5 根据时间——搜索文章
	def GetSearch(self,keyword_title,start_index,end_index,start_date, end_date):
		if start_date == "":
			start_date =  now().date() + timedelta(days=-7)
		else:
			start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")

		if end_date == "":
			end_date = now().date()
		else:
			end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")

		if keyword_title == "":
			_query = Article.objects.exclude(tag=None).filter(
				is_show=YES,
				issue_time__range = (start_date, end_date)
			)[start_index:end_index]
		else:
			_query = Article.objects.exclude(tag=None).filter(
				title__icontains = keyword_title ,
				is_show=YES,
				issue_time__range = (start_date, end_date)
			)[start_index:end_index]
		return self._PackList(self._PackCover,_query)
	# 6 会议模块 —— 获取会议文章
	def GetMeet(self,start_index,end_index):
		_query = Article.objects.filter(tag_id=TAG_MEET,is_show=YES)[start_index:end_index]
		return self._PackList(self._PackCover,_query)









	# #搜索文章
	# def GetSearchTemp(self,keyword_title,start_index,end_index):
	# 	_query = Article.objects.filter(
	# 		title__icontains = keyword_title ,
	# 		is_show=YES)[start_index:end_index]
	# 	return self._PackList(self._PackCover,_query)











	# def _pack_article(self,article):
	# 	_article = article
	# 	_article_content = {
	# 		"status":"true",
	# 		"id":_article.id,
	#
	# 		#综合
	# 		"click_rate":_article.click_rate,
	# 		"is_top":_article.is_top,
	#
	# 		#封面标题
	# 		"is_show_title":_article.is_show_title,
	# 		"cover":_article.cover,
	# 		"title":_article.title, # 七牛云自动缩略图
	# 		"subtitle":_article.subtitle,
	#
	# 		#摘要 发布时间
	# 		"summary":_article.summary,
	# 		"source":_article.source,
	# 		"issue_time":_article.issue_time.strftime("%Y-%m-%d"),
	#
	# 		#正文
	# 		"content_width":_article.content_width,
	# 		"content":_article.content,
	#
	# 		#音频
	# 		'is_show_audio': _article.is_show_audio,
	# 		'audio_poster': _article.audio_poster,
	# 		'audio_name': _article.audio_name,
	# 		'audio_author': _article.audio_author,
	# 		'audio_src': _article.audio_src,
	#
	# 		#视频
	# 		'is_show_video': _article.is_show_video,
	# 		'video_src': _article.video_src,
	# 	}
	# 	return _article_content
	#
	# #包装文章列表
	# def _pack_article_list(self,article_list):
	# 	_article_list = []
	# 	for _art in article_list:
	# 		_article_list.append({
	# 			"id":_art.id,
	# 			"role_id":_art.role_id,
	# 			"click_rate":_art.click_rate,
	# 			"cover":_art.cover,
	# 			"title":_art.title, # 七牛云自动缩略图
	# 			"subtitle":_art.subtitle,
	# 			"create_time":_art.create_time.strftime("%Y.%m.%d"),
	# 			"issue_time":_art.issue_time.strftime("%Y.%m.%d"),
	# 			"is_banner":NO, #不是广告
	# 		})
	# 	return _article_list
	#
	# #包装头条广告
	# def _pack_swiper_list(self):
	# 	_banner_list = []
	# 	_query = Banner.objects.filter(is_swiper = YES)[:5]
	# 	for banner in _query:
	# 		_banner_list.append({
	# 			"banner_id":banner.id,
	# 			"id":banner.article_id,
	# 			"tag_id":banner.tag_id,
	# 			"cover":banner.cover,
	# 			"serial":banner.serial,
	# 		})
	# 	return _banner_list
	#
	# def _pack_tag_banner_list(self,tag_id):
	# 	_banner_list = []
	# 	_query = Banner.objects.filter(is_swiper = NO, tag_id = tag_id)
	# 	for banner in _query:
	# 		_banner_list.append({
	# 			"banner_id":banner.id,
	# 			"id":banner.article_id,
	# 			"title":banner.article.title, # 七牛云自动缩略图
	# 			"tag_id":banner.tag_id,
	# 			"cover":banner.cover,
	# 			"serial":banner.serial,
	# 			"is_banner":YES, #是广告
	# 		})
	# 	return _banner_list
	#
	# #TODO 每页加一条广告
	# def _mix_article_banner(self,_article_list,_banner_list,page_num):
	# 	_len = len(_banner_list)
	# 	_len_article = len(_article_list)
	# 	if _len>0 and _len_article > PAGE_SIZE-3: #文章大于每页数量-2，则加入广告
	# 	# if _len>0 :
	# 		_index_banner =  page_num%_len
	# 		_article_list.insert(4,_banner_list[_index_banner]) #在第四个位置插第一个广告
	# 	return _article_list
	#
	#
	# #界面初始化
	# def GetIndex(self,_default_tag):
	# 	#首页显示标签
	# 	_tag_list = []
	# 	_tag_query = Tag.objects.filter(is_show = YES) #隐藏标签不显示。
	# 	for _t in _tag_query:
	# 		_tag_list.append({
	# 			"id":_t.id,
	# 			"name":_t.name,
	# 		})
	# 	_keyword =  Tag.objects.get(id=_default_tag).name
	# 	_article_list,_has_more = self.GetArticleByTag(  _default_tag ,PAGE_NUM)
	# 	_swiper_list = self._pack_swiper_list()
	# 	#关键字名称，tag列表，文章列表
	# 	return 	_keyword , \
	# 			_tag_list,\
	# 		    _article_list, \
	# 			_swiper_list
	#
	#
	# #根据标签获取文章，
	# # TODO 预留分页加载
	# def GetArticleByTag1(self,_tag_id,page_num):
	# 	_tag = Tag.objects.get(id=_tag_id)
	#
	# 	#分页加载
	# 	_page_num = int(page_num)
	# 	_page_size = PAGE_SIZE
	# 	_has_more = True
	# 	# _add_article_list = []
	#
	# 	_query_2 = _tag.article_set.filter(is_top = NO,is_show=YES) #查询不置顶的文章
	# 	_new_article_query =_query_2[ _page_num*_page_size : (_page_num+1)*_page_size ] #分页
	# 	_article_list = self._pack_article_list(  _new_article_query )
	#
	# 	#文章置顶 拼接
	# 	if _page_num == 0: #页面为0，加载头条
	# 		_query_1 = _tag.article_set.filter(is_top = YES,is_show=YES)
	# 		_list1 = self._pack_article_list(  _query_1 )
	# 		_article_list = _list1 + _article_list
	#
	# 	#计算是否有剩余
	# 	_count = _query_2.count()
	# 	_index = _page_num * _page_size
	# 	if _index < _count:
	# 		_has_more = True
	# 	else :
	# 		_has_more = False
	#
	# 	#混合广告
	# 	_banner_list = self._pack_tag_banner_list(_tag_id)
	# 	_article_list = self._mix_article_banner(_article_list,_banner_list,_page_num)
	# 	return _article_list,_has_more
	#
	# # TODO 预留分页加载
	# def GetSearch1(self,keyword_title,page_num):
	# 	_page_num = int(page_num)
	# 	_page_size = PAGE_SEARCH_SIZE
	# 	_article_query = Article.objects.filter( title__icontains = keyword_title )
	# 	_new_article_query =_article_query[ _page_num*_page_size : (_page_num+1)*_page_size ] #分页
	# 	_article_list = self._pack_article_list(  _new_article_query )
	#
	# 	#计算是否有剩余
	# 	_count = _article_query.count()
	# 	_index = _page_num * _page_size
	# 	if _index < _count:
	# 		_has_more = True
	# 	else :
	# 		_has_more = False
	# 	return _article_list,_has_more
	#
	# # # TODO 预留分页加载
	# # def GetTrace(self,keyword_title):
	# # 	_article_query = Article.objects.filter( title__icontains = keyword_title )
	# # 	return self._pack_article_list(  _article_query )
	#
	# #获取用户浏览记录
	# def GetUserTrace(self,user_id,role,page_num):
	#
	# 	_page_num = int(page_num)
	# 	_page_size = PAGE_SIZE
	#
	# 	if role == '' :
	# 		_rel_article_user = RelArticleUser.objects.filter( user = user_id)
	# 	else:
	# 		_rel_article_user = RelArticleUser.objects.filter(user=user_id,article__role_id = role)
	#
	# 	_article_query = []
	# 	for _r in _rel_article_user:
	# 		_article_query.append(_r.article)
	# 	_new_article_query =_article_query[ _page_num*_page_size : (_page_num+1)*_page_size ] #分页
	# 	_article_list = self._pack_article_list(  _new_article_query )
	#
	#
	# 	#计算是否有剩余
	# 	_count = len(_new_article_query)
	# 	_index = _page_num * _page_size
	# 	if _index < _count:
	# 		_has_more = True
	# 	else :
	# 		_has_more = False
	# 	return _article_list,_has_more
	#
	# def GetArticle(self,_article_id):
	# 	_article = Article.objects.get(id = _article_id )
	# 	return self._pack_article(  _article )
	#
	#
	# #获取会议的首页列表
	# def GetMeetIndex(self,):
	# 	#分页加载会议文章
	# 	# _page_num = int(page_num)
	# 	# _page_size = PAGE_SEARCH_SIZE
	# 	# _article_query = Article.objects.filter( title__icontains = keyword_title )
	# 	# _new_article_query =_article_query[ _page_num*_page_size : (_page_num+1)*_page_size ] #分页
	# 	# _article_list = self._pack_article_list(  _new_article_query )
	# 	#计算是否有剩余
	# 	# _count = _article_query.count()
	# 	# _index = _page_num * _page_size
	# 	# if _index < _count:
	# 	# 	_has_more = True
	# 	# else :
	# 	# 	_has_more = False
	#
	# 	#不分页加载会议文章
	# 	_tag = Tag.objects.get(id = TAG_MEET )
	# 	_article_query = _tag.article_set.filter()
	# 	# _article_query = Article.objects.filter( tag_id = TAG_MEET )
	# 	print _article_query
	# 	_article_list = self._pack_article_list(  _article_query )
	# 	return _article_list
