from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests

def send_all_city(request):
	try:
		response_json={}
		response_json["success"]=True
		response_json["city_data"]=[]
		for o in city_data.objects.all():
			temp_json={}
			temp_json["city_id"]=o.city_id
			temp_json["city_name"]=str(o.city_name)
			temp_json["data_type"]=o.data_type
			response_json["city_data"].append(temp_json)

	except:
		response_json["success"]=False
		response_json["message"]="city data not found"
	print str(response_json)
	return HttpResponse(str(response_json))
# Create your views here.
