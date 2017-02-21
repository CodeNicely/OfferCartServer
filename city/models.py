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
	#city_name=models.ForeignKey(city_data,related_name='user1',null=True)
	city_id=models.CharField(max_length=100,blank=True,null=True)
	fcm=models.CharField(max_length=100,blank=True,null=True)
	user_id=models.CharField(max_length=100,blank=True,null=True)
	#user_mobile=models.ForeignKey(user_data,related_name='user2',null=True)
	#user_id=models.CharField(max_length=100,blank=False,null=False)

	def __unicode__(self):
		return str(self.city_id)

	# def save(self, *args, **kwargs):
	# 	self.city_id = self.city_name.id
	# 	#self.user_id = self.user_mobile.mobile
	# 	super(city_fcm_data,self).save(*args, **kwargs)