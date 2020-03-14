from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Media(models.Model):
	title=models.CharField(max_length=100)
	image=models.FileField(upload_to='galery/images',blank=True)
	video=models.FileField(upload_to='galery/videos',blank=True)
	likes=models.IntegerField(default=0)
	created_on=models.DateField(blank=True,null=True)

	def __str__(self):
		return '%s%s%s%s%s'%(self.title,self.image,self.video,self.likes,self.created_on)

class Mediafeed(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='gallery_user')
	media=models.ForeignKey(Media,on_delete=models.CASCADE,related_name='gallery_media')
	liked=models.BooleanField(default=False)
	created_on=models.DateField(blank=True,null=True)