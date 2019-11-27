
import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from message.models import Message
from tools.logging_check import logging_check
from topic.models import Topic
from user.models import UserProfile


@logging_check('POST')
#留言系统
def messages(request,topic_id):
    if request.method == 'POST':
        json_str = request.body
        json_obj = json.loads(json_str)  # 把json格式的字符串转换成python的数据类型
        content = json_obj.get('content')
        parent_id = json_obj.get('parent_id',0)
        try:
            topic=Topic.objects.filter(id=topic_id)[0] #查找文章
        except Exception as e:
            result = {'code': 30110, 'error': 'The eroor is No topic  !'}
            return JsonResponse(result)
        Message.objects.create(content=content, parent_message=parent_id,
                               publisher_id=request.user,topic_id=topic)
        return JsonResponse({'code': 200})
    if request.method == 'GET':#查看留言
        all_m = Message.objects.filter(topic_id=int(topic_id))
        all_list = []
        for m in all_m:
            d= {}
            d['id'] = m.id
            d['content'] = m.content
            d['parent_message'] = m.parent_message
            d['topic'] = m.topic.id

            all_list.append(d)



        res = {'code': 200, 'data': all_list}
        return JsonResponse(res)
