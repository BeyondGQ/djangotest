from django.db import models

# Create your models here.



class UserInfo(models.Model):
    ui = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    # '直接定位到media'
    head = models.FileField(upload_to='account/user/zhangsan/%Y%m%d')

    class Meta:
        db_table = 'userinfo'
