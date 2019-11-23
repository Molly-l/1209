from django.db import models

# Create your models here.
#1对1:

class Author(models.Model):
    
    name=models.CharField(max_length=11)


class Wife(models.Model):
    name = models.CharField(max_length=11)
    # 指定外键
    author = models.OneToOneField(Author)
