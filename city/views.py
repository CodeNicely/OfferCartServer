from django.shortcuts import render
from .models import *
from register.models import * 
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.http import JsonResponse
import jwt
from django.views.decorators.csrf import csrf_exempt
from register.models import user_data
@csrf_exempt
def city(request):
	if(request.method=="GET"):
		try:
			response_json={}
			response_json["success"]=True
			response_json["city_data"]=[]
			print"debugged"
			for o in city_data.objects.all():
				temp_json={}
				print o.city_name
				temp_json["city_id"]=o.city_id
				temp_json["city_name"]=str(o.city_name)
				#temp_json["data_type"]=o.data_type
				response_json["city_data"].append(temp_json)

		except Exception,e:
			print "error@city get",e
			response_json["success"]=False
			response_json["message"]="city data not found"
		print str(response_json)
		return JsonResponse(response_json)
	
	if(request.method=="POST"):
		try:
			response_json={}
			
			city_id=request.POST.get('city_id')
			print"debuuged 39"
			access_token=request.POST.get('access_token')
			print"debuuged 41"
			print access_token
			json=jwt.decode(str(access_token),'999123',algorithms='HS256')
			print"debuuged 43"
			user_list=user_data.objects.get(mobile=str(json['mobile']))
			print"debuuged 45"
			setattr(user_list,'city',int(city_id))
			user_list.save()
			response_json['success']=True
			response_json['message']='Successful'
			pass
		except Exception,e:
			response_json["success"]=False
			response_json["message"]="City data not found"
			print "error@city post",e
		print str(response_json)
		return JsonResponse(response_json)
# Create your views here.
