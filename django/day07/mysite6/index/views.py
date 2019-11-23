from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookies(request):#设置cookies
    resp= HttpResponse('ok')
    resp.set_cookie('username','guoxiao',60*2)
    return resp
def get_cookies(request):#获取
    username=request.COOKIES.get('username')
    if username:
        html='欢迎～ %s'%(username)
    else:
        html='登录'
    return HttpResponse(html)

def set_session(request):
    request.session['username']='123321'
    return HttpResponse('set is ok')

def get_session(request):
    username=request.session.get('username')
    html='session 获取到 %s'%(username)
    return HttpResponse(html)

def test_cache(request):#设置缓冲（模板缓冲：只对部分缓存）
    import time
    t1=time.time()
    return render(request,'index/test_cache.html',locals())

def test_csrf(request):#
    if request.method=='GET':
        return render(request,'index/test_cache.html')
    elif request.method=='POST':
        return HttpResponse('提交成功')