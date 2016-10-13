from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def ver_check(request):
	try:
		version_row= version_data.objects.get(ver_type='production')
		version=version_row.version
		compulsory_update=version_row.compulsory_update
		#response_json={"success":True,"version":version,"compulsory_update":compulsory_update,}
		response_json["success"]=True
		response_json["version"]=version
		response_json["compulsory_update"]=compulsory_update
	except:
		response_json["success"]=False

	print str(response_json)
	return HttpResponse(str(response_json))




