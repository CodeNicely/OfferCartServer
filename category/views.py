from django.shortcuts import render
from .models import  *
from django.http import HttpResponse
import requests
from register.models import user_data

def category(request):
	# if(request.method=="POST"):
	# 	access_token=str(request.POST.get('access_token'))
	# 	fcm=str(request.POST.get('fcm'))
	# 	json=jwt.decode(str(access_token),'999123',algorithms='HS256')
	# 	mobile_number=str(json['mobile'])
	# 	if (city_fcm_data.objects.filter(user_id=mobile_number)):
	# 		print "ok"
	# 	city_id=user_data.objects.filter(mobile=mobile_number).values('city')
	# 	city_fcm,created=city_fcm_data.objects.get_or_create(fcm=fcm_city,city_id=city_id,user_id=mobile_number)
	try:
		response_json={}
		response_json["success"]=True
		response_json['message']="Successful"
		response_json["categoryDatas"]=[]
		for o in category_data.objects.all():
			temp_json={}
			temp_json["category_id"]=int(o.id)
			temp_json["name"]=str(o.name)
#			temp_json["image"]='https://www.aldi.com.au/typo3temp/pics/ALC6158_KVB_Groceries_1896x720_582e750e6c.jpg'#str(o.image)
			#tempp='http://xendroiders.pythonanywhere.com'
			temp_json["image"]=request.scheme+'://'+request.get_host()+'/media/'+str(o.image)			
			temp_json["description"]=str(o.describ)			
			#temp_json["data_type"]=o.data_type
			response_json["categoryDatas"].append(temp_json)
	except Exception,e:
		print "error@category",e
		response_json["success"]=False
		response_json["message"]="category_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))



# Create your views here.
