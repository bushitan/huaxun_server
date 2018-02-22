#coding:utf-8
from django.contrib import admin

# Register your models here.
from meet_sign.models import *


##class ImageLibraryAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(ImageLibrary,ImageLibraryAdmin)
##
####2
##class ArticleLibraryAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(ArticleLibrary,ArticleLibraryAdmin)
##
####3
##class PageAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(Page,PageAdmin)
##
####4
##class MeetAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(Meet,MeetAdmin)

##5
class BillAdmin(admin.ModelAdmin):
    list_display = ('id','name_admin','name','meet',)
admin.site.register(Bill,BillAdmin)

##6
class DiscountTemplateAdmin(admin.ModelAdmin):
    pass
admin.site.register(DiscountTemplate,DiscountTemplateAdmin)


##6.2
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','order',)
admin.site.register(Attendee,AttendeeAdmin)


##7
class DiscountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Discount,DiscountAdmin)

##8
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','bill','is_pay',)
admin.site.register(Order,OrderAdmin)

##9
##class CoverAdmin(admin.ModelAdmin):
##    list_display = ('id','page','meet','article',)
##    raw_id_fields = ('cover_image','logo_image',)  #选择封面图片
##admin.site.register(Cover,CoverAdmin)

