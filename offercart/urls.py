"""offercart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from splash_screen.views import version
from otp.views import send_otp
from otp.views import verify_otp
from welcome.views import welcome
from city.views import city
from category.views import category
from shop.views import shop
from offer.views import send_offer
from django.conf import settings
from city.views import city
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^version/$', version),#completed
    url(r'^send_otp/$', send_otp),
    url(r'^verify_otp/$', verify_otp),
    url(r'^welcome/$', welcome),
    url(r'^city/$', city),
    url(r'^category/$', category),
    url(r'^shop/$', shop),
    url(r'^offer/$', send_offer),
    url(r'^myoffer/$', send_offer),

    #url(r'^splash_screen/$',version),
]#+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)