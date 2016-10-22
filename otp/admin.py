from django.contrib import admin
from .models import *
# Register your models here.
class otp_dataAdmin(admin.ModelAdmin):
    list_display=["mobile","otp","flag"]
admin.site.register(otp_data,otp_dataAdmin)


class access_token_dataAdmin(admin.ModelAdmin):
    list_display=["id","access_token"]
admin.site.register(access_token_data,access_token_dataAdmin)
