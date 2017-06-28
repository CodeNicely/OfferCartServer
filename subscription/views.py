from __future__ import print_function
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
                        "subscription_description": subscription.subscription_description,
                        "subscription_price": subscription.subscription_price,
                        "subscription_period": subscription.subscription_days,
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


# @csrf_exempt
# def add_subscription(request):
#     response = {}
#     if request.method == 'GET':
#         try:
#             for x, y in request.GET.items():
#                 print(x, ":", y)
#             shop_access_token = str(request.GET.get("shop_access_token"))
#             subscription_id = int(request.GET.get("subscription_id"))

#             print("Shop Access Token : " + shop_access_token)

#             json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
#             shop_mobile = str(json['mobile'])

#             shop_instance = ShopData.objects.get(mobile=shop_mobile)
#             subscription_instance = SubscriptionData.objects.get(id=subscription_id)

#             # key = 't1iq81Kx'
#             # merchant_id = '5669435'
#             # merchant_salt = 'RZHvaXdcuR'

#             #Test Credentials
#             key='OPnqOtgp'
#             merchant_id='4943078'
#             merchant_salt='uIBWzo2PAt'

#             try:
#                 shop_subscription_instance = ShopSubscriptionData.objects.create(
#                     shop_id=shop_instance,
#                     subscription_id=subscription_instance)

#                 name = shop_instance.name
#                 email = 'shops@brandstore.in'
#                 transaction_id = str(shop_subscription_instance.id) + str(shop_instance.name) + str(
#                     subscription_instance.id)

#                 shop_subscription_instance.transaction_id = transaction_id
#                 shop_subscription_instance.save()

#                 amount = subscription_instance.subscription_price
#                 product_name = subscription_instance.subscription_title

#                 server_hash_to_encode = key + '|' + transaction_id + '|' + str(
#                     amount) + '|' + product_name + '|' + name + '|' + email + '||||||' + merchant_salt

#                 print(server_hash_to_encode)
#                 hash_encoded = hashlib.sha512(server_hash_to_encode).hexdigest().lower()
#                 print(hash_encoded)

#                 response['name'] = name
#                 response['mobile'] = shop_mobile
#                 response['email'] = email
#                 response['product_name'] = product_name
#                 response['amount'] = amount
#                 response['key'] = key
#                 response['merchant_id'] = merchant_id
#                 response['transaction_id'] = transaction_id
#                 response['server_hash'] = hash_encoded
#                 response['success'] = True
#                 response['message'] = "Successful"

#             except Exception as e:
#                 print(str(e))
#                 response['success'] = False
#                 response['message'] = "Something went wrong " + str(e)
#         except Exception as e:
#             response['success'] = False
#             response['message'] = "Something went wrong " + str(e)
#     elif request.method == 'POST':
#         try:
#             shop_access_token = request.POST.get("shop_access_token")
#             transaction_id = request.POST.get("transaction_id")
#             success = request.POST.get("success")

#             json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
#             shop_mobile = str(json['mobile'])

#             shop_instance = ShopData.objects.get(mobile=shop_mobile)
#             shop_subscription_instance = ShopSubscriptionData.objects.get(shop_id=shop_instance, id=transaction_id)
#             subscription_data = SubscriptionData.objects.get(transaction_id=transaction_id)

#             try:
#                 if success:
#                     shop_subscription_instance.payment_status = True
#                     shop_subscription_instance.subscription_expiry_date = shop_instance.subscription_expiry_date + timedelta(
#                         days=subscription_data.subscription_days)
#                     shop_subscription_instance.save()
#                 else:
#                     shop_subscription_instance.payment_status = False
#                 shop_subscription_instance.save()
#                 response['success'] = True
#                 response['message'] = "Successful"

#             except Exception as e:
#                 print(str(e))
#                 response['success'] = False
#                 response['message'] = "Something went wrong " + str(e)
#         except Exception as e:
#             print(str(e))
#             response['success'] = False
#             response['message'] = "Something went wrong " + str(e)

#     else:
#         response['success'] = False
#         response['message'] = "Illegal Request"
#     print(response)
#     return JsonResponse(response)


import Checksum


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

            # Test Credentials
            # key = 'OPnqOtgp'

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

                amount = str(subscription_instance.subscription_price)
                product_name = subscription_instance.subscription_title

                merchant_id = 'INVERN85845033309930'
                merchant_key = '3rqQdtKyC%EoeH&f'
                industry_type_id = 'Retail'
                channel_id = 'WAP'
                website = 'http://www.paytm.com'
                callback_url = 'https://pguat.paytm.com/paytmchecksum/paytmCallback.jsp'
                respons_dict = {}

                respons_dict['MID'] = str(merchant_id)  # Provided by Paytm
                respons_dict['ORDER_ID'] = str(transaction_id)  # unique OrderId for every request
                respons_dict['CUST_ID'] = str(shop_mobile)  # unique customer identifier



                respons_dict['INDUSTRY_TYPE_ID'] = industry_type_id  # Provided by Paytm
                respons_dict['CHANNEL_ID'] = channel_id  # Provided by Paytm
                respons_dict['TXN_AMOUNT'] = str(amount)  # transaction amount
                respons_dict['WEBSITE'] = website  # Provided by Paytm
                respons_dict['EMAIL'] = str(email)  # customer email id
                respons_dict['MOBILE_NO'] = str(shop_mobile)  # customer 10 digit mobile no.
                respons_dict['CALLBACK_URL'] = callback_url  # Provided by Paytm

                checksum = Checksum.generate_checksum(respons_dict, merchant_key)

                # paramarr = {};

                # paramarr = respons_dict;

                # response['CHECKSUMHASH'] = checksum

                # server_hash_to_encode = key + '|' + transaction_id + '|' + str(
                #     amount) + '|' + product_name + '|' + name + '|' + email + '||||||' + merchant_salt

                # print(server_hash_to_encode)
                # hash_encoded = hashlib.sha512(server_hash_to_encode).hexdigest().lower()
                # print(hash_encoded)

                response["merchant_id"] = merchant_id
                response["order_id"] = transaction_id
                response["customer_id"] = shop_mobile
                response["industry_type_id"] = industry_type_id
                response["channel_id"] = channel_id
                response["amount"] = amount
                response["website"] = website
                response["email"] = email
                response["mobile"] = shop_mobile
                response["callback_url"] = callback_url
                response["checksum_hash"] = checksum
                # response['name'] = name

                response["success"] = True
                response["message"] = "Successful"

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
            print ("error1")
            transaction_id = request.POST.get("transaction_id")
            print ("error1")
            success = request.POST.get("success")
            print ("error1")

            json = jwt.decode(str(shop_access_token), '810810', algorithms=['HS256'])
            print ("error1")
            shop_mobile = str(json['mobile'])
            print ("error1")
            shop_instance = ShopData.objects.get(mobile=shop_mobile)
            print ("error2")
            shop_subscription_instance = ShopSubscriptionData.objects.get(shop_id=shop_instance, id=transaction_id)
            print ("error3")
            subscription_data = SubscriptionData.objects.get(transaction_id=transaction_id)
            print ("error4")

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
                print("error5")
                response['success'] = False
                response['message'] = "Something went wrong " + str(e)
        except Exception as e:
            print(str(e))
            print("error6")
            response['success'] = False
            response['message'] = "Something went wrong " + str(e)

    else:
        response['success'] = False
        response['message'] = "Illegal Request"
    print(response)
    return JsonResponse(response)
