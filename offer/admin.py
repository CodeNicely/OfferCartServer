from django.contrib import admin
from .models import *

class offer_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","active","shop_name","shop_id","validity","image","description","created","modified","price"]
admin.site.register(offer_data, offer_dataAdmin)

