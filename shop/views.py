from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
import requests
from django.views.decorators.csrf import csrf_protect,csrf_exempt

@csrf_exempt
def send_all_shop(request):
	try:
		city_id= str(request.POST.get("city_id"))
		category_id=str(request.POST.get("category_id"))
		response_json={}
		response_json["success"]=True
		response_json["shop_data"]=[]
		fields=["shop_id","shop_name","category_id","city_id","data_type"]
		
		for o in shop_data.objects.filter(city_id=city_id,category_id=category_id):
			temp_json={}
			for f in fields:
				temp_json[f]=getattr(o,str(f))
			response_json["shop_data"].append(temp_json)

	except Exception,e:
		response_json["success"]=False
		response_json["message"]="shop_data not found"
		print"e@shop=", e

	print str(response_json)
	return HttpResponse(str(response_json))

# Create your views here.
