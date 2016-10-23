from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from register.models import user_data
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
# Create your views here.
@csrf_exempt
def send_otp(request):
	if(request.method=='POST'):		
		response_json={}
		try:
			name=str(request.POST.get('name'))
			mobile=str(request.POST.get('mobile'))
			email=str(request.POST.get('email'))
			print name
			print mobile
			print email
			otp=random.randint(100000,999999)
			url='http://api.msg91.com/api/sendhttp.php?authkey=125195AvX4LUlVf57dcd941&mobiles='
			url+=mobile
			url+='&message='
			url+='Welcome to OfferCart App . You One Time Password is '+str(otp)+'&sender=OfrCrt&route=4'
			print requests.request('GET', url)
			print 'Otp Sent'
			try:
				otp_list=otp_data.objects.get(mobile=mobile)
		 		setattr(otp_list,'otp',int(otp))
		 		otp_list.save()
				print 'old user'
				pass
			except Exception,e:
		 		otp_data.objects.create(mobile=mobile,otp=int(otp))
				print 'new user'
				print e
			try:
				user_list=user_data.objects.get(mobile=int(mobile))
				setattr(user_list,'name',name)
				setattr(user_list,'email',email)
				setattr(user_list,'mobile',int(mobile))
				setattr(user_list,'city',NULL)
				user_list.save()
				print 'User Details Updated'
				pass
			except Exception, e:
				user_data.objects.create(
					name=name,
					email=email,
					mobile=int(mobile),
					city='',
					)
				print 'User Created'
				print e
			response_json['success']=True
			response_json['message']="Otp Sent Successfully"
			pass	
		except Exception, e:
			response_json['success']=False
			response_json['message']='Unable to send otp at this time'
			print e
		print str(response_json)
		return JsonResponse(response_json)


@csrf_exempt
def verify_otp(request):
	
	response_json={}
	try:
		mobile=str(request.POST.get("mobile"))
		otp=str(request.POST.get("otp"))
		access_token='No Access Token'
		otp_list=otp_data.objects.get(mobile=mobile)
		

		if otp_list.otp == int(otp):
			setattr(otp_list,'flag',True)
			access_token= jwt.encode({}, str(mobile), algorithm='HS256')
			
			try:
				access_token_data.objects.create(
					access_token=access_token
					)
				otp_list.save()
				response_json['access_token']=str(access_token)
				print 'Access Token Created'
				pass
			except Exception,e:
				print 'Unable to create Access Token'
				response_json['access_token']='None'
				print e
						
		else:
			response_json['success']=False
			response_json['message']='Invalid Otp'
		pass
	except Exception,e:
		response_json['success']=False
		response_json['message']='Invalid Mobile Number'
		print e
	print str(response_json)
	return JsonResponse(response_json)