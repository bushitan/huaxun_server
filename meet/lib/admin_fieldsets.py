#coding:utf-8
from util import *
# ARTICLE_STYLE_NORMAL = 1
# ARTICLE_STYLE_TEXT = 2
# ARTICLE_STYLE_AUDIO = 3
# ARTICLE_STYLE_VIDEO = 4
def ArticleFieldsets(style):
	print style,style == ARTICLE_STYLE_TEXT
	if style == ARTICLE_STYLE_TEXT:
		return Text()
	if style == ARTICLE_STYLE_AUDIO:
		return Audio()
	if style == ARTICLE_STYLE_VIDEO:
		return Video()
	return Normal()

# 纯文字
def Text():
	_tuple = (
        (u"展示", {
            'fields': ['is_show','style',]
        }),
    )
	return _tuple
# 纯文字
def Audio():
	_tuple = (
        (u"展示", {
            'fields': ['is_show','style',]
        }),
        (u"标题", {
            'fields': ['title','subtitle','summary','source',]
        }),
    )
	return _tuple

def Video():
	_tuple = (
        (u"展示", {
            'fields': ['is_show','style',]
        }),
        (u"标题", {
            'fields': ['title','subtitle','summary','source',]
        }),
        (u"正文", {
            'fields': ['content','content_width','summary','source',]
        }),
    )
	return _tuple

def Normal():
	_tuple = (
        (u"展示", {
            'fields': ['is_show','style',]
        }),
        (u"标题", {
            'fields': ['title','subtitle','summary','source',]
        }),
        (u"正文", {
            'fields': ['content','content_width','summary','source',]
        }),
        (u"地址", {
            'fields': ['address','work_date','phone','introduction',]
        }),
    )
	return _tuple