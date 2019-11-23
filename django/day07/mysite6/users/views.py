from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from users.models import User


def reg(request):#注册
    if request.method=='GET':
        return render(request,'users/register.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        if not username:
            return HttpResponse('输入用户名')

        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if not password or not password1:
            return HttpResponse('输入密码')

        old_users=User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户已存在')
        try:
            user=User.objects.create(username=username,password=password)
        except Exception as e:
            print('reg error')
            return HttpResponse('用户已存在')
        resp=HttpResponse('注册成功')
        resp.set_cookie('username',username,60*60*24)
        resp.set_cookie('uid',user.id,60*60*24)
        return resp


    return HttpResponse('ok')


def login_view(requste):#登录
    if requste.method=='GET':   # 2
        if 'username' in requste.session and 'uid'\
            in requste.session:
            return HttpResponseRedirect('/user/index')
        if 'username' in requste.COOKIES and 'uid'\
            in requste.COOKIES:
            requste.session['username']=requste.COOKIES \
                ['username']
            requste.session['uid'] = requste.COOKIES \
                ['uid']
            return HttpResponseRedirect('/user/index') # 3  302重定向
            
        return render(requste,'users/login.html')
    elif requste.method=='POST':
        save_cookies=False
        if 'save_cookies' in requste.POST.keys():
            save_cookies=True

        username=requste.POST.get('username')#从浏览器的POST提交请求中获取
        if not username:
            dic={'msg':'提交用户名'}
            return render(requste,'users/login.html',dic)
        password=requste.POST.get('password')
        if not password:
            dic={'msg':'提交密码'}
            return render(requste,'users/login.html',dic)

        user=User.objects.filter(username=username)#从数据库查找跟从浏览器中一样的，获取的是一个对象列表
        if not user:
            dic={'msg':'用户名不存在'}
            return render(requste,'users/login.html',dic)
        if user[0].password !=password: #数据库中的密码跟浏览器输入的
            dic={'msg':'用户名或密码错误'}
            return render(requste, 'users/login.html', dic)
        requste.session['username']=username #设置一个session, 作用：存到服务器中
        requste.session['uid']=user[0].id

        resp=HttpResponseRedirect('/users/index') #创建一个response对象
        if save_cookies:
            resp.set_cookie('username',username,60*60*24*30)#设置一个cookie, 作用：存到浏览器中
            resp.set_cookie('uid',user[0].id,60*60*24*30)
        return resp
def index(request): # 首页  5
    if 'username' in request.session and 'uid' in request.session:
        username=request.session.get('username')
        is_login=True
    else:
        is_login=False
    return render(request, 'users/index.html',locals())

def logout_view(request):# 退出
    if 'username' in request.session and 'uid' in request.session:
        del request.session['username']
        del request.session['uid']
    resp=HttpResponseRedirect('/users/index')
    if 'username' in request.COOKIES and 'uid' \
            in request.COOKIES:
        resp.delete_cookie('username')
        resp.delete_cookie('uid')
    return resp
