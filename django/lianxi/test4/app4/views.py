from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def img(request):
    return render(request,'app4/fgh.html')
def date(request,y,m,d):
    print('***',y,m,d)
    html='生日为:%s年%s月%s日'%(y,m,d)
    return HttpResponse(html)
def count(request):
    if request.method=='GET':
        return render(request,'app4/count.html')
    elif request.method=='POST':

        num1=float(request.POST.get('num1'))
        op=request.POST.get('op')
        num2=float(request.POST.get('num2'))
        num3=0
        if op=='add':
            num3=num1+num2
        elif op=='sub':
            num3=num1-num2
        elif op=='mul':
            num3=num1*num2
        else:
            num3=num1/num2
        dict1={'num1':num1,'num2':num2,'num3':num3,'op1':op}
        return render(request,'app4/count.html',dict1)
