from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def get_otp(request):
	try:
		url='http://api.msg91.com/api/sendhttp.php?authkey=120246AC7mrK6PUjd5794d29c&mobiles='
		mobile=str(request.POST.get("mobile"))
		#mobile=str(9406277619)
		#mobile=str(request.POST.get("9406277619"))
		#phno_data = np.loadtxt('phno.csv', delimiter=' ',dtype='str')
		#n = random.random()
		#for o in phno_data:
		#	url+= str(o)+',
		n=random.randint(1000,9999)
		url+=str(mobile)
		otp=str(n)

		#url+='&message='+'E-Cell team welcomes you. \nVerification code for the app is '+otp
		url+='&message='+' \nVerification code for the app is '+otp
		url+='&sender=mARPIT&route=4'
	
		result = requests.request('GET', url)

		try:
			otp_list=otp_data.objects.get(mobile=mobile)
			setattr(otp_list,'otp',int(otp))
			otp_list.save()
		except:
			otp_data.objects.create(mobile=mobile,otp=int(otp))
	# for o in otp_queries:
	# 	print o.number
	# 	if(number == o.number):
	# 		otp_queries.otp=int(otp)
	# 		otp_data.objects.create(number=number,otp=int(otp))
	#
		response_json={"success":True,"message":"otp sent"}
	except:
		response_json={"success":False,"message":"otp not sent"}
	print str(response_json)
	return HttpResponse(str(response_json))
#@csrf_exempt
@csrf_exempt
def ver_otp(request):
	try:
		name=str(request.POST.get("name"))
		email=str(request.POST.get("email"))
		mobile=str(request.POST.get("mobile"))
		otp=str(request.POST.get("otp"))
		#mobile=str(9406277619)

		print "get method successful"
		print"\n"
		access_token_str=str(random.randint(1000,9999))+mobile+str(random.randint(1000,9999))
		#otp=9137
		otp_list=otp_data.objects.get(mobile=mobile)
		if otp_list.otp== int(otp):
			setattr(otp_list,'flag',int(1))
			#url='http://api.msg91.com/api/sendhttp.php?authkey=120246AC7mrK6PUjd5794d29c&mobiles='
			#url+=str(mobile)
			#url+='&message='+' \n '+mobile +' verified user for the app'
			#url+='&sender=mARPIT&route=4'
			#result = requests.request('GET', url)
			otp_list.save()
			try:
				user_list=user_data.objects.get(mobile=mobile)
				setattr(user_list,'name',name)
				setattr(user_list,'email',email)
				setattr(user_list,'mobile',mobile)
				setattr(user_list,'city',city)
				#setattr(user_list,'access_token',access_token)
				user_list.save()

				#user_token_data_list=user_token_data.objects.get(id=user_list.id)
				#setattr(user_token_data_list,'fcm',fcm)
				#setattr(user_token_data_list,'access_token',access_token_str)
				#user_token_data_list.save()
				access_token_str=str(user_token_data_list.access_token)
				response_json={
				"success":True,
				"message":"successful",
				"access_token":access_token_str,}

			except:
				#try:
				#	fcm__not_registered.objects.get(fcm=fcm).delete()
				#except:
				#	pass
				try:
					user_data.objects.create(
						name=name,
						email=email,
						mobile=mobile,
						city=city,
						#access_token=access_token
						)
					print "debug=99"
					user_list=user_data.objects.get(mobile=mobile)
					print "debug=101"

					#print"\nerror in getting id\n"
					user_token_data.objects.create(
						id=user_list.id,
						#fcm=fcm,
						access_token=access_token_str)
					print"debug=108"
					response_json={
					"success":True,
					"message":"successful",
					"access_token":access_token_str,
					}
				except:
					response_json={
					"success":False,
					#"message":"fcm not found in table",
					"access_token":access_token_str,
					}

			#return HttpResponse(str(response_json))
		else:
			#return HttpResponse('{"status":"not_verified"}')
			response_json={
			"success":False,
			"message":"not verified otp did not match",
			"access_token":"NULL",
			}

	except:
		response_json={
			"success":False,
			"message":"number does not exsist",
			"access_token":"NULL",
			}
	print str(response_json)
	return HttpResponse(str(response_json))