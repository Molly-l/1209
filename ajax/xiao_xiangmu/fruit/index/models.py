from django.db import models

# Create your models here.
class User(models.Model):

    uphone=models.CharField(max_length=11,verbose_name='手机号')
    password=models.CharField(max_length=32,verbose_name='密码')
    username=models.CharField(max_length=20,verbose_name='用户名')
    eamil=models.EmailField(max_length=200,verbose_name='邮箱')
    isActive=models.BooleanField(verbose_name='是否激活',default=True)
    class Meta:
        db_table='User'


class GoodsType(models.Model):

    title=models.CharField(max_length=20,verbose_name='品类名')
    desc=models.CharField(max_length=200,verbose_name='品类描述')
    def __str__(self):
        return self.title
    class Meta:
        db_table='goods_type'
        verbose_name='商品类别'
        verbose_name_plural = verbose_name


class Goods(models.Model):

    title=models.CharField(max_length=40,verbose_name='商品名称')
    price=models.DecimalField(max_digits=7,decimal_places=2,verbose_name='价格')
    spec=models.CharField(max_length=20,verbose_name='规格')
    picture=models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片')
    goodsType=models.ForeignKey(GoodsType)
    created_time=models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(verbose_name='是否上架', default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

