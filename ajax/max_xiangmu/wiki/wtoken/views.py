import datetime
import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
from user.models import UserProfile

# Create your views here.
def tokens(request):#登录

    if request.method != 'POST':
        result = {'code': 20101, 'error':'Please use POST'}
        return JsonResponse(result)
    else:
        json_str = request.body
        #TODO 检查参数是否存在
        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        password = json_obj.get('password')
        #找用户
        users = UserProfile.objects.filter(username=username)
        if not users:
            result = {'code':20102, 'error':'The username or password is error!'}
            return JsonResponse(result)
        user = users[0]
    
        pm = hashlib.md5()
        pm.update(password.encode())
        if user.password != pm.hexdigest():#数据库中存储的密码的散列值，获取的密码的散列值
            result = {'code': 20103, 'error':'The username or password is error!!'}
            return JsonResponse(result)

        now_datetime=datetime.datetime.now()

        user.login_time=now_datetime
        user.save()

        #生成token
        token = make_token(username, 3600*24,now_datetime)
        result = {'code':200, 'username':username, 'data':{'token':token.decode()}}
        return JsonResponse(result)


def make_token(username, exp,now_datetime): #exp :token的有效期
    #生成token
    key = '1234567ab'
    now_t = time.time() #当前时间
    payload = {'username':username, 'exp':int(now_t+exp),'login_time':str(now_datetime)} #消息主体
    return jwt.encode(payload, key, algorithm='HS256') #加密