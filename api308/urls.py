# -*- coding: utf-8 -*-


from django.conf.urls import url
from api308.views import *


urlpatterns = [

   url(r'^token/create/$', TokenCreate.as_view()),
   url(r'^cms/get/industry/$', CMSGetIndustry.as_view()),
   url(r'^cms/get/category_list/$', CMSGetCategoryList.as_view()),
   url(r'^cms/get/article_list/$', CMSGetArticleList.as_view()),

]
