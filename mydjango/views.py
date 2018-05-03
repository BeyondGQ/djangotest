from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from mydjango.models import DJ_User

def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    try:
        user = DJ_User.objects.get(username=username)
        if user:
            if user.password == password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('账号密码不存在')
    except:
        pass

    return HttpResponse('网络异常')


def register(request):
    # 获取客服端通过get请求发送过来的数据
    username = request.GET.get('username')
    password = request.GET.get('password')

    result = '注册失败'
    try:
        user = DJ_User.objects.filter(username=username)
        if user:
            result = '用户存在'
        else:
            DJ_User.objects.create(username=username, password=password)
            result = '注册成功'
    except:
        pass
    return HttpResponse(result)


def index(request):
    name = '老王'
    content = {'name': name}
    return render(request, 'index.html', content)

def update(request):
    uid = request.GET.get('uid')
    username = request.GET.get('username')
    password = request.GET.get('password')
    result = '更新失败'
    try:
        users = DJ_User.objects.filter(uid=uid).update(username=username, password=password)
        # users.username = username
        # users.save()
        # DJ_User.objects.
        result = '更新成功'

    except:
        pass
    return HttpResponse(result)