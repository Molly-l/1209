from django.http import HttpResponse
from django.shortcuts import render


# def shebao(request)


def test_url(request):
    return render(request,'test_url.html')

def page_view(request):
    return HttpResponse('test_url.html')

def test_static(request):
    #测试静态文件加载
    return render(request,'test_static.html')
