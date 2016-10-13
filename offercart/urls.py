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
from splash_screen.views import ver_check
from otp.views import get_otp
from otp.views import ver_otp
from welcome.views import url_send
from city.views import send_all_city
from category.views import send_all_category
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^version/', ver_check),
    url(r'^otp/', get_otp),
    url(r'^otp1/', ver_otp),
    url(r'^url/', url_send),
    url(r'^city/', send_all_city),
    url(r'^category/', send_all_category),
    #url(r'^url1/', run_url),

    #url(r'^splash_screen/$',version),
]