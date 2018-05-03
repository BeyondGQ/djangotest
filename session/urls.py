from django.conf.urls import url

from session import views
urlpatterns = [

    url('test/', views.test_cookie),
    url('test2/', views.test_cookie2),
    url('test3/', views.test_session),
    url('test4/', views.test_session2),
    url('ligin/', views.login),
    url('index/', views.index),


]