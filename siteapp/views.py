from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages as msg
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.utils import timezone
import random
import string

from .models import *
# Create your views here.
class HomeView(View):
	def get(self,request):
		return render(request,'siteapp/home.html',{})

class LoginView(View):
	next_path=None
	email=''
	errors=[]
	def get(self,request):
		messages=msg.get_messages(request)
		if request.GET.get('next',""):
			self.next_path=request.GET['next']
		if request.user.is_authenticated:
			if self.next_path is not None:
				return redirect(self.next_path)
			else:
				return redirect("/home/")
		return render(request,'siteapp/login.html',{'errors':self.errors,'messages':messages,
			'email':self.email})
	def post(self,request):
		self.errors=[]
		self.email=request.POST['email']
		password=request.POST['password']
		checkuser=User.objects.filter(email=self.email)
		if len(checkuser)>0:
			if checkuser[0].check_password(password):
				backend='django.contrib.auth.backends.ModelBackend'
				login(request,checkuser[0],backend)
		self.errors.append('Account doen\'t exist with provided credentials')
		return self.get(request)

class RegisterView(View):
	first_name=''
	last_name=''
	email=''
	username=''
	errors=[]
	def get(self,request):
		if request.user.is_authenticated:
			return redirect("/home/")
		return render(request,'siteapp/register.html',{'fn':self.first_name,'ln':self.last_name,
			'email':self.email,'username':self.username,'errors':self.errors})
	def post(self,request):
		self.errors=[]
		if request.POST.get('fn',""):
			self.first_name=request.POST['fn']
		if request.POST.get('ln',""):
			self.last_name=request.POST['ln']
		self.email=request.POST['email']
		self.username=request.POST['username']
		np=request.POST['np']
		cp=request.POST['cp']
		try:
			usercheck=User.objects.get(username=self.username)
			self.errors.append('Username already taken')
		except:
			pass
		emailcheck=User.objects.filter(email=self.email)
		if(len(emailcheck)>0):
			self.errors.append('An account already exist with this email')
		if len(np) < 8:
			self.errors.append('Password length must be 8 or greater')
		if np != cp:
			self.errors.append('New and confirm password mismatched.')
		if not self.errors:
			password_characters = string.ascii_letters + string.digits + string.punctuation
			verify_id = ''.join(random.choice(password_characters) for i in range(32))

			user=User.objects.create_user(username=self.username,email=self.email,first_name=self.first_name,
				last_name=self.last_name,password=np)
			verify_account=AccountVerification.objects.create(user=user,verification_id=verify_id,
				created_on=timezone.now())
			login(request,user,'django.contrib.auth.backends.ModelBackend')

			subject, from_email, to = 'Divine Web Solutions', 'aneildhakal21@gmail.com', self.email
			text_content = 'Account created successfuly.'
			email_template = get_template('siteapp/account_verify_email.html')
			#context = Context({'username': self.username})
			html_content = email_template.render({'username':self.username,'verify_id':verify_id})
			emaildemo = EmailMultiAlternatives(subject, text_content, from_email, [to])
			emaildemo.attach_alternative(html_content, "text/html")
			emaildemo.send(fail_silently=False)
			
			msg.add_message(request,msg.SUCCESS,'Account created Successfully')
			return redirect('/home/')
		return self.get(request)

class LogoutView(View):
	def get(self,request):
		msg.add_message(request,msg.INFO,'Successfully logged out.')
		logout(request)
		return redirect("/home/")

class AccountVerifyView(View):
	def get(self,request,uid,verify_id):
		user=User.objects.get(pk=uid)
		verify_account=AccountVerification.objects.get(user=user,verification_id=verify_id)
		if verify_account:
			verify_account[0].verified=True
			verify_account.save()
			msg.success(request,'Your account is verified')
			return redirect('/home/')
		return HttpResponse("Something went wrong.<a href='http://localhost:8000/contact/'>Report this.</a>")
		
