from django.db import models
# 数据迁移
# 创建表 python manage.py makemigrations [目录（可指定app_name,不指定就是整个工程）]
# 在migrations 0001init文件
# python manage.py migrate [目录]   迁移数据

# Create your models here.
# 编写模型
# 定义类 继承 models.Model
class DJ_User(models.Model):
    # 创建主键，如果不重写 默认id
    uid = models.AutoField(primary_key=True)  # 创建主键
    # username  Varchar(32)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=1, default='1')
    # decimal(7,2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    '''
    auto_now =True 创建的时候生成日期，每次修改的时候生成日期
    auto_now_add 创建的时候生成日期，每次修改的时候不生成日期
    不能同时存在
    '''
    create_date = models.DateField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)
    head_img = models.ImageField(upload_to='uploads/')

    # 唯一 自动创建索引
    class Meta:
        # abstract = True
        db_table = 'D_USER'
        ordering = ['create_date']
        # 默然时升序 -表示降序 ？ 随机排序
        # ordering = ['-create_date'] 降序
        verbose_name = '用户'
        verbose_name_plural = '用户列表'
        # 1.11新加的
        # indexes = ['username']
        # indexes = [models.Index('username')]
        # create index idx_user_name on user(username


# create table mydjango_user
# 更改模型时 需要重新进行数据迁移
