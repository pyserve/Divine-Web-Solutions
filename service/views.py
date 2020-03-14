from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class ServicesView(View):
	def get(self,request):
		services=Service.objects.all()
		return render(request,'siteapp/services.html',{'services':services})