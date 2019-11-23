from django.http import HttpResponse

def index(requset):
    return HttpResponse('返回内容')