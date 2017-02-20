from __future__ import unicode_literals

from django.db import models

# Create your models here.
class city_data(models.Model):
	name= models.CharField(max_length=120, blank=True, null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	
	def __unicode__(self):
		return str(self.name)

class city_fcm_data(models.Model):
	city=models.IntegerField(default=0)
	fcm=models.CharField(max_length=100,blank=True,null=True)
	mobile=models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.city)