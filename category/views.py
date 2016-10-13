from django.shortcuts import render
from .models import  *
from django.http import HttpResponse
import requests

def send_all_category(request):
	#city_id= requests.request.get(city_id=city_id)
	try:
		response_json={}
		response_json["success"]=True
		response_json["category_data"]=[]
		for o in category_data.objects.all():
			temp_json={}
			temp_json["category_id"]=o.category_id
			temp_json["category_name"]=str(o.category_name)
			temp_json["data_type"]=o.data_type
			response_json["category_data"].append(temp_json)
	except:
		response_json["success"]=False
		response_json["message"]="category_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))



# Create your views here.
