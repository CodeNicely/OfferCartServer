from django.contrib import admin
from .models import *
# Register your models here.
class offer_bought_dataAdmin(admin.ModelAdmin):
	list_display=["user_id","offer_id","price","created","modified"]
admin.site.register(offer_bought_data,offer_bought_dataAdmin)

# Register your models here.
