from __future__ import unicode_literals

from django.db import models

class subcategory_data(models.Model):
	subcategory_id= models.AutoField(primary_key=True)
	shop_id= models.SmallIntegerField(default=0)
	category_id=models.SmallIntegerField(default=0)
	data_type=models.SmallIntegerField(default=3)
	subcategory_name=models.CharField(max_length=120, blank=True, null=True)
	

# Create your models here.
