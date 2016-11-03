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
		response_body['image']="http://192.168.0.111:8000/static/images/about_us/discount_store_logo.png"

		return JsonResponse(response_body)
