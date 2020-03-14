from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostMedia(models.Model):
	image=models.FileField(upload_to='post_medias/images',blank=True)
	video=models.FileField(upload_to='post_medias/videos',blank=True)
	poster=models.FileField(upload_to='post_medias/videos/poster',blank=True)
	def __str__(self):
		return '%s%s' %(self.image,self.video)

class Post(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	description=models.TextField(blank=True)
	file=models.ManyToManyField(PostMedia,blank=True)
	likes=models.IntegerField(default=0)
	comments=models.IntegerField(default=0)
	views=models.IntegerField(default=0)
	created_on=models.DateTimeField(blank=True,null=True)

class PostLike(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='postlike_user')
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postlike_post')
	liked=models.BooleanField(default=False)
	created_on=models.DateTimeField(blank=True,null=True)

class PostComment(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='postcomment_user')
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postcomment_post')
	comment=models.CharField(max_length=1000,blank=True)
	created_on=models.DateTimeField(blank=True,null=True)
			
		