from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def about_us(request):
    if request.method == 'GET':
        response_body = {}
        response_body['success'] = True
        response_body['message'] = "Successful"
        response_body['title'] = "About Brand Store"
        response_body[
            'description'] = "Brand Store is a startup ,\n Brand Store sells out Offers from Traditional shops. You " \
                             "will get a offer code in your mobile phone after registering for a offer.\n\n Have a " \
                             "Nice Day:) "
        response_body[
            'image_url'] = request.scheme + '://' + request.get_host() + '/media/about_us/brand_store_logo-web.png'

        return JsonResponse(response_body)
