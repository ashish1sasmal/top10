from django.contrib import admin

# Register your models here.
from .models import *

class AlbumAdmin(admin.ModelAdmin):
	list_display=['name','artist','link']


class UserInfoAdmin(admin.ModelAdmin):
	list_display=['user']

admin.site.register(Album,AlbumAdmin)
admin.site.register(UserInfo,UserInfoAdmin)