import datetime

from day04.models import UserInfo
from djangotest import settings
from django.shortcuts import render

# Create your views here.
from django.views import View



class UploadFile(View):
    # def get(self):
    #     pass
    '''
    前端  表单 必须是POST请求
    ENCTYPE=multipart/from-date
    input  type='file'
    如果发现request.FILES是空 检查是否为POST 请求
    '''

    def post(self, request):
        '''
        request.FILES 是一个字典 包含
        文件的名称
        文件的内容
        content-type  文件的类型

        '''
        upload_file = request.FILES.get('img')
        # upload_file = request.FILES.getlist('img')
        # 多文件上传

        '''
        read()
        读取文件上传的数据，慎用
        multiple_chunks(size)
        判断文件是否够大 
        chunks()
        返回一个生成器对象，把上传文件切割  可以制定size
        .name
        获取文件的名称
        size  获取文件的大小
        content-type  上传文件的类型
        charset  文件的编码
        
        '''
        '''
        客服端上传文件  服务端保存文件
        保存文件的路径到数据库
        '''

        '''
        对客服端上传的文件服务器要重新命名 防止同名文件覆盖
        对路径进行细分 对文件进行重命名 （保证名字是唯一的）
        1.获取文件的后缀名
        os.path.splittext()   
        str.split()
        str.slice()
        # 2.IMG——年月日时分秒
        '''
        # IMG_201802211124536.jpg
        # [‘文件名称’， '后缀名']
        file_name_last = upload_file.name[upload_file.name.find('.'):]
        file_name = 'IMG_{}{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'), file_name_last)

       # 123.jpg  xx.pdf
        with open(settings.MEDIA_ROOT + '/img/' + file_name, 'wb') as file:
            # 包二进制的数据保存到服务器
            for chunk in upload_file.chunks():
                file.write(chunk)

        return render(request, 'index2.html')

# def upload(request):
#     if request.method == 'Post':
#         pass

def index(request):
     pass
     return render(request, 'file.html')

def upload(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserInfo()
        user.head = request.FILES.get('head')
        user.username = username
        user.password = password
        user.save()

    return render(request, 'index2.html')

