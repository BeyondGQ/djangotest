from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# 主要负责显示
from django.views import View
from django.views.decorators.http import require_GET, require_POST

'''
请求  HttpRequest
响应  Http Response

'''


def require_http_method(param):
    pass


# @require_GET
# @require_POST
# @require_http_method(['GET', 'POST'])


def home(request):
    # request.POST
    # request.GET
    # 获取请求方式
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass

    request.POST.get('name', '')
    request.POST.get('page', '1')
    request.getlist('love')
    '''
    获取请求的路径  不包括域名
    request.path
    获取的客服端文件
    request.FILES.get()  UploadFiles
    name
    #字典 = request.FILES.get('file')
    filename
    content-type
    content 文件内容
    http

    request.META
    content_length content_type
    HOST
    PORT

    request.COOKIES
    '''

    return render(request, 'home.html')


def home1(request):
    HttpResponse

    # 重定向 转发
    HttpResponseRedirect
    '''
     # HttpResponseBadRequest  400 错误
     HttpResponseServerError  500 操作
     HttpResponseNotFound  404 操作
    '''

    # render  简写 转化
    # redirect  重定向
    '''
    重定向：3XX 服务器向浏览器发送一个302的状态码，浏览器接收到302后会立即重新定向到新的地址
    为什么要用重定向技术
    1.网站的内部结构调整
    2.网站的服务器发生改变了
    3.资源的名字修改了

    重定向：
    1.重定向发送两次请求
    2.浏览器的地址路径发生变化
    3.重定向可是站内或者站外

    转发：
    1.浏览器地址不会发生改变
    2.客服端只发送一次请求
    3. 转发一般指服务器内部转发
    '''
    return HttpResponse('hello')


def redirect_request(request):
    # 重定向可是是站内或者站外
    return redirect('http://www.baidu.com')


def render_request(request):
    # 转发
    return render(request, 'index.html')


# 基于类的转发
# class Home(View):
#     def login(self, request, *arg,**kwargs):
#         return render(request,'index.html')

def login(request, name):
    pass
