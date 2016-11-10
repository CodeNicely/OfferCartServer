from django.contrib import admin
from .models import *
# Register your models here.
class city_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","created","modified"]

admin.site.register(city_data,city_dataAdmin)

# Register your models here.
