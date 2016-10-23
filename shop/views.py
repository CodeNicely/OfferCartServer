from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
import requests
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import jwt
from register.models import user_data
@csrf_exempt
def shop(request):
	try:
		access_token=request.POST.get('access_token')
		json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
		print json['mobile']
		city_id=user_data.objects.get(mobile=int(json['mobile'])).city
		category_id=str(request.GET.get("category_id"))
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
