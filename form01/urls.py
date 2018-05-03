from django.conf.urls import url

from form01 import views
urlpatterns = [

    url('test/', views.test),
    url('register/', views.register)

]