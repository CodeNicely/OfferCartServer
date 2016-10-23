from __future__ import unicode_literals

from django.db import models

# Create your models here.
class category_data(models.Model):
	category_id = models.AutoField(primary_key= True)
	#city_id= models.SmallIntegerField(default=0)
	category_name= models.CharField(max_length=120, blank=True, null= True)
	data_type=models.SmallIntegerField(default=2)
	describ=models.CharField(max_length=120, blank=True,null= True)
	image=models.ImageField(upload_to='/media/category/',default="/media/category/default.png")
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)