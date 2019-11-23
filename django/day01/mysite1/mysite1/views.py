from django.http import HttpResponse

post_html="""
<form method='post' action="/page2">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>
"""

def page1_view(request):
    print(111)
    print(request.GET.get('a'))
    print(222)
    print(request.GET.getlist('a'))
    print(333)
    print(dict(request.GET))

    html='<h1>11</h1>'
    return HttpResponse(post_html)

def page2_view(request):
    #post取值
    if request.method=='POST':
        print('my post username is')
        print(request.POST.get('username'))

    html='<h1>22</h1>'
    return HttpResponse(html)
def index(request):
    html='<h1>22</h1>'
    return HttpResponse(html)
# def pagen_view(request,n,m):
#     html='%s%s'%n,m
#     return HttpResponse(html)

def pagen_view(request,n,i,m):
    if i not in ('add','sub','mul'):
        return HttpResponse('sorry')
    elif i=='add':
        html='%s'%(int(n)+int(m))
    elif i=='sub':
        html='%s'%(int(n)-int(m))
    else:
        html = '%s' % (int(n) * int(m))
    return HttpResponse(html)

def person_view(request,name,age):
    res='姓名：'+name
    res+='年龄:'+age
    return HttpResponse(res)
def daytime_view(request,year,mounth,day):
    res='%s年%s月%s日'%(year,mounth,day)
    return HttpResponse(res)