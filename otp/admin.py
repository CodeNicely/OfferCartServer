from django.contrib import admin
from .models import *
# Register your models here.
class otp_dataAdmin(admin.ModelAdmin):
    list_display=["mobile","otp","flag","created","modified"]
admin.site.register(otp_data,otp_dataAdmin)


class access_token_dataAdmin(admin.ModelAdmin):
    list_display=["id","access_token","created","modified"]
admin.site.register(access_token_data,access_token_dataAdmin)
