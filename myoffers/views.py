from django.shortcuts import render
from .models import *
from offer.models import *
from shop.models import *
import jwt
from django.http import HttpResponse,JsonResponse

# Create your views here.

def my_offers(request):
	response_json={}
	if request.method=='GET':
		try:
			for x,y in request.GET.items():
				print x,":",y
			access_token=request.GET.get('access_token')
			json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
			print json['mobile']
			response_json["success"]=True
			response_json["message"]='Successful'

			response_json["my_offer_list"]=[]
			for o in offers_bought.objects.filter(mobile=str(json['mobile'])):
				offer_details=offer_data.objects.get(id=o.offer_id)
				my_offer_details={}
				my_offer_details['offer_id']=offer_details.id
				my_offer_details['offer_name']=offer_details.name
				my_offer_details['offer_validity']=offer_details.validity
				my_offer_details['offer_price']=offer_details.price
				shop_details=shop_data.objects.get(id=offer_details.shop_id)
				my_offer_details['shop_name']=shop_details.name
				my_offer_details['shop_address']=shop_details.address
				response_json["my_offer_list"].append(my_offer_details)

		except Exception,e:
			response_json["success"]=False
			response_json["message"]="error in my offers"
			print"e@myoffer=", e

		
	else:
		response_json['success']=False
		response_json['message']="Get Out of here!"
	print str(response_json)
	return JsonResponse(response_json)


# def myoffers(request):
# 	response_json={}
# 	if request.method=='GET':
# 		try:
# 			for x,y in request.GET.items():
# 				print x,":",y
# 			access_token=request.GET.get('access_token')
# 			json=jwt.decode(str(access_token), '999123', algorithms=['HS256'])
# 			print json['mobile']
# 			response_json["success"]=True
# 			response_json["message"]='Successful'

# 			response_json["offer_list"]=[]
# 			fields=["price","created","transaction_id"]
# 			fields_offer=["name","image","description","validity"]
# 			fields_shop=["name","address","image"]
# 			for o in offer_bought.objects.filter(user_id=str(json['mobile'])):
# 				temp_json={}
# 				for f in fields:
# 					print "f=",f
# 					temp_json[f]=str(getattr(o,str(f)))

# 				offer_row=offer_data.objects.get(offer_id=o.offer_id)
# 				for p in fields_offer:
# 					temp_json[p]=getattr(offer_row,p)
# 				temp_json_shop={}
# 				shop_row=shop_data.objects.get(shop_id=offer_row.shop_id)
# 				for q in fields_shop:
# 					temp_json_shop[q]=getattr(shop_row,q)
# 				temp_json['shop_data']=temp_json_shop
# 				response_json["offer_list"].append(temp_json)

# 		except Exception,e:
# 			response_json["success"]=False
# 			response_json["message"]="error in my offers"
# 			print"e@myoffer=", e

		
# 	else:
# 		response_json['success']=False
# 		response_json['message']="not get method"
# 	print str(response_json)
# 	return HttpResponse(str(response_json))