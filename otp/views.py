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
from customs.sms import send_sms

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
			msg='Welcome to OfferCart App . You One Time Password is '+str(otp)
			send_sms(mobile,msg)
			print 'Otp Sent'
			try:
				otp_list=otp_data.objects.get(mobile=int(mobile))
		 		setattr(otp_list,'otp',int(otp))
		 		setattr(otp_list,'flag',False)
		 		otp_list.save()
				print 'old user'
				user_list=user_data.objects.get(mobile=int(mobile))
				setattr(user_list,'name',name)
				setattr(user_list,'email',email)
				#setattr(user_list,'mobile',int(mobile))
				setattr(user_list,'city',"")
				user_list.save()
				print 'User Details Updated'
		
			except Exception,e:
		 		otp_data.objects.create(mobile=int(mobile),otp=int(otp))
		 		user_data.objects.create(
					name=name,
					email=email,
					mobile=int(mobile)
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
			access_token= jwt.encode({'mobile':str(mobile)}, '999123', algorithm='HS256')
			
			try:
				access_token_data.objects.create(
					access_token=access_token
					)
				otp_list.save()
				response_json['access_token']=str(access_token)
				print 'Access Token Created'
				response_json['success']=True
				response_json['message']='Successful'
			except Exception,e:
				response_json['access_token']='None'
				print e
				response_json['success']=False
				response_json['message']='Unable to create Access Token'
			

		else:
			response_json['success']=False
			response_json['message']='Invalid Otp'
	except Exception,e:
		response_json['success']=False
		response_json['message']='Invalid Mobile Number'
		print e
	print str(response_json)
	return JsonResponse(response_json)