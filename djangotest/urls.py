"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from mydjango import views
from day04 import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url('mydjango/', include('mydjango.urls')),
    url('day01/', include('day01.urls')),
    url('day02', include('day02.urls')),
    url('day04', include('day04.urls')),
    # url('login/', views.login),
    url('form01/', include('form01.urls')),
    url('session/', include('session.urls')),
    url('middleware/', include('middleware.urls'))
]
