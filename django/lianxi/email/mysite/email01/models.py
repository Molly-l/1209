from django.db import models

# Create your models here.
#创建表，一个类就是一张表
class EmailList(models.Model):
    name=models.CharField('用户名',max_length=20,unique=True)
    adress=models.EmailField('地址',max_length=200,unique=True)
    def __str__(self):#设置对象显示的名字
        return self.name

