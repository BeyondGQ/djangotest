from _md5 import md5

from django.shortcuts import render

# Create your views here.
from day02.models import User, ShopCar

def add_shop_car(request):
    user = User()  # 创建用户对象
    user.username = 'zhangsan'
    # ShopCar.objects.create()
    # user.password = md5('123')
    user.password = '123456'
    user.save()
    shop_iterms = []
    for i in range(10):
        sc = ShopCar(count=1, user_id=user.user_id, shop_info_id=1)
        shop_iterms.append(sc)
    ShopCar.objects.create(shop_iterms)
    return render(request, 'index.html')

def find_shop_items(request):
    # uid = request.GET.get('user_id')
    # shop_items = ShopCar.objects.filter(user_id=uid)
    # 查出所有买的用户对应的购物车信息
    # 查询所有的用户
    users = User.objects.all()
    for user in users:
        # 查询每个用户下面所有的购物车信息保存的信息
        shop_items = ShopCar.objects.filter(user_id=user.user_id)
        #  将用户下的所有的购物车信息保存到用户(对象)中
        user.shop_items = shop_items
    # 前端 + 模板语言

    #  content = {} 字典
    content = {'user': users}
    return render(request, 'index.html', content)

class Test():
    def __init__(self, name='123', age=12):
        self.name = '123'
        self.age = 12


def test_templates(request):
    li = [0, 1, 2, 3, 4]
    dic = {
        'name': '123321',
        'pwd': '123456',
    }
    content = {
        'num': 1,
        'li': li,
        'dic': dic,
        'test': Test()
    }
    return render(request, 'temp01', content)





