from django.contrib import admin
from .models import *

# Register your models here.
class PostMediaAdmin(admin.ModelAdmin):
	list_display=['image','video']

class PostAdmin(admin.ModelAdmin):
	list_display=['title','user','likes','comments','views','created_on']

class PostLikeAdmin(admin.ModelAdmin):
	list_display=['user','post','liked','created_on']

class PostCommentAdmin(admin.ModelAdmin):
	list_display=['user','post','comment','created_on']

admin.site.register(PostMedia,PostMediaAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(PostLike,PostLikeAdmin)
admin.site.register(PostComment,PostCommentAdmin)