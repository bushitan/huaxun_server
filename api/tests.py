# -*- coding: utf-8 -*-
import django
django.setup()
# Create your tests here.

# from api.lib.hx_article import *
#


##from api.hx.hx_tag import *
##from api.hx.hx_role import *
##from api.hx.hx_article import *
# t = HX_Tag()
# print t.GetSonListByFather(1)
# print t.GetFatherList()
# print t.GetTree()

# r = HX_Role()
# print r.GetMemberByUser(3)
# print r.CheckValue(3,3)
# a = HX_Article()

from api.models.article import *
a = Article.objects.filter(tag__father = 1)
b = Article.objects.filter(tag__father = 1)[0:10]
print a


# start_date = datetime.date(2017, 12, 1)
# end_date = datetime.date(2017, 12, 31)
# # print a.GetSearchTemp("",0,10,start_date, end_date)
# print a.GetSearchTemp("",0,10,"","")
# import time
#
# date = datetime.date(2017,12,30)
#
# str = "2017-12-29"
# str2 = "2017-12-31"
# print Article.objects.get(id=290).issue_time
# print Article.objects.filter(issue_time__range=(str, str2))



# import cv2
# import cv2.cv as cv #here
# import numpy as np
# import matplotlib.pyplot as plt
#
# img = cv2.imread('1.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# plt.subplot(121),plt.imshow(gray,'gray')
# plt.xticks([]),plt.yticks([])
#
# circles1 = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,
# 600,param1=100,param2=30)
# # circles1 = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,
# # 600,param1=100,param2=30,minRadius=80,maxRadius=97)
# print datetime.datetime.now()
# print circles1
# circles = circles1[0,:,:]
# circles = np.uint16(np.around(circles))
# for i in circles[:]:
# 	cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)
# 	cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)
# 	cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)
# 	print u"圆心坐标",i[0],i[1]
# print circles
# plt.subplot(122),plt.imshow(img)
# plt.xticks([]),plt.yticks([])
#
# print datetime.datetime.now()
