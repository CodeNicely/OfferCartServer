from __future__ import unicode_literals

from django.db import models

# Create your models here.
class category_data(models.Model):
	category_id = models.AutoField(primary_key= True)
	city_id= models.SmallIntegerField(default=0)
	category_name= models.CharField(max_length=120, blank=True, null= True)
	data_type=models.SmallIntegerField(default=2)