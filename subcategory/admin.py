from django.contrib import admin
from .models import *

class  subcategory_dataAdmin(admin.ModelAdmin):
	list_display=["subcategory_id", "subcategory_name","category_id", "shop_id"]

admin.site.register(subcategory_data, subcategory_dataAdmin)


# Register your models here.
