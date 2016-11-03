from django.shortcuts import render
from myoffer.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from register.models import user_data
from offer.models import offer_data
from myoffers.models import offer_bought_data
from random import randint

@csrf_exempt
def buyoffers(request):
	response_json={}
	if request.method=='POST':
		try:
			for x,y in request.POST.items():
				print x,":",y
			access_token=request.POST.get('access_token')
			offer_id=request.POST.get('offer_id')
			json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
			print json['mobile']
			mobile=json['mobile']
			response_json["success"]=True
			response_json["message"]='Successful'
			user=user_data.objects.get(mobile=str(json['mobile']))
			wallet=user.wallet
			offer=offer_data.objects.get(offer_id=int(offer_id))
			price=offer.price
			if(wallet<price):
				response_json["success"]=False
				response_json["message"]='Transaction Unsuccessful, wallet does not have that amount of money23457"
			else:
				transaction_id=str(randint(11,99))+str(mobile)[randint(0,5),randint(5,9)]+str(randint(11,99))
				user_id=str(mobile)
				offer_bought_data.objects.create(user_id=user_id,transaction_id=transaction_id,price=price,offer_id=offer_id)
				user.wallet=wallet-price
				user.save()
				response_json["transaction_id"]=transaction_id
				response_json["offer_name"]=offer.name
				response_json["price"]=offer.price
		except Exception,e:
			response_json["success"]=False
			response_json["message"]="error in buyoffers"
			print"e@buyoffer=", e

		
	else:
		response_json['success']=False
		response_json['message']="not POST method"
	print str(response_json)
	return HttpResponse(str(response_json))
