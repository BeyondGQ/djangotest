from django.http import HttpResponse
from django.shortcuts import render, redirect

from session.models import User


def test_cookie(request):
    #获取cookie信息
    request.COOKIES
    # request.COOKIES['username'] 如果key不存在 会跑异常
    username = request.COOKIES.get('username')
    # del request.COOKIES.get('username') 删除值
    # username = request.get_signed_cookie('username', salt='test')

    # 响应
    resp = render(request, 'index2.html')
    # resp = HttpResponse('')
    # reqsp = redirect()
    if username:
        resp.set_cookie('username', 'zhangsan')
        # resp.set_signed_cookie('username', 'xiaohong', salt='tset') # 加密写法
    return resp

def test_cookie2(request):
    # 加密写法
    resp = render(request, 'index2.html')
    username = request.get_signed_cookie('username', default='', salt='test')
    #  username = request.COOKIES.get('username')
    if username:
         #  path 限制范围的路径 /session/  能访问/session/test1/test2/
         #  /session/test2/ 表示 http://ip:端口/session/test2 或者/xxx 能获取这个cookie信息
         #  其他的比如说像 http://ip:端口/session/test1  或者 http://ip:端口/session1/test/test2  都不能访问这个cookie信息
        resp.set_signed_cookie('username', 'xiaohong', salt='test',max_age=7 * 24 * 60 * 60,
                               domain=None, path='/session/', httponly=False)
        #  删除cookie
        # resp.delete_cookie('username')
    return resp

# 不要存中文
# 缺点 安全性不高 而且客服端可以禁用
# 数据存在客服端   减轻服务器的压力

'''
在setting.py 中药开启，默认已经开启  如果你用会话追踪技术可以去关闭
django 处理session数据 的处理方式
1.存在数据库中
2.缓存
3.文件中
4.缓存+ 数据库
5.加密 cookie
6. django-redis-session(第三方 需要单独安装)
'''

def test_session(request):
    # request.session['username'] # key 不存在就报错
    #{'username','xiaoming'}
    username = request.session.get('username',  default=None)
    # 设置值 存在就修改 不存在就设置
    request.session.setdefault('username', '123123')
    # request.session['user'] = '123'

    #获取所有的key
    request.session.keys()
    # 获取所有的值
    request.session.values()
    # 获取所有的键值对
    request.session.iteritems()

    request.session.set_expiry(2 * 24 * 60 * 60)
    '''
    如果设置的值是个整数  多少秒之后失效
    如果是有一个datetime对象  在制定的日期失效
    如果是θ  表示浏览器关闭失效
    如果是None 表示参照全局的设置
    '''
    pass

def test_session2(request):
    # request.COOKIES.get('sessionid')
    # request.session.setdefault('username','123')
    # resp = render(request, 'index2.html')
    # resp.setdefault('sessionid', request.session.session_key)
    #
    count = request.session.get('count', defalut=0)
    if count == 0:
        count = 1
        request.session.setdefault('count', 1)

    else:
        count += 1
        # 不存在就设置，存在就不设置
        request.session['count'] = count

    return HttpResponse('次数--->{}'.format(count))

 # session 实现免登录
def login(request):
     username = request.POST.get('username')
     password = request.POST.get('password')
     user = User.objects.filter(username=username, password=password)
     if user:
         request.session.setdefault('username', user.name)
         request.session.setdefault('username', user.name)
         request.session.set_expiry(7 * 24 * 60 * 60)
         return  redirect('/session')
     else:
         render(request, '/login.html',{'msg':'账号密码错误'})

def index(request):
    username = request.session.get['username']
    if username:
        render(request,'index2.html',{'username':username})