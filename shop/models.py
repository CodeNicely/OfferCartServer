from __future__ import unicode_literals

from django.db import models

# Create your models here.
class shop_data(models.Model):
	shop_id= models.AutoField(primary_key= True)
	city_id= models.SmallIntegerField(default=0)
	category_id= models.SmallIntegerField(default=0)
	shop_name= models.CharField(max_length=120, blank=True, null=True)
	data_type=models.SmallIntegerField(default=3)
	address= models.CharField(max_length=120, blank=True, null=True)
	describ= models.CharField(max_length=120, blank=True, null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)