from __future__ import unicode_literals

from django.db import models

class image_data(models.Model):
	image_id= models.IntegerField(primary_key= True)
	image_url=models.CharField(max_length=120, blank= True, null=True)
	message= models.CharField(max_length=120, blank= True, null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)