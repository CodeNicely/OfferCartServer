from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def contact_us(request):
	if request.method=='GET':
		response_body={}
		response_body['success']=True
		response_body['message']="Successful"
		response_body['email']="codenicely@gmail.com"
		response_body['mobile']="+91 8109109457"
		response_body['address']="Indore , Bhopal"
		response_body['facebook']="DiscountStore"
		#temp_json["image"]=request.scheme+'://'+request.get_host()+'/media/'+str(o.image)
		response_body['image']=request.scheme+'://'+request.get_host()+"/media/about_us/discount_store_logo.png"

		print response_body
		return JsonResponse(response_body)
