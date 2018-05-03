from django.conf.urls import url

from middleware import views
urlpatterns = [
    url('test/', views.test),
]