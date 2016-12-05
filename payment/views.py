from django.shortcuts import render
import random

from register.models import user_data
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
import hashlib
from .models import *

# Create your views here.


@csrf_exempt
def request_payment_hash(request):
	if(request.method=='POST'):		
		for x,y in request.POST.items():
				print x,":",y
		access_token=request.POST.get('access_token')
		response_json={}

		json={}

		try:
			json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
			user_details=user_data.objects.get(mobile=str(json['mobile']))
			amount=request.POST.get("amount")
			name=str(user_details.name)
			email=str(user_details.email)
			mobile=str(user_details.mobile)
			product_name='Wallet'
		

			# key='t1iq81Kx'
			# merchant_id='5669435'
			# merchant_salt='RZHvaXdcuR'
		
			key='OPnqOtgp'
			merchant_id='4943078'
			merchant_salt='uIBWzo2PAt'
		


			transaction_id=mobile+str(random.randint(100,999))

			try:		
				response_json['name']=name
				response_json['email']=email
				response_json['mobile']=mobile
				response_json['product_name']=product_name
				response_json['key']=key
				response_json['merchant_id']=merchant_id
				response_json['amount']=amount
				response_json['transaction_id']=transaction_id

				server_hash_to_encode=key+'|'+transaction_id+'|'+amount+'|'+product_name+'|'+name+'|'+email+'|||||||||||'+merchant_salt
				print server_hash_to_encode
				hash_encoded=hashlib.sha512(server_hash_to_encode).hexdigest().lower()
				print hash_encoded
				response_json['server_hash']=hash_encoded
				response_json['success']=True
				response_json['message']='Successfully Sent Hash'
				
				payment_data.objects.create(transaction_id=transaction_id,amount=amount,mobile=mobile)

			except Exception,e:

				response_json['success']=False
				response_json['message']=str(e)

				print e


		except Exception,e:
			response_json['success']=False
			response_json['message']=str(e)
			print e

		return JsonResponse(response_json)
				
		
	else:
		response_json['success']=False
		response_json['message']="This api is not made for GET Requests"

		return JsonResponse(response_json)
