from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages as msg
from django.views import View

# Create your views here.
class ContactView(View):
	name=''
	email=''
	number=''
	message=''
	errors=[]
	def get(self,request):
		messages=msg.get_messages(request)
		return render(request,'siteapp/contact.html',{'messagess':messages})
	def post(self,request):
		self.errors=[]
		self.email=request.POST['email']
		if request.POST.get('name',""):
			self.name=request.POST['name']
		if request.POST.get('number',""):
			self.number=request.POST['number']
		if request.POST.get('message',""):
			self.message=request.POST['message']
		if not self.errors:
			msg.success(request,'Your CallBack is registered successfully, we\'ll reach you as soon as possible')
			return JsonResponse({'success':'1'})
		return JsonResponse({'success':'0'})
		