from django.contrib import admin

from .models import *


# Register your models here.
class CityDataAdmin(admin.ModelAdmin):
    list_display = ["name", "state_name", "created", "modified"]


admin.site.register(CityData, CityDataAdmin)


# Register your models here.
class StateDataAdmin(admin.ModelAdmin):
    list_display = [ "name", "created", "modified"]


admin.site.register(StateData, StateDataAdmin)


class UserCityDataAdmin(admin.ModelAdmin):
    list_display = ["city_id", "user_id"]


admin.site.register(UserCityData, UserCityDataAdmin)


# class CityFcmDataAdmin(admin.ModelAdmin):
#     list_display = ["id", "city_id", "user_id"]
#
#
# admin.site.register(CityFcmData, CityFcmDataAdmin)
