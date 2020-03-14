from django.shortcuts import render,redirect
from django.views import View
from .models import *
# Create your views here.
class GalleryView(View):
	def get(self,request):
		medias=Media.objects.all()
		return render(request,'siteapp/gallery.html',{'medias':medias})
		