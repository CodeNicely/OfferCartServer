from __future__ import unicode_literals

from django.db import models

class image_data(models.Model):
	image_id= models.IntegerField(primary_key= True)
	image_url=models.CharField(max_length=120, blank= True, null=True)
	message= models.CharField(max_length=120, blank= True, null=True)
	#image_type=models.CharField(max_length=120,blank=True,null=True)

# Create your models here.
