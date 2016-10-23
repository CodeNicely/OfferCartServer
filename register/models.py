from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_data(models.Model):
	name= models.CharField(max_length= 120,blank= True ,null = True)
	email= models.TextField(blank= True, null= True)
	city= models.CharField(max_length=120, blank=True, null=True)
	mobile=models.IntegerField(primary_key=True,default=0)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)