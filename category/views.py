from __future__ import print_function
from __future__ import print_function

import jwt
from django.http import HttpResponse

from city.models import UserCityData, CityData
from register.models import UserData
from shop.models import ShopData
from .models import *


def category(request):
    try:
        access_token = request.GET.get('access_token')
        json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
        mobile = str(json['mobile'])
        user_instance = UserData.objects.get(mobile=mobile)
        user_city_instance = UserCityData.objects.get(user_id=user_instance)
        # city_id = user_city_instance.city_id
        city_instance = CityData.objects.get(name=user_city_instance.city_id)
        response_json = {"categoryDatas": []}
        print('1')
        print(city_instance.name)

        for o in ShopData.objects.filter(city_id=city_instance.id):
            # category_instance = CategoryData.objects.get(id =o.category_id)
            category_instance = o.category_id
            print(category_instance.name)
            try:
                temp_json = {"category_id": int(category_instance.id), "name": str(category_instance.name),
                             "image": request.scheme + '://' + request.get_host() + '/media/' + str(
                                 category_instance.image),
                             "description": str(category_instance.description)}
                if temp_json in response_json["categoryDatas"]:
                    pass
                else:
                    response_json["categoryDatas"].append(temp_json)
            except Exception as e:
                print(e)

        response_json['message'] = "Successful"
        response_json['success'] = True
    except Exception as e:
        print("error@category", e)
        response_json["success"] = False
        response_json["message"] = "category_data not found"

    print(str(response_json))
    return HttpResponse(str(response_json))

# Create your views here.

#     response_json = {"categoryDatas": []}
#     for o in CategoryData.objects.all():
#         temp_json = {"category_id": int(o.id), "name": str(o.name),
#                      "image": request.scheme + '://' + request.get_host() + '/media/' + str(o.image),
#                      "description": str(o.description)}
#         response_json["categoryDatas"].append(temp_json)
#     response_json['message'] = "Successful"
#     response_json['success'] = True
# except Exception as e:
#     print("error@category", e)
#     response_json["success"] = False
#     response_json["message"] = "category_data not found"
#
# print(str(response_json))
# return HttpResponse(str(response_json))
