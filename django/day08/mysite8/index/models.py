from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=11,verbose_name='书名')
    def __str__(self):
        return self.title


class Email_list(models.Model):
    
    username = models.CharField(verbose_name="用户名", max_length=30, unique=True)
    email=models.EmailField(verbose_name="邮箱", max_length=230, unique=True) #unique 唯一索引：字段值不重复
    

    def __str__(self):
        return "用户" + self.username
