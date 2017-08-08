from __future__ import print_function
import random
from .models import *
from register.models import UserData
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
# Create your views here.
from customs.sms import send_sms


@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        response_json = {}
        try:
            name = str(request.POST.get('name'))
            mobile = str(request.POST.get('mobile'))
            print(name)
            print(mobile)
            otp = random.randint(1000, 9999)
            msg = 'Welcome to Brand Store App. Please use OTP: ' + str(otp)
            send_sms(mobile, msg)
            print('Otp Sent')
            try:
                # otp_list = OtpData.objects.create(mobile=str(mobile))
                # setattr(otp_list, 'otp', int(otp))
                # setattr(otp_list, 'flag', False)
                # otp_list.save()
                # print('old user')
                user_list = UserData.objects.get(mobile=str(mobile))
                setattr(user_list, 'name', name)
                setattr(user_list, 'city', "")
                user_list.save()
                print('User Details Updated')
                try:
                    otp_instance = OtpData.objects.get(mobile=str(mobile))
                    otp_instance.otp = otp
                    otp_instance.save()
                except Exception as e:
                    print (e)
                    OtpData.objects.create(mobile=str(mobile), otp=int(otp))



            except Exception as e:
                OtpData.objects.create(mobile=str(mobile), otp=int(otp))
                UserData.objects.create(
                    name=name,
                    mobile=str(mobile)
                )
                print('User Created')
                print(e)

            response_json['success'] = True
            response_json['message'] = "Otp Sent Successfully"
            pass
        except Exception as e:
            response_json['success'] = False
            response_json['message'] = 'Unable to send otp at this time'
            print(e)
        print(str(response_json))
        return JsonResponse(response_json)


@csrf_exempt
def verify_otp(request):
    response_json = {}
    try:
        mobile = str(request.POST.get("mobile"))
        otp = str(request.POST.get("otp"))
        access_token = 'No Access Token'
        otp_list = OtpData.objects.get(mobile=mobile)
        if otp_list.otp == int(otp):
            setattr(otp_list, 'flag', True)
            access_token = jwt.encode({'mobile': str(mobile)}, '810810', algorithm='HS256')
            otp_list.save()
            response_json['access_token'] = str(access_token)
            print('Access Token Created')
            # json = jwt.decode(str(access_token), '810910', algorithms='HS256')
            user = OtpData.objects.filter(mobile=str(mobile))
            if user.exists():
                for u in user:
                    u.delete()

            response_json['success'] = True
            response_json['message'] = 'Successful'
        else:
            response_json['success'] = False
            response_json['message'] = 'Invalid Otp'
    except Exception as e:
        response_json['success'] = False
        response_json['message'] = 'Invalid Mobile Number'
        print(e)
    print(str(response_json))
    return JsonResponse(response_json)
