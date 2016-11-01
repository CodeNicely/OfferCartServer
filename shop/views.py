from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
import requests
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import jwt
from register.models import user_data
@csrf_exempt
def shop(request):

	response_json={}
	if request.method=='GET':
		try:
			for x,y in request.GET.items():
				print x,":",y
			access_token=request.GET.get('access_token')
			json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
			print json['mobile']
			city_id=user_data.objects.get(mobile=int(json['mobile'])).city
			print "debuuged 20"
			category_id=str(request.GET.get("category_id"))
			print "debuuged 22"
			response_json["success"]=True
			response_json["message"]='Successful'
			response_json["shopDatas"]=[]
			fields=["shop_id","shop_name","shop_image","address","category_id","city_id","data_type"]
			print "debuuged 27"
			for o in shop_data.objects.filter(city_id=city_id,category_id=int(category_id)):
				print "debuuged 29"
				temp_json={}
				for f in fields:
					print "f=",f
					temp_json[f]=str(getattr(o,str(f)))
				response_json["shopDatas"].append(temp_json)

		except Exception,e:
			response_json={}
			
			response_json["success"]=False
			response_json["message"]="shop_data not found"
			print"e@shop=", e

		print str(response_json)
	else:
		response_json['success']=False
		response_json['message']="not get method"

	return HttpResponse(str(response_json))

# Create your views here.
