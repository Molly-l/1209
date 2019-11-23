from django.db import models

# Create your models here.
class Publisher(models.Model):
    #一表
    name = models.CharField(max_length=11)


class Book(models.Model):
    #多表
    title = models.CharField(max_length=11)
    # 指定外键
    publisher = models.ForeignKey(Publisher)
