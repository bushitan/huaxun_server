#coding:utf-8
from meet.models import *

class MeetAdmin():
    article_fieldsets = (
        (u"展示", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['is_show',]
        }),
        (u"标题", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['title','subtitle','summary','source',]
        }),
        (u"正文", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['content','content_width','summary','source',]
        }),
        (u"地址", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['address','work_date','phone','introduction',]
        }),
    )
    
    cover_fieldsets = (
        (u"", {
            'fields': ['meet','article']
        }),
        (u"分类", {
            'fields': ['page',]
        }),
        (u"文章", {
            'fields': ['article_title','article_summary','article_des',
                       'article_footer','article_start_time','article_end_time',]
        }),
        (u"嘉宾", {
            'fields': ['guest_name','guest_logo_image','guest_company','guest_introduction',]
        }),
    )

    def GetArticleFieldsets(self):
        return self.article_fieldsets
    def GetCoverFieldsets(self):
        return self.cover_fieldsets

    #字符串转元组
    def Str2Tuple(self,str):
        _str = str.strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()
        _tuple = tuple(eval( _str ))
        return _tuple


##(
##        (u"展示", {
##            'classes': ('suit-tab', 'suit-tab-content',),
##            'fields': ['is_show','page',]
##        }),
##        (u"标题", {
##            'classes': ('suit-tab', 'suit-tab-content',),
##            'fields': ['title','subtitle','summary','source',]
##        }),
##        (u"正文", {
##            'classes': ('suit-tab', 'suit-tab-content',),
##            'fields': ['content','content_width','summary','source',]
##        }),
##        (u"地址", {
##            'classes': ('suit-tab', 'suit-tab-content',),
##            'fields': ['address','work_date','phone','introduction',]
##        }),
##    )
