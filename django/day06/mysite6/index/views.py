from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookies(request):
    resp= HttpResponse('ok')
    resp.set_cookie('username','guoxiao',60*2)
    return resp
def get_cookies(request):
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