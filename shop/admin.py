from django.contrib import admin
from .models import *
# Register your models here.
class shop_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","city_id","city_name","city_id","category_name","category_id","image","description","modified","created"]
admin.site.register(shop_data,shop_dataAdmin)

# Register your models here.
