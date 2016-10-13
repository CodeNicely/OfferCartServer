from django.contrib import admin
from .models import *

class offer_dataAdmin(admin.ModelAdmin):
	list_display=["offer_id","offer_name","offer_des","offer_code","offer_validdate",]

admin.site.register(offer_data, offer_dataAdmin)


# Register your models here.
