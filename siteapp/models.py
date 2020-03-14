from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AccountVerification(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
	verification_id=models.CharField(max_length=64)
	verified=models.BooleanField(default=False)
	created_on=models.DateTimeField(blank=True,null=True)
		