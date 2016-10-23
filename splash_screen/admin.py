from django.contrib import admin
from .models import *
# Register your models here.
class version_dataAdmin(admin.ModelAdmin):
	list_display=["version","compulsory_update","created","modified"]

admin.site.register(version_data,version_dataAdmin)


class fcm_dataAdmin(admin.ModelAdmin):
	list_display=["fcm","created","modified"]
admin.site.register(fcm_data,fcm_dataAdmin)

