from django.core.serializers import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from index.models import User
from django.http import HttpResponseRedirect

def register(request):#注册
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        uphone = request.POST.get('uphone')
        username = request.POST.get('username')        
        eamil = request.POST.get('eamil')
        password = request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            users = User.objects.filter(username=username)
            if users:
                return HttpResponse('用户名已存在')
            user=User.objects.create(uphone=uphone,username=username,password=password,eamil=eamil)
            return render(request,'login.html')
    return render(request,'logon.html')



def login(request):#登录
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        users = User.objects.get(username=username,password=password)
        if users:
            return render(request, 'index.html')
    return render(request, 'login.html')

def phone(request):
    uphone = request.GET.get('phone')
    user = User.objects.filter(uphone=uphone)
    if user:
        return JsonResponse({'i': False})
    return JsonResponse({'i': True})


def index(request):
    return render(request, 'index.html')

def check_login(requset):#检查登录状态
    #检查session,
    # 如果session没数据，则检查Cookie
    # 3-1 如果Cookie有，需要把Cookie数据回写给session
    # 3-2 如果Cookie没有，用户肯定没登录

    # 未登录返回结构
    # res = {'loginState':0}
    # 登录状态返回
    res = {'loginState': 1, 'username': 'guoxiaonao'}
    return JsonResponse(res)

def load_goods(requset):#加载商品
    all_list=[]
    all_types=GoodsType.objects.all()
    for _type in all_types:
        data={}
        data['type']={'title':_type.title}
        data['goods']=[]
        all_goods=_type.goods_set.filter(isActive=True)\
        .order_by('-created_time')[:10]
        for good in all_goods:
            d={}
            d['title']=good.title
            d['price']=str(good.price)
            d['spec']=good.spec
            d['pirture']=str(good.pirture)
            data['goods'].append(d)
        all_list.append(data)
    return HttpResponse(json.dumps(all_list),content_type='application/json')











def check_username(requset):#查询用户名
    username=requset.GET.get('username')
    users=User.objects.filter(username=username)
    if users:
        # return HttpResponse('用户名已注册')
        return HttpResponse('1')
    return HttpResponse('0')


    
def logon(request):#登录
    return render(request, 'logon.html')



def check_logging(fn):
    def wrap(request,*args,**kwargs):
        #检查当前用户是否登录
        #检查session
        if 'username' not in request.session or\
            'uid' not in request.session:
            #可能没登录
            # 检查cookie
            if 'username' not in request.COOKIES or \
                    'uid' not in request.COOKIES:
                return HttpResponseRedirect('/users/login')
            else:
                request.session['username']=request.COOKIES['username']
                request.session['uid'] = request.COOKIES['uid']
        return fn(request,*args,**kwargs)
    return wrap