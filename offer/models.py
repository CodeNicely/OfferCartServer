from __future__ import unicode_literals

from django.db import models

class offer_data(models.Model):
	offer_id= models.AutoField(primary_key=True)
	name=models.CharField(max_length=120, blank=True,null=True)
	shop_id= models.SmallIntegerField(default=0)
	image=models.CharField(max_length=120,blank=True,null=True)
	category_id=models.SmallIntegerField(default=0)
	data_type=models.SmallIntegerField(default=4)
	describ=models.CharField(max_length=200,blank=True,null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)