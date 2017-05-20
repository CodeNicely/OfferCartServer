from __future__ import print_function

import hashlib
from datetime import timedelta

import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.
@csrf_exempt
def request_subscription(request):
    response = {}
    if request.method == 'GET':
        try:
            subscription_list = []
            for subscription in SubscriptionData.objects.all():
                subscription_list.append(
                    {
                        "subscription_id": subscription.id,
                        "subscription_title": subscription.subscription_title,
                        "subscription_price": subscription.subscription_price,
                    }
                )
            response['success'] = True
            response['message'] = "Successful"
            response['subscription_list'] = subscription_list

        except Exception as e:
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
    else:
        response['success'] = False
        response['message'] = "Illegal Request"
    print(response)
    return JsonResponse(response)


@csrf_exempt
def add_subscription(request):
    response = {}
    if request.method == 'GET':
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            shop_access_token = str(request.GET.get("shop_access_token"))
            subscription_id = int(request.GET.get("subscription_id"))

            print("Shop Access Token : " + shop_access_token)

            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            shop_mobile = str(json['mobile'])

            shop_instance = ShopData.objects.get(mobile=shop_mobile)
            subscription_instance = SubscriptionData.objects.get(id=subscription_id)

            # key = 't1iq81Kx'
            # merchant_id = '5669435'
            # merchant_salt = 'RZHvaXdcuR'

            #Test Credentials
            key='OPnqOtgp'
            merchant_id='4943078'
            merchant_salt='uIBWzo2PAt'

            try:
                shop_subscription_instance = ShopSubscriptionData.objects.create(
                    shop_id=shop_instance,
                    subscription_id=subscription_instance)

                name = shop_instance.name
                email = 'shops@brandstore.in'
                transaction_id = str(shop_subscription_instance.id) + str(shop_instance.name) + str(
                    subscription_instance.id)

                shop_subscription_instance.transaction_id = transaction_id
                shop_subscription_instance.save()

                amount = subscription_instance.subscription_price
                product_name = subscription_instance.subscription_title

                server_hash_to_encode = key + '|' + transaction_id + '|' + str(
                    amount) + '|' + product_name + '|' + name + '|' + email + '||||||' + merchant_salt

                print(server_hash_to_encode)
                hash_encoded = hashlib.sha512(server_hash_to_encode).hexdigest().lower()
                print(hash_encoded)

                response['name'] = name
                response['mobile'] = shop_mobile
                response['email'] = email
                response['product_name'] = product_name
                response['amount'] = amount
                response['key'] = key
                response['merchant_id'] = merchant_id
                response['transaction_id'] = transaction_id
                response['server_hash'] = hash_encoded
                response['success'] = True
                response['message'] = "Successful"

            except Exception as e:
                print(str(e))
                response['success'] = False
                response['message'] = "Something went wrong " + str(e)
        except Exception as e:
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)
    elif request.method == 'POST':
        try:
            shop_access_token = request.POST.get("shop_access_token")
            transaction_id = request.POST.get("transaction_id")
            success = request.POST.get("success")

            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            shop_mobile = str(json['mobile'])

            shop_instance = ShopData.objects.get(mobile=shop_mobile)
            shop_subscription_instance = ShopSubscriptionData.objects.get(shop_id=shop_instance, id=transaction_id)
            subscription_data = SubscriptionData.objects.get(transaction_id=transaction_id)

            try:
                if success:
                    shop_subscription_instance.payment_status = True
                    shop_subscription_instance.subscription_expiry_date = shop_instance.subscription_expiry_date + timedelta(
                        days=subscription_data.subscription_days)
                    shop_subscription_instance.save()
                else:
                    shop_subscription_instance.payment_status = False
                shop_subscription_instance.save()
                response['success'] = True
                response['message'] = "Successful"

            except Exception as e:
                print(str(e))
                response['success'] = False
                response['message'] = "Something went wrong " + str(e)
        except Exception as e:
            print(str(e))
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)

    else:
        response['success'] = False
        response['message'] = "Illegal Request"
    print(response)
    return JsonResponse(response)
