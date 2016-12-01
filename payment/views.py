from django.shortcuts import render

from register.models import user_data
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
# Create your views here.


@csrf_exempt
def payment_hash(request):
	if(request.method=='POST'):		
		access_token=request.GET.get('access_token')
		json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
		
		user_details=user_data.objects.get(mobile=str(json['mobile']))

		amount=double(request.POST.get("amount"))
		name=str(user_details.name)
		email=str(user_details.email)
		mobile=str(user_details.mobile)
		product_name='Wallet'
		key='t1iq81Kx'
		merchant_id='5669435'
		merchant_salt='RZHvaXdcuR'
		transaction_id=mobile+str(random.randint(100,999))
		response_json={}

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
			
			hash_encoded=hashlib.sha512(server_hash_to_encode).hexdigest().lower()
			
			response_json['server_hash']=str(hash_encoded)
			response_json['success']=True
			response_json['message']='Successfully Sent Hash'
		except Exception,e:

			response_json['success']=False
			response_json['message']=str(e)

			print e
		return JsonResponse(response_json)

	else:
		response_json['success']=False
		response_json['message']="This api is not made for GET Requests"

		return JsonResponse(response_json)
