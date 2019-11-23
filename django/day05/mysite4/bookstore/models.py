from django.db import models



# Create your models here.\
class BookStore(models.Model):
    title=models.CharField(max_length=20,verbose_name='书名')
    def __str__(self):
            return '<%s>' %(self.title)

class Book(models.Model):
    title=models.CharField(max_length=50,
                           verbose_name='书名', null=False,unique=True)
    pub = models.CharField(max_length=11,
                             verbose_name='出版社',null=False )
    price = models.DecimalField(verbose_name='图书定价', max_digits=5,\
                            decimal_places=2)
    market_price = models.DecimalField(verbose_name='图书零售价',max_digits=5,decimal_places=2)
    def __str__(self):
            return '<%s>' %(self.title)
    class Meta:
        #当前model类对应的数据表表名
        db_table='book'
        verbose_name='图书'
        verbose_name_plural=verbose_name


class Author(models.Model):
    name=models.CharField(max_length=11,
                           verbose_name='姓名',null=False)
    age= models.IntegerField(verbose_name='年龄', \
                             default=1)
    email= models.EmailField(verbose_name='邮箱', null=True)
    def __str__(self):
            return '<%s %s>' %(self.name,self.age)

    class Meta:
        # 当前model类对应的数据表表名
        db_table = 'Author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name
