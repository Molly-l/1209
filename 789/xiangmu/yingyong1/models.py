from django.db import models

# Create your models here.
class Laoshi(models.Model):
    name=models.CharField("名字", max_length=30, unique=True)
    age=models.CharField("年龄", max_length=8, unique=True)
