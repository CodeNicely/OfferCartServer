from __future__ import unicode_literals

from django.db import models
# Create your models here.
class version_data(models.Model):
	version= models.SmallIntegerField(default= 0)
	compulsory_update= models.SmallIntegerField(default=0)
	ver_type=models.CharField(max_length=120, blank=True, null=True)
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	modified= models.DateTimeField(auto_now=False,auto_now_add=True)

class fcm_data(models.Model):
	fcm=models.CharField(max_length=400, blank=True, null=True)
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	modified= models.DateTimeField(auto_now=False,auto_now_add=True)
