from django.contrib import admin
from .models import *
# Register your models here.
class category_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","describ","image","modified","created"]

#	list_display=["category_id","category_name"]

admin.site.register(category_data,category_dataAdmin)

# Register your models here.
