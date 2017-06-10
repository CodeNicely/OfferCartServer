from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *


@csrf_exempt
def request_states(request):
    if request.method == "GET":
        try:
            response_json = {"success": True, "message": "Succesful", "state_data": []}
            print("debugged")
            for o in StateData.objects.order_by('name'):
                temp_json = {}
                print(o.name)
                temp_json["state_id"] = o.id
                temp_json["state_name"] = str(o.name)
                # temp_json["data_type"]=o.data_type
                response_json["state_data"].append(temp_json)
        except Exception as e:
            print("error@city get", e)
            response_json["success"] = False
            response_json["message"] = "State data not found"
        print(str(response_json))
        return JsonResponse(response_json)


@csrf_exempt
def request_cities(request):
    if request.method == "GET":
        try:
            print("debugged")
            state_id = request.GET.get('state_id')
            response_json = {"success": True, "city_data": []}
            print("debugged")
            print(state_id)
            state = StateData.objects.get(id=state_id)
            print(state_id)
            for o in CityData.objects.filter(state_name=state).order_by('name'):
                temp_json = {}
                print(o.name)
                temp_json["city_id"] = o.id
                temp_json["city_name"] = str(o.name)
                # temp_json["data_type"]=o.data_type
                response_json["city_data"].append(temp_json)
        except Exception as e:
            print("debugged1")
            print("error@city get", e)
            response_json["success"] = False
            response_json["message"] = "city data not found"
        print(str(response_json))
        return JsonResponse(response_json)


@csrf_exempt
def get_city(request):
    if request.method == "POST":
        try:
            response_json = {}
            city_id = request.POST.get('city_id')
            access_token = request.POST.get('access_token')
            json = jwt.decode(str(access_token), '810810', algorithms='HS256')
            mobile = str(json['mobile'])
            user_instance = UserData.objects.get(mobile=mobile)
            city_instance = CityData.objects.get(id=city_id)

            try:
                user_city = UserCityData.objects.get(user_id=mobile)
                user_city.city_id = city_instance
                user_city.save()
            except Exception as e:
                print("Exception", e)
                city_fcm, created = UserCityData.objects.get_or_create(
                    city_id=city_instance,
                    user_id=user_instance
                )
                city_fcm.save()
            response_json['success'] = True
            response_json['message'] = 'Successful'
        except Exception as e:
            response_json["success"] = False
            response_json["message"] = "City data not found"
            print("error@city post", e)
        print(str(response_json))
        return JsonResponse(response_json)


# Create your views here.
@csrf_exempt
def update_fcm(request):
    response_json = {}
    try:
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        access_token = str(request.POST.get('access_token'))
        json = jwt.decode(str(access_token), '810810', algorithms='HS256')
        fcm = str(request.POST.get('fcm'))
        user_id = str(json['mobile'])
        print(fcm)
        if fcm is not None:
            data = UserData.objects.filter(mobile=user_id)
            if data.count() > 0:
                for d in data:
                    setattr(d, 'fcm', fcm)
                    d.save()
                # data.save()
                response_json['success'] = True
                response_json['message'] = "fcm updated successfully"
        else:
            response_json['success'] = False
            response_json['message'] = "fcm is null so it cannot be updated"
    except Exception as e:
        response_json['success'] = False
        response_json['message'] = "fcm cannot be updated"
        print("error@city_fcm  post", e)
    print(str(response_json))
    return JsonResponse(response_json)
