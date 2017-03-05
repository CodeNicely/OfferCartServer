from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
import requests
import json
from city.models import city_fcm_data
from shop.models import shop_data
from city.models import city_data
# Create your views here.
@csrf_exempt
def send_notification(request):
	if request.method=='GET':
		shops=shop_data.objects.values('id','name','city_name')
		cities=city_data.objects.values('id','name')
		print("yes",shops)
		print("yes 1",cities)
		shop_all_data = shop_data.objects.all()
		print (shop_all_data)
		for r in shop_all_data:
			print r.city_name.name
			print r.city_name.id
		return render(request,"notification.html",{"shop_data":shops,"cities_data":cities,"city":shop_all_data})
	else:
		
		for x,y in request.POST.items():
			print "key,value",x,":",y
		message=str(request.POST.get('message'))
		city=request.POST['city']
		shop_id=request.POST.get('shops')
		cities=city_data.objects.values('id','name')
		shop_name=str(shop_data.objects.get(id=shop_id).name)
		for o in city_fcm_data.objects.filter(city_id=city):
			notify_users(o.fcm,message,shop_id,shop_name)
		return render(request,"notification.html",{"cities_data":cities}) 


@csrf_exempt
def notify_users(fcm,body,id,name,title="Discount Store"):
	json= {
	"to" :str(fcm),
    "notification" : {
      "body" : str(body)+"",
      "title" : str(title),
      "sound": "default",
      "click_action":"com.codenicely.dicountstore.home.HomePage"
    },
    "data" : {
      "message":str(body),
      "shop_id":str(id),
      "shop_name":str(name),
    }
	}
	print json
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	'Content-Type':'application/json',
	"Authorization":"key=AAAAf59-gMY:APA91bH47UFR2GGd7RUPbKLYahb6K2IVYRyzzgZpUOYZ9cQak4Zr_6Id4gUdByR48AhLpygmcTqxqzahzCylM_WipAVxlOsEva_drEXE8YJO6yhlLDD0tWPoZyLVJENXlT_ubW1_WRy8LVcwKuC7mNPNU0984hNmxQ"

	}
	#print json
	r=requests.post(url,headers=headers,json=json)
	for o in r:
		print o

@csrf_exempt
def send_shops(request):
	response_json={}
	if (request.method=='POST'):
		city_id=request.POST.get('city_id')
		shop_names=shop_data.objects.filter(city_name__id=city_id)
		response_json["shop_data"]=[]
		if(shop_names.count()==0):
			temp_json={}
			temp_json["shop_id"]=""
			temp_json["shop_name"]="No shop available"
			response_json["shop_data"].append(temp_json)
			print"debugged"
		print"debugged"
		for o in shop_names:
			temp_json={}
			print o.name
			temp_json["shop_id"]=o.id
			temp_json["shop_name"]=str(o.name)
			response_json["shop_data"].append(temp_json)
		print ("hmm",shop_names)
		if(city_id!=0):
			print ("ok",city_id)
		print str(response_json)
		return JsonResponse(response_json)

