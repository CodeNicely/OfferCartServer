from django.contrib import admin
from .models import *
# Register your models here.
class otp_dataAdmin(admin.ModelAdmin):
    list_display=["id","flag"]
admin.site.register(otp_data,otp_dataAdmin)

# Register your models here.
