from django.contrib import admin
from .models import *

class offer_dataAdmin(admin.ModelAdmin):
	list_display=["offer_id","active","offer_code","name","validity","description","created","modified","shop_id","image","category_id","price","modified","created"]
admin.site.register(offer_data, offer_dataAdmin)


# Register your models here.
