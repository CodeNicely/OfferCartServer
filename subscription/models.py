from __future__ import unicode_literals

from django.db import models

from shop.models import ShopData


class SubscriptionData(models.Model):
    subscription_title = models.CharField(max_length=255)
    subscription_description = models.CharField(max_length=255, default="Subscription Details")
    subscription_price = models.PositiveIntegerField()
    subscription_days = models.IntegerField()
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


class ShopSubscriptionData(models.Model):
    shop_id = models.ForeignKey(ShopData)
    subscription_id = models.ForeignKey(SubscriptionData, db_column="SubscriptionData.id")
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
