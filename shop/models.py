from __future__ import unicode_literals

from django.db import models
from city.models import city_data
from category.models import category_data
# Create your models here.
class shop_data(models.Model):
	city_name=models.ForeignKey(city_data,null=True)
	city_id= models.IntegerField(default=0,editable=False)
	category_name=models.ForeignKey(category_data,null=True)
	category_id= models.IntegerField(default=0,editable=False)
	name= models.CharField(max_length=120, blank=True, null=True)
	image=models.ImageField(upload_to='shop/',default="/media/shop/default.png")
	address= models.CharField(max_length=120, blank=True, null=True)
	description= models.CharField(max_length=120, blank=True, null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	password=models.CharField(max_length=55,blank=False,null=False,default=0)

	def __unicode__(self):
		return str(self.name)

	def save(self, *args, **kwargs):
		self.city_id = self.city_name.id
		self.category_id = self.category_name.id
		super(shop_data,self).save(*args, **kwargs)