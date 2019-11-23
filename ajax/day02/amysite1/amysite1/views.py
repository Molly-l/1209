from django.shortcuts import render
from django.http import HttpResponse

def test_xhr(request):
    return render(request,'test_xhr.html')
def get_xhr(request):
    return render(request,'get_xhr.html')
def get_xhr_server(request):
    print(11111111111111111111)

    if 'param' in request.GET.keys():
        # param=request.GET['param']
        param=request.GET.get('param')

        
        print(11111111111111111111,param)
        html='%s'%param
        return HttpResponse(param)
    return HttpResponse('get_xhr_server.html')
def post_xhr(request):
    return render(request,'post_xhr.html')
def post_xhr_server(request):
    return HttpResponse('ok')