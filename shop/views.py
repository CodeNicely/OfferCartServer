from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
import requests

def send_all_shop(request):
	try:
		response_json={}
		response_json["success"]=True
		response_json["shop_data"]=[]
		for o in shop_data.objects.all():
			temp_json={}
			temp_json["shop_id"]=o.shop_id
			temp_json["shop_name"]=str(o.shop_name)
			temp_json["category_id"]=o.category_id
			temp_json["city_id"]=o.city_id
			temp_json["data_type"]=o.data_type
			response_json["shop_data"].append(temp_json)
	except:
		response_json["success"]=False
		response_json["message"]="shop_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))

# Create your views here.
