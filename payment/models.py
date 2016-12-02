from __future__ import unicode_literals

from django.db import models

# Create your models here.
class payment_data(models.Model):
    transaction_id=models.CharField(max_length=15,blank=False,null=False)
    mobile=models.CharField(max_length=12,blank=False,null=False)
    amount=models.CharField(max_length=10,blank=True,null=False)
    status=models.BooleanField(default=False)
