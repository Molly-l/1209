from django.db import models

# Create your models here.

class BookStore(models.Model):
    title=models.CharField('姓名',max_length=20)
    price=models.DecimalField('定价',max_digits=5,\
                           decimal_places=2,default=0.0)
    desc=models.CharField('描述',max_length=100,default='')


