from django.contrib import admin

from subscription.models import SubscriptionData, ShopSubscriptionData


class SubscriptionDataAdmin(admin.ModelAdmin):
    list_display = ["id", "subscription_title", "subscription_description","subscription_price","subscription_days" ,"modified", "created"]


admin.site.register(SubscriptionData, SubscriptionDataAdmin)


class ShopSubscriptionDataAdmin(admin.ModelAdmin):
    list_display = ["id","shop_id", "subscription_id", "payment_status", "modified", "created"]


admin.site.register(ShopSubscriptionData, ShopSubscriptionDataAdmin)