from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import jwt
from django.http import JsonResponse

from offer.models import *
from shop.models import *


# Create your views here.

def my_offers(request):
    response_json = {}
    if request.method == 'GET':
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            access_token = request.GET.get('access_token')
            json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
            print(json['mobile'])
            response_json["success"] = True
            response_json["message"] = 'Successful'

            response_json["my_offer_list"] = []
            for o in OfferBoughtData.objects.filter(mobile=str(json['mobile'])):
                offer_details = OfferData.objects.get(id=o.offer_id)
                my_offer_details = {}
                my_offer_details['offer_id'] = offer_details.id
                my_offer_details['offer_name'] = offer_details.name
                my_offer_details['offer_validity'] = offer_details.validity
                my_offer_details['offer_description'] = offer_details.description
                my_offer_details['offer_image'] = request.scheme + '://' + request.get_host() + '/media/' + str(
                    offer_details.image)
                shop_details = ShopData.objects.get(name=offer_details.shop_id)
                my_offer_details['shop_name'] = shop_details.name
                my_offer_details['shop_address'] = shop_details.address
                my_offer_details['shop_distance'] = shop_details.distance
                response_json["my_offer_list"].append(my_offer_details)
        except Exception as e:
            response_json["success"] = False
            response_json["message"] = "error in my offers"
            print("e@myoffer=", e)
    else:
        response_json['success'] = False
        response_json['message'] = "Get Out of here!"
    print(str(response_json))
    return JsonResponse(response_json)
