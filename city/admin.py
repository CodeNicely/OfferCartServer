from django.contrib import admin
from .models import *
# Register your models here.
class city_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","created","modified"]

admin.site.register(city_data,city_dataAdmin)

class city_fcm_dataAdmin(admin.ModelAdmin):
	list_display=["id","city_id","user_id"]
admin.site.register(city_fcm_data,city_fcm_dataAdmin)
