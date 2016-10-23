from django.shortcuts import render
from .models import *
from register.models import * 
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.http import JsonResponse
import jwt
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def city(request):
	if(request.method=="GET"):
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
		return JsonResponse(response_json)
	
	if(request.method=="POST"):
		try:
			response_json={}
			
			city_id=request.POST.get('city')
			access_token=request.POST.get('access_token')
			json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
			
			user_list=user_data.objects.get(mobile=int(json['mobile']))
			setattr(user_list,'city',str(city_id))
			user_list.save()
			response_json['success']=True
			response_json['message']='Successful'
			pass
		except:
			response_json["success"]=False
			response_json["message"]="City data not found"
		print str(response_json)
		return JsonResponse(response_json)
# Create your views here.
