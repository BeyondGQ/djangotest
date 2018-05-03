from django.conf.urls import url
from day02 import views
urlpatterns = [
    url('add_shop_car/', views.add_shop_car),  # 注册接口
]
