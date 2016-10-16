from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def ver_check(request):
	try:
		response_json={}
		version_row= version_data.objects.get(ver_type='arp')
		version=version_row.version
		compulsory_update=version_row.compulsory_update
		#response_json={"success":True,"version":version,"compulsory_update":compulsory_update,}
		response_json["success"]=True
		response_json["version"]=version
		response_json["compulsory_update"]=compulsory_update
		response_json["message"]="version_data found"
	except:
		response_json["success"]=False
		response_json["message"]="version_data not found"

	print str(response_json)
	return HttpResponse(str(response_json))

#from Splash_Screen.models import version_control

@csrf_exempt
def send_fcm(request):
	version=version_data.objects.all()[0].version
	compulsory_update=version_data.objects.all()[0].compulsory_update
	if(request.method=='POST'):
		try:
			fcm=str(request.POST.get("fcm"))
			if fcm!=None:

				print "fcm recived:"+fcm
				try:
					fcm_list=user_token_data.objects.get(fcm=fcm)
					response_json={"success":True,
					"version":int(version),
					"message":"already added",
					"compulsory_update":int(compulsory_update)}
				except:
					try:
						fcm_list=fcm__not_registered.objects.get(fcm=fcm)
						response_json={"success":True,
						"version":int(version),
						"message":"already added",
						"compulsory_update":int(compulsory_update)}
					except:
						fcm__not_registered.objects.create(fcm=fcm)
						response_json={"success":True,
						"version":int(version),
						"message":"successfully added",
						"compulsory_update":int(compulsory_update)}
			else:
				response_json={"success":False,
				"version":int(version),
				"message":"fcm none recieved",
				"compulsory_update":int(compulsory_update)}

		except:
			response_json={"success":False,
			"version":int(version),
			"message":"send fcm : invalid parameters",
			"compulsory_update":int(compulsory_update)}

	else:
		response_json={"success":False,
				"message":"not post method",
				"compulsory_update":int(compulsory_update),
				"version":int(version),}
	print str(response_json)
	return HttpResponse(str(response_json))

def initial(request):
	return HttpResponse("<a href=./login>admin_login</a>")



