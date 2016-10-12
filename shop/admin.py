from django.contrib import admin
from .models import *
# Register your models here.
class shop_dataAdmin(admin.ModelAdmin):
	list_display=["shop_id","shop_name"]

admin.site.register(shop_data,shop_dataAdmin)

# Register your models here.
