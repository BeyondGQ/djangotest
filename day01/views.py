from django.db.models import Q, Count
from django.http import HttpResponse

from django.shortcuts import render
from day01.models import DJ_User
# from django.shortcuts import Q

'''
filter
过滤条件
返回值
QUERYSET 对象   列表
'''

# Create your views here.
#User.objects.get()
# 当查询不存在，直接抛异常
def test(request):
    # select * from  表名 WHERE
    # users = DJ_User.objects.filter(username='xiaoming')
    # users = DJ_User.objects.filter(username='xiaoming')
    # users_list = DJ_User.objects.filter(username='xiaoming',password='123456')
    # user_list=DJ_User.objects.exclude(username='xiaoming')
    # user_list = DJ_User.objects.filter(username='xiaoming').order_by('create_date')
    '''
    order_by
    更具查询的数据排序
    参数 排序的字段
    默认是升序  降序：字段前面加-
    '''
    # SELECT *  FROM USER
    # 只能是正整数  分页效果
    #SELECT 8 FROM USER limit 10,20
    # SELECT 8 FROM USER limit 10 OFFSET 20
    # user_list = DJ_User.objects.all()
    # user_list = DJ_User.objects.all()[0:3]

    users = DJ_User.objects.all().values('uid', 'username')
    #参数 要过滤的列
    # 返回 querset 对象 [{'uid':1,'username':'xikoaming'}]
    # for dic in users:
    #     for uid,name in dic.items():
    #         print(uid)
    #         print(name)
    #
    #
    # DJ_User.objects.all().values_list('uid', flag=True)
    # users = DJ_User.objects.all().values_list('uid', 'username')
    # for id,name in users:
    #     print(uid)
    #     print(name)

    # kind 年 月 日 时 分 秒
    # year 只会返回年
    # month 返回年月
    # day 返回年月日

    # users_date = DJ_User.objects.dates('create_date', 'day')
    # users_date = DJ_User.objects.all().datetimes('create_date', 'second')

    # 执行原生的sql语句
    # 返回queryset
    # qsr = DJ_User.objects.raw('SELECT * FROM t_user')
    # li = []
    # for q in qsr:
    #      q.__dict__.pop('_state')
    #      li.append(q)
    # print(li)

    return render(request, 'index.html')


#相当于对象sql的关键字的封装 AND  Or NOT
def test1(request):
    DJ_User.objects.filter(Q(username='xiaoming') | Q(username='xiaohong'))
    DJ_User.objects.filter(~Q(uid=1))


    # QuerySET []
    user = DJ_User.objects.filter(pk=1).first()

    return render(request, 'index.html')


def test2(request):
    # 没有满足条件的会报错
    #User.object.get()
    # 返回一个元组 第一个值是查询 或者合返回的保存的对象 create  True 表示执行save 操作
    user = DJ_User.objects.get_or_create(username='xiaoming',password='123456')
# insert into table () values(),(),()
    # 批量插入
    '''
    objects  列表
    batch_size =列表的长度
    '''
    user_list =[]
    for i in range(10):
        user = DJ_User(username='test'+str(i), password='123456')
        user_list.append(user)
    DJ_User.objects.bulk_create(user_list)

    # default ={}  **kwargs
    DJ_User.objects.bulk_create(default={}, username='余屌')
    # try:
    #     DJ_User.objects.get(id=10)
    # except:
    #     DJ_User.objects.create()

    return render(request, 'index.html')


def test3(request):
    # 聚合函数
    # Count AVG  ROUND
    '''
    select count(name) name_count from t_user
    :return:
    '''
    count = DJ_User.objects.aggregate(name_count=Count('username'))

    # 大于 gt 小于 lt  大于等于gte 小于等于lte
    DJ_User.objects.filter(uid__gt=1)
    DJ_User.objects.filter(uid__lt=1)
    DJ_User.objects.filter(uid__gte=1)
    DJ_User.objects.filter(uid__gte=1)

    # WHERE uid in (1,2,3)
    DJ_User.objects.filter(uid__in=[1, 2])
    return render(request, 'index.html')

    #ignore

    # between 1 and 10
    DJ_User.objects.filter(uid__range=[1,10])
    DJ_User.objects.filter(username_startswith='a')
    DJ_User.objects.filter(username__istartswith='a')