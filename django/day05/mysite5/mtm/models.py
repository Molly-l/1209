from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=11)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=11)
    #属性
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.title