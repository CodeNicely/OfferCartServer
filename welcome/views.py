from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
from .models import *
# Create your views here.
def welcome(request):
	try:
		response_json={}
		response_json["success"]=True
		response_json["slider_data"]=[]
		for o in  image_data.objects.all():
			temp_json={}
			temp_json["image_id"]=o.image_id
			temp_json["image_url"]=str(o.image_url)
			temp_json["message"]=str(o.message)
			response_json['slider_data'].append(temp_json)
	except:
		response_json["success"]=False
		response_json["message"]='url not sent'
		
	print str(response_json)
	return HttpResponse(str(response_json))

# def run_url(request):
# 	#try:
# 	url1='http://127.0.0.1:8000/url/'
# 	result=requests.get(url1)

# 	#print str(response_json)

# 	return HttpResponse(result)

