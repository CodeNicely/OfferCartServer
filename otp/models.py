from __future__ import unicode_literals

from django.db import models

# Create your models here.
class otp_data(models.Model):
	id = models.AutoField(primary_key=True)
	otp= models.DecimalField(max_digits= 4, default=0,decimal_places=0)
	flag=models.SmallIntegerField(default=0)
	mobile= models.DecimalField(max_digits= 10 ,decimal_places=0, default= 0)

class user_token_data(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    access_token=models.CharField(max_length=120,blank=True,null=True)
