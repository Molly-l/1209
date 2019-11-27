import json

import jwt
from django.http import JsonResponse
from django.shortcuts import render

from message.models import Message
from tools.logging_check import logging_check, get_user_by_request
# Create your views here.
from user.models import UserProfile
from .models import Topic



@logging_check('POST','DELETE')#获取 用户文章数据
def topics(request,author_id):
    if request.method=='GET':

        # /v1/topics/zxc?category=tec|no-tec  分类查看用户的所有文章列表
        # /v1/topics/zxc?t_id=1  查看文章id为1 的文章详情
        # /v1/topics/zxc  没有查询字符串，查看用户的所有文章列表

    #1 访问当前博客的访问者 visitor
    #2 当前被访问的博客的博主 author
        authors=UserProfile.objects.filter(username=author_id)
        if not authors:
            result = {'code': 30104, 'error': 'The author is not existed !'}
            return JsonResponse(result)
        #当前被访问的博客博主
        author=authors[0]

        visitor_username=None
        #访问者
        visitor=get_user_by_request(request)

        if visitor:
            visitor_username=visitor.username  #把取到的用户的用户名赋给visitor_username
#按上面三种情况分别查看
        #1.文章详情
        t_id=request.GET.get('t_id')#文章的id
        if t_id:#获取指定文章的详情页
            t_id=int(t_id)

            is_self=False
            if author_id==visitor_username:#author_id 作者的用户名
            #博主访问自己的博客
                is_self = True
                try:
                    author_topic = Topic.objects.get(id=t_id) #通过文章id获取到文章对象
                except Exception as e:
                    result = {'code': 30108, 'error': 'The eroor is No topic !'}
                    return JsonResponse(result)
            else:#非博主访问当前博客
                try:
                    author_topic = Topic.objects.get(id=t_id,limit='public')
                except Exception as e:
                    result = {'code': 30109, 'error': 'The eroor is No topic visitor !'}
                    return JsonResponse(result)
            #生成具体返回值
            res=make_topic_res(author,author_topic,is_self)
            return JsonResponse(res)


        #2/3.文章列表
        else:

            category=request.GET.get('category')
            if category in ['tec','no-tec']:#按种类筛选
                if author_id==visitor_username:
                    #博主访问自己的博客
                    author_topics=Topic.objects.filter(author_id=author_id,category=category)
                else:
                    #陌生访客访问他人博客
                    author_topics=Topic.objects.filter(author_id=author_id,limit='public',category=category)
                res=make_topics_res(author,author_topics)
                return JsonResponse(res)

            else: #全量不分种类筛选
                if author_id==visitor_username:
                    #博主访问自己的博客
                    author_topics=Topic.objects.filter(author_id=author_id)
                else:
                    #陌生访客访问他人博客，只返回公开权限
                    author_topics=Topic.objects.filter(author_id=author_id,limit='public')
                res=make_topics_res(author,author_topics)
                return JsonResponse(res)





    # 发表博客
    elif request.method=='POST':

        author=request.user #从token中获取登陆的用户名对应的用户
        if author.username!=author_id:
            result = {'code': 30101, 'error': 'The author is eroor'}
            return JsonResponse(result)

        json_str = request.body
        json_obj=json.loads(json_str)
        title = json_obj.get('title')
        #注意xss(前段网页代码注入)攻击，
        import html
        title=html.escape(title) #将用户输入进行转义(代码不可执行)，

        category=json_obj.get('category')
        if category not in ['tec','no-tec']:
            result = {'code': 30102, 'error': 'The category is eroor'}
            return JsonResponse(result)
        limit = json_obj.get('limit')
        if limit not in ['private', 'public']:
            result = {'code': 30103, 'error': 'The limit is eroor'}
            return JsonResponse(result)
        #带样式的文章内容
        content = json_obj.get('content')
        #纯文本的文章内容-用于做文章简介的切片
        content_text=json_obj.get('content_text')
        introduce=content_text[:30] #取出纯文本内容前30个存为文章简介
        #创建topic到Topic数据库
        Topic.objects.create(title=title,limit=limit,category=category,
                            content=content,introduce=introduce,author=author)
        result={'code':200,'username':author.username}
        return JsonResponse(result)




    
    elif request.method=='PUT':
        pass

    elif request.method=='DELETE':
        #删除博客文章，真

        user=request.user
        if author_id != user.username:
            result = {'code': 30105, 'error': 'The author_id is erorr !'}
            return JsonResponse(result)
        topic_id = request.GET.get('topic_id')#获取到文章的id
        if not topic_id:
            result = {'code': 30106, 'error': 'Must be give me topic_id!'}
            return JsonResponse(result)
        topic_id=int(topic_id)
        try:
            topic=Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {'code': 30107, 'error': 'The topic is not existed !'}
            return JsonResponse(result)
        topic.delete()
        return JsonResponse({'code':200})




#生成文章列表返回值
def make_topics_res(author,author_topics):
    res = {'code': 200,'data':{}}
    res['data']['nickname']=author.nickname
    res['data']['topics'] =[]
    for topic in author_topics:
        d={}
        d['id']=topic.id
        d['title']=topic.title
        d['introduce']=topic.introduce
        d['category']=topic.category
        d['create_time']=topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        d['author']=author.nickname
        res['data']['topics'].append(d)
    return res


#获取上一篇文章的id和title
def make_topic_res(author, author_topic,is_self):

    if is_self:
        #博主访问自己的博客
        #next_topic大于当前文章id 的第一个
        next_topic=Topic.objects.filter(id__gt=author_topic.id,author=author).first()
        last_topic=Topic.objects.filter(id__lt=author_topic.id,author=author).last()

    else:
        #访客访问当前博客
        next_topic=Topic.objects.filter(id__gt=author_topic.id,author=author,limit='public').first()
        last_topic=Topic.objects.filter(id__lt=author_topic.id,author=author,limit='public').last()
    if next_topic:
        next_id=next_topic.id
        next_title=next_topic.title
    else:
        next_id = None
        next_title = None

    if last_topic:
        last_id=last_topic.id
        last_title=last_topic.title
    else:
        last_id = None
        last_title = None

    res={'code':200,'data':{}}
    res['data']['title']=author_topic.title  #文章所有信息放到字典里面，返回出去
    res['data']['nickname']=author.nickname
    res['data']['content']=author_topic.content
    res['data']['introduce']=author_topic.introduce
    res['data']['category']=author_topic.category
    res['data']['create_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    res['data']['author']=author.nickname

    res['data']['next_id']=next_id    #下一篇文章的id放到res这个字典中
    res['data']['next_title']=next_title
    res['data']['last_id']=last_id
    res['data']['last_title']=last_title
    #留言
    #ToDO添加留言显示
    #
    all_message=Message.objects.filter(topic_id=author_topic).order_by('-created_time') #本篇文章下所有留言内容
    m_count=0
    #留言专属容器
    msg_list=[]
    #
    reply_home={}
    for message in all_message:
        m_count+=1
        if message.parent_message:
            reply_home.setdefault(message.parent_message,[])
            reply_home[message.parent_message].append({'msg_id':message.id,
                                                       'content': message.content,
                                                       'publisher_avatar':  str(message.publisher_id.avatar),
                                                       'created_time': message.created_time.strftime('%Y-%M-%d '
                                                                                                    '%H:%M:%S'),
                                                       })
        else:
            msg_list.append({'id':message.id,
                             'content':message.content,
                             'publisher':message.publisher_id.username,
                             'publisher_avatar': str(message.publisher_id.avatar),
                             'created_time': message.created_time.strftime('%Y-%M-%d %H:%M:%S'),

                             })

            for m in msg_list:
                if m['id'] in reply_home:
                    m['reply']=reply_home[m['id']]




            res['data']['messages']=msg_list
            res['data']['messages_count']=m_count




    return res
