from __future__ import unicode_literals

from django.db import models

# Create your models here.
class offer_bought_data(models.Model):
	order_id=models.AutoField(primary_key=True)
	user_id= models.CharField(max_length=120, blank=True, null=True)
	offer_id= models.IntegerField(default=0)
	price=models.IntegerField(default=0)
	transaction_id=models.IntegerField(default=0)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)