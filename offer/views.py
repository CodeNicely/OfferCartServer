from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import requests

def send_offer(request):
	try:
		category_id= str(request.POST.get("category_id"))
		shop_id=str(request.POST.get("shop_id"))
		#category_id=1
		#shop_id=1
		response_json={}
		response_json["success"]=True
		response_json["offer_data"]=[]
		for o in offer_data.objects.filter(shop_id=shop_id).filter(category_id=category_id):
			temp_json={}
			temp_json["offer_id"]=o.offer_id
			temp_json["offer_name"]=str(o.offer_name)
			temp_json["offer_des"]=str(o.offer_des)
			temp_json["offer_validdate"]=o.offer_validdate
			temp_json["data_type"]=o.data_type
			temp_json["offer_image"]=str(o.offer_image)
			temp_json["offer_code"]=str(o.offer_code)
			response_json["offer_data"].append(temp_json)

	except:
		response_json["success"]=False
		response_json["message"]=" offer_data not  found"

	print str(response_json)
	return HttpResponse(str(response_json))
# Create your views here.
