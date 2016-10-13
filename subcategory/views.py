from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import *

def send_all_subcategory(request):
	try:
		category_id=str(request.POST.get("category_id"))
		shop_id=str(request.POST.get("shop_id"))
		response_json={}
		response_json["success"]=True
		response_json["subcategory_data"]=[]
		for o in subcategory_data.objects.all():
		#for o in subcategory_data.objects.filter(category_id= "category_id", shop_id= "shop_id"):
			temp_json={}
			temp_json["subcategory_id"]=o.subcategory_id
			temp_json["subcategory_name"]=str(o.subcategory_name)
			temp_json["data_type"]=o.data_type
			response_json["subcategory_data"].append(temp_json)
	except:
		response_json["success"]=False
		response_json["message"]="subcategory_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))

# Create your views here.
