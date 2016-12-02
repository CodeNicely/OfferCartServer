from django.contrib import admin
from .models import *
# Register your models here.
class payment_dataAdmin(admin.ModelAdmin):
    list_display=["mobile","amount","transaction_id","status"]
admin.site.register(payment_data,payment_dataAdmin)