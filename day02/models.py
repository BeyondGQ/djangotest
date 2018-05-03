from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Shop_User'
        indexes = [
            models.Index(fields=['username'])
        ]


# 一对一的关系
# 主表（主表的主键作为从表的外键）  从表（从表设置外键）
# 第一个作用  多表查询需要去除笛卡尔积
# 第二个作用  通过主表查询从表的信息
class ShopInfo(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=64)
    shop_title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'S_User'
        indexes = [
            models.Index(fields=['shop_name', 'shop_title'])
        ]
        # unique_together=(('shop_name'))

class ShopDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    detail_content = models.TextField(max_length=255)
    '''
    to: 要关联的对象 （要关联的表）
    on_delete = 可选值
        models.CASCADE 级联删除
        models.SET_NULL 外键设置Null
        DO_NOTHING  什么都不做
        PROTECT 删除数据引发的错误
        models.SET 
        
        to_field 参照的字段  默认是主键
        外键在数据库里的命名  默认是 表名_主键的名字
    '''
    # 外键的要求  参照的列必须唯一
    shop_info = models.OneToOneField(ShopInfo, on_delete=models.SET_NULL, db_column='shop_id', to_field='shop_id', null=True)
    class Meta:
        db_table = 'S_Detail'

class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0)
    # 实现一对多
    shop_info = models.ForeignKey(ShopInfo, on_delete=models.CASCADE, db_column='shop_id', to_field='shop_id')

    class Meta:
        db_table = 'shop_car'
        indexes = [
            models.Index(fields=['shop_info']),
        ]












