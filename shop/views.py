import jwt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from city.models import UserCityData
from .models import *


@csrf_exempt
def shop(request):
    response_json = {}
    if request.method == 'GET':
        try:
            for x, y in request.GET.items():
                print x, ":", y
            access_token = request.GET.get('access_token')
            json = jwt.decode(str(access_token), '999123', algorithms=['HS256'])
            user_id = str(json['mobile'])
            category_id = str(request.GET.get("category_id"))

            city_id = UserCityData.objects.get(user_id=user_id).city_id

            # print "City id",city_id

            response_json["success"] = True
            response_json["message"] = 'Successful'
            response_json["shopDatas"] = []
            fields = ["name", "address"]
            for o in ShopData.objects.filter(city_id=city_id, category_id=category_id):

                temp_json = {}
                for f in fields:
                    print "f=", f
                    temp_json[f] = str(getattr(o, str(f)))
                temp_json['shop_id'] = int(o.id)
                temp_json['category_id'] = int(o.category_id.id)
                temp_json['city_id'] = int(o.city_id.id)

                temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/' + str(o.image)
                response_json["shopDatas"].append(temp_json)

        except Exception, e:
            response_json = {"success": False, "message": "shop_data not found"}

            print"e@shop=", e

        print str(response_json)
    else:
        response_json['success'] = False
        response_json['message'] = "Invalid request"

    return HttpResponse(str(response_json))

# Create your views here.
