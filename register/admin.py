from django.contrib import admin
from .models import *
# Register your models here.
class user_dataAdmin(admin.ModelAdmin):
    list_display=["id","name","email","city","mobile"]
admin.site.register(user_data,user_dataAdmin)

# Register your models here.
