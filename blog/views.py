from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages as msg
from .models import *

# Create your views here.
class BlogView(View):
	def get(self,request):
		recentposts=Post.objects.all().order_by('-created_on')[:7]
		popularposts=Post.objects.all().order_by('-likes','-comments','-views')[:7]

		posts=Post.objects.all().order_by('-created_on')
		p=Paginator(posts,5)
		pagecount=p.num_pages
		pages=list(range(0,pagecount))
		page_number = request.GET.get('page')
		page_obj = p.get_page(page_number)

		postlikes=[]
		if request.user.is_authenticated:
			for post in page_obj:
				postlikesobj=PostLike.objects.filter(user=request.user,post=post)
				if len(postlikesobj) > 0:
					postlikes.append(postlikesobj[0])
		return render(request,'siteapp/blog.html',{'posts':page_obj,'pages': pages,
			'recentposts':recentposts,'popularposts':popularposts,'postlikes':postlikes})
	def post(self,request):
		postid=request.POST['postid']
		post=Post.object.get(pk=postid)
		return JsonResponse({})

class BlogLikeView(View):
	def get(self,request):
		liked=None
		likescount=None
		if not request.user.is_authenticated:
			msg.info(request,'You must be logged-in to like the post.')
		else:
			postid=request.GET['postid']
			post=Post.objects.get(pk=postid)
			postlike=PostLike.objects.get_or_create(user=request.user,post=post)[0]
			if postlike.liked:
				liked='no'
				post.likes-=1
				postlike.delete()
			else:
				liked='yes'
				post.likes+=1
				postlike.liked=True
				postlike.created_on=timezone.now()
				postlike.save()
			likescount=post.likes
			post.save()
		return JsonResponse({'liked':liked,'likescount':likescount})

class BlogCommentView(View):
	def post(self,request):
		postid=request.POST['postid']
		comment=request.POST['comment']
		post=Post.objects.get(pk=postid)
		postcomment=PostComment(user=request.user,post=post,comment=comment,created_on=timezone.now())
		post.comments+=1
		postcomment.save()
		post.save()
		return render(request,'siteapp/comment.html',{'postcomment':postcomment,'comments':post.comments})

class BlogDetailsView(View):
	def get(self,request,postid):
		recentposts=Post.objects.all().order_by('-created_on')[:7]
		popularposts=Post.objects.all().order_by('-likes','-comments','-views')[:7]
		post=Post.objects.get(pk=postid)
		postcomments=PostComment.objects.filter(post=post).order_by('-created_on')
		postlikes=[]
		if request.user.is_authenticated:
			postlikesobj=PostLike.objects.filter(user=request.user,post=post)
			if len(postlikesobj) > 0:
				postlikes.append(postlikesobj[0])
		return render(request,'siteapp/blogdetails.html',{'post':post,'recentposts':recentposts,
			'popularposts':popularposts,'postlikes':postlikes,'postcomments':postcomments})