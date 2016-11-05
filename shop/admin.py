from django.contrib import admin
from .models import *
# Register your models here.
class shop_dataAdmin(admin.ModelAdmin):
	list_display=["shop_id","name","city_id","category_id","image","address","description","modified","created"]
admin.site.register(shop_data,shop_dataAdmin)

# Register your models here.
