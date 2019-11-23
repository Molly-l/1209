from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User
from django.core import serializers


    
def check_username(requset):#查询用户名
    username=requset.GET.get('username')
    users=User.objects.filter(username=username)
    if users:
        # return HttpResponse('用户名已注册')
        return HttpResponse('1')
    return HttpResponse('0')
def register(request):#注册
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        users = User.objects.filter(username=username)
        if users:
            return HttpResponse('用户名已存在')
        user=User.objects.create(username=username,pwd=pwd)
        return HttpResponse('注册成功')


def get_user_server(request):
    #返回用户表数据
    all_users = User.objects.all()
    all_users_list = []
    for user in all_users:
        all_users_list.append(user.to_dict())
    import json
    res = json.dumps(all_users_list)
    return HttpResponse(res,content_type='application/json')



def get_user_server(request):
    all_users=User.objcts.all()
    res=serializers.serialize('json',all_users)




    return HttpResponse(res,content_type='application/json')
