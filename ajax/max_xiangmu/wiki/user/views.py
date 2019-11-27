import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
from .models import UserProfile
from wtoken.views import make_token
from tools.logging_check import logging_check


# Create your views here.
@logging_check('PUT')
def users(request,username=None):
    #查看用户信息
    if request.method == 'GET':
        if username:
            users = UserProfile.objects.filter(username=username)
            user = users[0]
            #拿具体用户数据
            #有查询字符串[]
            if request.GET.keys():  #.keys() 获取字典里面所有的键
                #查询字符串
                data={}
                for k in request.GET.keys():
                    if hasattr(user,k): #查询字符串是否为表对象字段
                        #
                        if k=='password':
                            continue

                        v=getattr(user,k)#取出表中某个对象的某个字段的值
                        data[k]=v
                res = {'code': 200, 'username': username, 'data':data}

            else:
                #无查询字符串

                res={'code':200,'username':username,'data':{\
                    'nickname':user.nickname,'sign':user.sign,
                'info':user.info,'avatar':str(user.avatar)}}





            return JsonResponse(res)

        else:
            #拿数据
            all_users=UserProfile.objects.all()
            users_data=[]
            for user in all_users:
                dic={}
                dic['nickname']=user.nickname
                dic['username']=user.username
                dic['sign']=user.sign
                dic['info']=user.info
                users_data.append(dic)
            res={'code':200,'data':users_data}
            return JsonResponse(res)



    # 创建用户
    elif request.method == 'POST':

        json_str = request.body  #从请求中获取json格式的字符串
        if not json_str:
            result = {'code':10102, 'error':'Please give me data~'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)#把json格式的字符串转换成python的数据类型
        username = json_obj.get('username')
        email = json_obj.get('email')
        if not username:
            result = {'code':10101, 'error':'Please give me username~'}
            return JsonResponse(result)
        #TODO 检查 json dict 中的key 是否存在
        password_1 = json_obj.get('password_1')
        password_2 = json_obj.get('password_2')
        if password_1 != password_2:
            result = {'code': 10103, 'error':'The password is error!' }
            return JsonResponse(result)

        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10104, 'error':'The username is already existed !'}
            return JsonResponse(result)

        #生成散列密码   散列作用：定长32位，不可逆，雪崩(密码中1位变动，整个散列都变)
        pm = hashlib.md5()  # 生成一个散列对象
        pm.update(password_1.encode()) #想要进行散列计算的值加进去，值必须是二进制

        #创建用户
        try:  #增加数据到UserProfile表中
            UserProfile.objects.create(username=username, password=pm.hexdigest(),nickname=username,email=email)
        except Exception as e:
            print('---create error---')
            print(e)
            result = {'code':10105, 'error':'The username is already existed !!'}
            return JsonResponse(result)
        login_time=time.time()

        #生成token
        token = make_token(username, 3600*24,login_time)
        result = {'code':200, 'data':{'token':token.decode()},'username':username}
        return JsonResponse(result)

    # 更新数据
    elif request.method == 'PUT':
        if not username:
            res={'code':10108,'error':'Must be give me username!!'}
            return JsonResponse(res)
        json_str=request.body
        json_obj=json.loads(json_str)
        nickname=json_obj.get('nickname')
        sign=json_obj.get('sign')
        info=json_obj.get('info')
        #更新
        users= UserProfile.objects.filter(username=username)
        user = users[0]
        # user=request.user
        #当前请求，token用户 修改自己数据
        # if user.username!=username:
        #     result={'code':10109,'error':'The username is eroor!'}
        #     return JsonResponse(result)



        to_update=False
        if user.nickname!=nickname:
            to_update = True
        if user.sign != sign:
            to_update = True
        if user.info!=info:
            to_update = True

        if to_update:
            #做更新
            user.nickname = nickname
            user.sign = sign
            user.info = info
            user.save()

        return JsonResponse({'code':200,'username':username})

@logging_check('POST')#处理头像上传
def users_avatar(request,username):

    if request.method!='POST':
        result = {'code': 10110, 'error': 'Please use POST!'}
        return JsonResponse(result)
    user=request.user
    if user.username!= username:  #token中获取的用户的用户名/请求中携带的用户名
        result = {'code': 10109, 'error': 'The username is eroor!'}
        return JsonResponse(result)
    user.avatar=request.FILES['avatar'] #request.FILES 获取用户上传文件
    user.save()
    return JsonResponse({'code':200,'username':username})








