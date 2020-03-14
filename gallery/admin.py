from django.contrib import admin
from .models import *
# Register your models here.
class MediaAdmin(admin.ModelAdmin):
	list_display=['title','image','video','likes','created_on']

admin.site.register(Media,MediaAdmin)