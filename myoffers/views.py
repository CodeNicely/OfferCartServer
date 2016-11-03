from django.shortcuts import render
from .models import *
from offer.models import *
from shop.models import *
# Create your views here.
def myoffers(request):
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

			response_json["offer_list"]=[]
			fields=["price","created"]
			fields_offer=["name","image","description","validity"]
			fields_shop=["name","address","image"]
			for o in offer_bought_data.objects.filter(user_id=str(json['mobile'])):
				temp_json={}
				for f in fields:
					print "f=",f
					temp_json[f]=str(getattr(o,str(f)))

				offer_row=offer_data.objects.get(offer_id=o.offer_id)
				for p in fields_offer:
					temp_json[p]=getattr(offer_row,p)
				temp_json_shop={}
				shop_row=shop_data.objects.get(shop_id=offer_row.shop_id)
				for q in fields_shop:
					temp_json_shop[q]=getattr(shop_row,q)
				temp_json['shop_data']=temp_json_shop
				response_json["offer_list"].append(temp_json)

		except Exception,e:
			response_json["success"]=False
			response_json["message"]="error in my offers"
			print"e@myoffer=", e

		
	else:
		response_json['success']=False
		response_json['message']="not get method"
	print str(response_json)
	return HttpResponse(str(response_json))
