from django.contrib import admin
from .models import *

class offer_dataAdmin(admin.ModelAdmin):
	list_display=["offer_id","name","describ","created","modified","offer_id","name","shop_id","image","category_id","price","data_type","describ","modified","created"]
admin.site.register(offer_data, offer_dataAdmin)


# Register your models here.
