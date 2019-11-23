from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=11,verbose_name='用户名')
    password=models.CharField(max_length=6,verbose_name='密码')
    nickname=models.CharField(max_length=11,verbose_name='昵称')
    class Meta:
        db_table='user'

    def to_dict(self):

        data = {}
        data['username'] = self.username
        data['password'] = self.password
        data['nickname'] = self.nickname
        return data


