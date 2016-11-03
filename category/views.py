from django.shortcuts import render
from .models import  *
from django.http import HttpResponse
import requests

def category(request):
	try:
		response_json={}
		response_json["success"]=True
		response_json['message']="Successful"
		response_json["categoryDatas"]=[]
		for o in category_data.objects.all():
			temp_json={}
			temp_json["id"]=o.category_id
			temp_json["name"]=str(o.category_name)
#			temp_json["image"]='https://www.aldi.com.au/typo3temp/pics/ALC6158_KVB_Groceries_1896x720_582e750e6c.jpg'#str(o.image)
			temp_json["image"]='http://xendroiders.pythonanywhere.com'+str(o.image)[33:]			
			temp_json["data_type"]=o.data_type
			response_json["categoryDatas"].append(temp_json)
	except:
		response_json["success"]=False
		response_json["message"]="category_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))



# Create your views here.
