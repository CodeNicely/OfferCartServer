from django.contrib import admin
from .models import *

class image_dataAdmin(admin.ModelAdmin):
	list_display=["image_id", "image_url", "message","created","modified"]

admin.site.register(image_data, image_dataAdmin)
# Register your models here.
