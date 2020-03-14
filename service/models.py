from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicefile(models.Model):
	file=models.FileField(upload_to='service_files',null=True)

class Service(models.Model):
	name=models.CharField(max_length=200)
	logo=models.FileField(upload_to='service_logos')
	description=models.TextField(blank=True)
	files=models.ManyToManyField(Servicefile,blank=True)
	created_on=models.DateTimeField(blank=True,null=True)