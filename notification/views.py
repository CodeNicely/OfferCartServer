from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import requests
# Create your views here.
@csrf_exempt
def send_notification(request):
	if request.method=='GET':
		return render(request,"notification.html",{})
	else:
		for x,y in request.POST.items():
			print "key,value",x,":",y
		title=str(request.POST.get('title'))
		message=str(request.POST.get('message'))
		city=request.POST['city']
		#intent_type=int(request.POST['category'])
		#l=login_data.objects.create(name=name,password=password,gender=gender,email=email,description=description,city=city,mobile=mobile)
		
		for o in city_fcm_data.objects.all():
			notify_users(o.fcm,""+title+""+message)
		return render(request,"notification.html",{}) 


@csrf_exempt
def notify_users(fcm,body,title="Discount Store"):
	json= {
	"to" :str(fcm),
	"notification":{
	#"intent_id":int(intent_id),
	"body" :'"'+str(body)+'"',
	"title" :'"'+str(title)+'"',
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