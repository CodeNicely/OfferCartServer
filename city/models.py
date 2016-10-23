from __future__ import unicode_literals

from django.db import models

# Create your models here.
class city_data(models.Model):
	city_id= models.AutoField(primary_key= True)
	city_name= models.CharField(max_length=120, blank=True, null=True)
	data_type=models.IntegerField(default=1)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)