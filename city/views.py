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
				print o.name
				temp_json["city_id"]=o.id
				temp_json["city_name"]=str(o.name)
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
			fcm_city=request.POST.get('fcm')
			print fcm_city
			json=jwt.decode(str(access_token),'999123',algorithms='HS256')
			print"debuuged 43"
			user_list=user_data.objects.get(mobile=str(json['mobile']))
			city_fcm,created=city_fcm_data.objects.get_or_create(fcm=fcm_city,city_id=city_id,user_id=str(json['mobile']))
			print"debuuged 45"
			setattr(user_list,'city',int(city_id))
			user_list.save()
			city_fcm.save()
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
@csrf_exempt
def update_fcm(request):
	response_json={}
	try:
		for x,y in request.POST.items():
			print "key,value",x,":",y
		access_token=str(request.POST.get('access_token'))
		json=jwt.decode(str(access_token),'999123',algorithms='HS256')
		fcm=str(request.POST.get('fcm'))
		print fcm
		if fcm!=None:
			data=city_fcm_data.objects.filter(user_id=str(json['mobile']))
			for d in data:
				setattr(d,'fcm',fcm)
				d.save()
			# data.save()
			response_json['success']=True
			response_json['message']="fcm updated successfully"
		else:
			response_json['success']=False
			response_json['message']="fcm is null so it cannot be updated"	
	except Exception,e:
		response_json['success']=False
		response_json['message']="fcm cannot be updated"
		print "error@city_fcm  post",e
	print str(response_json)
	return JsonResponse(response_json)

