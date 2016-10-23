from django.contrib import admin

# Register your models here.
from .models import *
class keys_dataAdmin(admin.ModelAdmin):
	list_display=["key","value","created","modified"]
admin.site.register(keys,keys_dataAdmin)
# Register your models here.
