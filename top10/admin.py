from django.contrib import admin

# Register your models here.
from .models import Album

class AlbumAdmin(admin.ModelAdmin):
	list_display=['name','artist','link']

admin.site.register(Album,AlbumAdmin)