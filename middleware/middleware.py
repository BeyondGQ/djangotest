# # django1.10
# class middle1(object):
#     #  请求到达 view 之前
#     def process_request(self, request):
#         print('middel')
#
#     def process_view(self, request,view_func, view_args, view):
#         print('')
#
#         # view 返回Response 之后
#     def process_exception(self,request, exception):
#         print('')

#1.10以上的版本

# 同一ip地址十分钟禁止重复注册
'''
1.获取客服端的Ip地址  记录时间 需要记录时间sesssion
2.通过查询ip 地址做后一次是时间 跟当前这个时间进行比较
'''
import datetime

from django.http import HttpResponse
from django.shortcuts import render

from middleware.models import Ip


class middle01(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        response = self.get_response
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 获取客服端的ip地址
        if request.get_path == '/account/register/':
            addr = request.Meta['REMOTE_ADDR']
            client_ip = Ip.objects.get(cip=addr)
            if client_ip:
                if(datetime.datetime.now()-client_ip.last_time).total_seconds() < 600 * 0:
                    return HttpResponse('十分钟内禁止注册')
                client_ip.last_time = datetime.datetime.now()
                client_ip.save()
                return render(request, 'register.html')


        return HttpResponse('这个是中间件返回的')

    def process_exception(self, request, exception):
        print('middle------exception')

    def process_template_response(self, request, response):
        print('middle------template')