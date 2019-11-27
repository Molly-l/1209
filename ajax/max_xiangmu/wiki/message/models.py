from django.db import models

# Create your models here.
from topic.models import Topic
from user.models import UserProfile


class Message(models.Model):
    content = models.CharField(max_length=50, verbose_name='留言内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='留言创建时')
    parent_message = models.IntegerField(verbose_name='f留言')
    publisher_id = models.ForeignKey(UserProfile)
    topic_id = models.ForeignKey(Topic)
    class Meta:
        db_table='message'