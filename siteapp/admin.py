from django.contrib import admin
from .models import *
# Register your models here.
class AccountVerificationAdmin(admin.ModelAdmin):
	list_display=['user','verification_id','verified','created_on']
		
admin.site.register(AccountVerification,AccountVerificationAdmin)