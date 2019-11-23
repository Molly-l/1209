from django.shortcuts import render
from django.http import HttpResponse

def test_xhr(request):
    return render(request,'test_xhr.html')
def get_xhr(request):
    return render(request,'get_xhr.html')
def get_xhr_server(request):
    return HttpResponse('get_xhr_server.html')