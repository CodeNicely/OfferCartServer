from __future__ import print_function
from __future__ import print_function

import json
import os
import random

import jwt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from city.models import UserCityData, StateData
from customs.sms import send_sms
from .models import *
from math import sin, cos, asin, sqrt, radians
import numpy as np
import datetime


@csrf_exempt
def shop(request):
    response_json = {}
    if request.method == 'GET':
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            access_token = request.GET.get('access_token')
            json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
            user_id = str(json['mobile'])
            category_id = str(request.GET.get("category_id"))
            latitude = request.GET.get('latitude')
            longitude = request.GET.get('longitude')
            city_id = UserCityData.objects.get(user_id=user_id).city_id

            # print "City id",city_id

            response_json["success"] = True
            response_json["message"] = 'Successful'
            response_json["shopDatas"] = []
            fields = ["name", "address"]

            for o in ShopData.objects.filter(city_id=city_id, category_id=category_id):
                # today_date = datetime.datetime.today().date()
                today_date = datetime.date.today()
                if (o.subscription_expiry_date.date() - today_date).days > 0 and o.verified:
                    distance = get_distance(np.float32(latitude), np.float32(longitude),
                                            np.float32(o.latitude), np.float32(o.longitude))
                    temp_json = {}
                    for f in fields:
                        print("f=", f)
                        temp_json[f] = str(getattr(o, str(f)))
                    temp_json['distance'] = distance
                    print("Distance=", distance)
                    temp_json['shop_id'] = int(o.id)
                    temp_json['category_id'] = int(o.category_id.id)
                    temp_json['city_id'] = int(o.city_id.id)
                    temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/shop/' + str(o.image)
                    response_json["shopDatas"].append(temp_json)
            response_json["shopDatas"] = sorted(response_json["shopDatas"], key=lambda x: x['distance'], reverse=False)
        except Exception as e:
            response_json = {"success": False, "message": "shop_data not found"}
            print("e@shop=", e)
        print(str(response_json))
    else:
        response_json['success'] = False
        response_json['message'] = "Invalid request"

    return HttpResponse(str(response_json))


# Create your views here.
# noinspection PyUnreachableCode

# From here the methods are for Shop Admin module

@csrf_exempt
def state_category(request):
    response_json = {}
    if request.method == 'GET':
        try:
            response_json['state_list'] = []
            for i in StateData.objects.order_by('name'):
                temp_json = {}
                temp_json['id'] = int(i.id)
                temp_json['name'] = str(i.name)
                response_json['state_list'].append(temp_json)
            response_json['category_list'] = []
            for i in CategoryData.objects.order_by('name'):
                temp_json = {}
                temp_json['id'] = int(i.id)
                temp_json['name'] = str(i.name)
                response_json['category_list'].append(temp_json)
            response_json['success'] = True
            response_json['message'] = "Succesful"
            # response_json['city_list'] = [(i.id, i.name) for i in CityData.objects.all()]
            # response_json['category_list'] = [(i.id, i.name) for i in CategoryData.objects.all()]
            print(response_json)
        except Exception as e:
            response_json = {'success': True, 'message': "city/category not found"}
            print(e)
    else:
        response_json['success'] = False
        response_json['message'] = "Invalid request"
    return HttpResponse(str(json.dumps(response_json)))


@csrf_exempt
def create_shop(request):
    response_json = {}
    if request.method == 'POST':
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            name = str(request.POST.get('name'))
            mobile = str(request.POST.get('mobile'))
            password = str(request.POST.get('password'))
            description = str(request.POST.get('description'))
            address = str(request.POST.get('address'))
            category = str(request.POST.get('category'))
            city = str(request.POST.get('city'))
            latitude = str(request.POST.get('latitude'))
            longitude = str(request.POST.get('longitude'))

            try:
                image = request.FILES.get('image').name
                folder = 'media/' + 'shop/'
                full_filename = os.path.join(folder, image)
                print("full name", full_filename)
                # fout = open(folder+image, 'wb+')
                print("image=", image)
                fout = open(folder + image, 'w')
                file_content = request.FILES.get('image').read()
                # for chunk in file_content.chunks():
                fout.write(file_content)
                fout.close()
            except Exception as e:
                image = 'image'
                print(e)

            # print("Hashed password is:", make_password(password))
            print(name, mobile, type(image), image)

            try:
                category_instance = CategoryData.objects.get(name=category)
                city_instance = CityData.objects.get(name=city)

                if ShopData.objects.filter(mobile=str(mobile)).count() > 0:
                    shop_instance = ShopData.objects.get(mobile=mobile)
                    if shop_instance.otp_verified:
                        print("Shop already exist")
                        response_json['success'] = False
                        response_json[
                            'message'] = "Mobile Number already Registered.\nPlease try again with a different mobile number"
                    else:
                        shop_instance.name = name
                        shop_instance.mobile = mobile
                        shop_instance.password = password
                        shop_instance.description = description
                        shop_instance.address = address
                        shop_instance.latitude = latitude
                        shop_instance.longitude = longitude
                        shop_instance.category_id = category_instance
                        shop_instance.city_id = city_instance
                        shop_instance.image = image
                        shop_instance.save()

                        otp = random.randint(1000, 9999)
                        msg = 'Welcome to Brand Store. Your One Time Password is ' + str(otp)
                        send_sms(mobile, msg)

                        otp_list = ShopOtpData.objects.get(shop_id=shop_instance)
                        setattr(otp_list, 'otp', int(otp))
                        setattr(otp_list, 'flag', False)
                        otp_list.save()

                        print("Shop Registering again without otp verification")
                        response_json['success'] = True
                        response_json['message'] = "Otp Sent Successfully"


                else:
                    print("New shop")

                    shop_instance = ShopData.objects.create(
                        name=name,
                        mobile=str(mobile),
                        password=str(password),
                        description=description,
                        address=address,
                        latitude=latitude,
                        longitude=longitude,
                        category_id=category_instance,
                        city_id=city_instance,
                        image=image
                    )

                    print('User Created')

                    otp = random.randint(1000, 9999)
                    msg = 'Welcome to Brand Store. You One Time Password is ' + str(otp)
                    send_sms(mobile, msg)

                    try:
                        otp_list = ShopOtpData.objects.get(shop_id=shop_instance)

                        if otp_list.count() == 1:
                            setattr(otp_list, 'otp', int(otp))
                            setattr(otp_list, 'flag', False)
                            otp_list.save()
                            print('old user')
                        else:
                            ShopOtpData.objects.create(shop_id=shop_instance, otp=int(otp))

                    except Exception as e:
                        ShopOtpData.objects.create(shop_id=shop_instance, otp=int(otp))
                        print("Otp data does not exist, Creating it")

                    response_json['success'] = True
                    response_json['message'] = "Otp Sent Successfully"

            except Exception as e:
                response_json['success'] = False
                response_json['message'] = 'Unable to send otp at this time'
                print(e)
            print(str(response_json))
        except Exception as e:
            response_json['success'] = False
            response_json['message'] = 'Something went wrong'
            print(e)
    else:
        response_json['success'] = False
        response_json['message'] = "Invalid request"
    return JsonResponse(response_json)


@csrf_exempt
def verify_shop_otp(request):
    response = {}
    if request.method == 'POST':
        try:

            mobile = str(request.POST.get('mobile'))
            otp = str(request.POST.get('otp'))
            print("Mobile" + str(mobile))
            print("otp:" + str(otp))
            shop_instance = ShopData.objects.get(mobile=str(mobile))
            shop_otp_instance = ShopOtpData.objects.get(shop_id=shop_instance)

            access_token = jwt.encode({'mobile': str(mobile)}, '810810', algorithm='HS256')

            print("Required" + str(shop_otp_instance.otp))

            if int(shop_otp_instance.otp) == int(otp):
                shop_instance.otp_verified = True
                shop_instance.save()
                response['success'] = True
                response['message'] = "Otp verified successfully"
                response['shop_access_token'] = str(access_token)

            else:
                response['success'] = False
                response['message'] = "Otp doesn't match"
        except Exception as e:
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
            print(e)
    else:
        response['success'] = False
        response['message'] = "Invalid request"
    print(response)
    return JsonResponse(response)


@csrf_exempt
def verify_shop_login(request):
    response = {}
    if request.method == 'POST':
        try:
            mobile = str(request.POST.get('mobile'))
            password = str(request.POST.get('password'))
            access_token = jwt.encode({'mobile': str(mobile)}, '810810', algorithm='HS256')
            if ShopData.objects.filter(mobile=mobile, password=password).count() == 1:
                shop_instance = ShopData.objects.get(mobile=mobile, password=password)
                if shop_instance.otp_verified:
                    response['success'] = True
                    response['message'] = "Successful"
                    response['shop_access_token'] = str(access_token)
                else:
                    response['success'] = False
                    response['message'] = "Invalid mobile or password"
            else:
                response['success'] = False
                response['message'] = "Invalid mobile or password"

        except Exception as e:
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
    else:
        response['success'] = False
        response['message'] = "Invalid request type"
    # response_data = json.dumps(response)
    print(response)
    return JsonResponse(response)


@csrf_exempt
def my_shop_profile(request):
    response = {}
    if request.method == 'GET':
        try:
            shop_access_token = str(request.GET.get('shop_access_token'))
            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            shop_mobile = str(json['mobile'])
            shop_instance = ShopData.objects.get(mobile=shop_mobile)

            response['name'] = shop_instance.name
            response['mobile'] = shop_instance.mobile
            response['description'] = shop_instance.description
            response['address'] = shop_instance.address
            response['category'] = str(shop_instance.category_id)
            response['city'] = str(shop_instance.city_id)
            response['image'] = request.scheme + '://' + request.get_host() + '/media/shop/' + str(shop_instance.image)
            response['success'] = True
            response['message'] = "Successful"

        except Exception as e:
            response['success'] = False
            response['message'] = "Something went wrong" + str(e)
            print(e)
    else:
        response['success'] = False
        response['message'] = "Illegal request"
    # response_json=json.dumps(response)
    print(response)
    return JsonResponse(response)


@csrf_exempt
def edit_shop_profile(request):
    response = {}
    if request.method == 'POST':
        try:
            for x, y in request.POST.items():
                print(x, ":", y)

            shop_access_token = str(request.POST.get('shop_access_token'))
            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            shop_mobile = str(json['mobile'])
            print("Shop mobile:" + str(shop_mobile))
            name = str(request.POST.get('name'))
            description = str(request.POST.get('description'))
            address = str(request.POST.get('address'))
            category = str(request.POST.get('category'))
            city = str(request.POST.get('city'))
            latitude = str(request.POST.get('latitude'))
            longitude = str(request.POST.get('longitude'))
            shop_instance = ShopData.objects.get(mobile=shop_mobile)

            try:
                image = request.FILES.get('image').name
                folder = 'media/' + 'shop/'
                full_filename = os.path.join(folder, image)
                print("full name", full_filename)
                # fout = open(folder+image, 'wb+')
                print("image=", image)
                shop_instance.image = image
                fout = open(folder + image, 'w')
                file_content = request.FILES.get('image').read()
                # for chunk in file_content.chunks():
                fout.write(file_content)
                fout.close()
            except Exception as e:
                image = 'image'
                print(e)

            shop_instance.name = name
            shop_instance.description = description
            shop_instance.address = address
            shop_instance.latitude = latitude
            shop_instance.longitude = longitude
            shop_instance.category_id = CategoryData.objects.get(name=category)
            shop_instance.city_id = CityData.objects.get(name=city)
            if image != None:
                print("Image not null-------")
            shop_instance.save()
            response['success'] = True
            response['message'] = "Successful"

        except Exception as e:
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
            print(e)
    else:
        response['success'] = False
        response['message'] = "Illegal request"

    print(response)
    return JsonResponse(response)


@csrf_exempt
def change_password(request):
    response = {}
    if request.method == 'POST':
        try:
            shop_access_token = str(request.POST.get('shop_access_token'))
            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            shop_mobile = str(json['mobile'])

            old_password = str(request.POST.get('old_password'))
            new_password = str(request.POST.get('new_password'))

            try:
                shop_instance = ShopData.objects.get(mobile=shop_mobile, password=old_password)
                shop_instance.password = new_password
                shop_instance.save()
                response['success'] = True
                response['message'] = "Sucessfully Changed"
            except Exception as e:
                print(str(e))
                response['success'] = False
                response['message'] = "Incorrect Old Password"

        except Exception as e:
            print(str(e))
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
    else:
        response['success'] = False
        response['message'] = "Illegal request"
    print(response)
    return JsonResponse(response)


@csrf_exempt
def forgot_password(request):
    response_json = {}
    if request.method == 'POST':
        try:
            mobile = str(request.POST.get('mobile'))

            otp = random.randint(1000, 9999)
            msg = 'Welcome to Discount Store. You One Time Password is ' + str(otp)
            send_sms(mobile, msg)

            try:
                shop_instance = ShopData.objects.get(mobile=str(mobile))
                shop_otp_instance = ShopOtpData.objects.get(shop_id=shop_instance)
                print(shop_otp_instance.otp)
                setattr(shop_otp_instance, 'otp', int(otp))
                print(shop_otp_instance.otp)
                shop_otp_instance.save()
                print('old user')

            except Exception as e:
                ShopOtpData.objects.create(shop_id=shop_instance, otp=int(otp))
                print("Otp data does not exist, Creating it")
                print(e)
            response_json['success'] = True
            response_json['message'] = "Otp Sent Successfully"
        except Exception as e:
            response_json['success'] = False
            response_json['message'] = 'No shop exists with mobile number ' + str(mobile)
            print(e)
        print(str(response_json))
    else:
        response_json['success'] = False
        response_json['message'] = "Invalid request"
    return JsonResponse(response_json)


@csrf_exempt
def forgot_change_password(request):
    response = {}
    if request.method == 'POST':
        try:
            shop_access_token = str(request.POST.get('shop_access_token'))
            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            shop_mobile = str(json['mobile'])
            new_password = str(request.POST.get('new_password'))

            try:
                shop_instance = ShopData.objects.get(mobile=shop_mobile)
                shop_instance.password = new_password
                shop_instance.save()
                response['success'] = True
                response['message'] = "Sucessfully Changed"
            except Exception as e:
                print(str(e))
                response['success'] = False
                response['message'] = "Something Went Wrong" + str(e)

        except Exception as e:
            print(str(e))
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
    else:
        response['success'] = False
        response['message'] = "Illegal request"
    print(response)
    return JsonResponse(response)


def get_distance(lat1, lon1, lat2, lon2):
    try:
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        # print "Km is ", km
        return km
    except Exception as e:
        print(e)
        return 100.0


# ===============================================================================================


def delete_shop_data(request):
    return 0
    # for x in cities:
    #     try:
    #         CityData.objects.get(name=x['name'])
    #     except Exception as e:
    #         shop_instance= StateData.objects.get(name= x['state'])
    #         CityData.objects.create(
    #             name= x['name'],
    #             state_name= shop_instance
    #         )
    #
