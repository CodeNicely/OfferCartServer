from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_data(models.Model):
	name= models.CharField(max_length= 120,blank= True ,null = True)
	email= models.TextField(blank= True, null= True)
	city= models.CharField(max_length=120, blank=True, null=True)
	mobile=models.IntegerField(primary_key=True,default=0)