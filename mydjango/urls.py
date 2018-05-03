from django.conf.urls import url

from mydjango import views

urlpatterns = [
    url('login/', views.login),
    url('register/', views.register),
    url('index/', views.index),
    url('update/', views.update),  # 注册接口

]
