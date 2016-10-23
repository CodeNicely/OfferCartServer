from __future__ import unicode_literals

from django.db import models

# Create your models here.
class otp_data(models.Model):
	mobile= models.IntegerField(primary_key=True, null=False)
	otp= models.PositiveSmallIntegerField(default=0,null=True)
	flag=models.BooleanField(default=False)
	
class access_token_data(models.Model):
    id=models.AutoField(primary_key=True)
    access_token=models.CharField(max_length=500,blank=True,null=True)
