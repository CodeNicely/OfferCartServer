from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import requests
import json
from city.models import city_fcm_data
from shop.models import shop_data

# Create your views here.
@csrf_exempt
def send_notification(request):
	#response_json={}
	if request.method=='GET':
		# shop=category_data.objects.values('id', 'name').exclude(name__isnull=True)
		# intent_type=int(request.POST['category'])
		# for o in shop:
		# 	shop_list=[]
		# 	shop_list_data={}
		# 	shop_list_data["shop_id"]=shop.id;
		# 	shop_list_data["shop_name"]=shop.name;
		# 	shop_list.append(shop_list_data)
		# 	response_json["shop_data"]=shop_list
		# print(response_json)
		#"obj_as_json":json.dumps(response_json)
		return render(request,"notification.html",{})
	else:
		for x,y in request.POST.items():
			print "key,value",x,":",y
		message=str(request.POST.get('message'))
		city=request.POST['city']
		shop_id=request.POST['shop_id']
		for o in city_fcm_data.objects.filter(city_id=city):
			notify_users(o.fcm,message,shop_id)
		return render(request,"notification.html",{}) 


@csrf_exempt
def notify_users(fcm,body,data,title="Discount Store"):
	json= {
	"to" :str(fcm),
    "notification" : {
      "body" : str(body)+"",
      "title" : str(title),
      "sound": "default",
    },
    "data" : {
      "text":"Click to check new offers",
      "message":str(body),
      "shop_id":str(shop_id),
      "shop_name":"Khushee Sarees",
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