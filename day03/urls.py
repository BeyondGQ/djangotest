from django.conf.urls import url

from day03 import views

urlpatterns = [
    url('redirect/', views.redirect_request),
    url('render/', views.render_request)
]