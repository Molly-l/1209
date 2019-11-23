from django.core import mail
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from email01.models import EmailList


def email_list(request):
    all_email=EmailList.objects.all()
    return render(request,'email01/email_list.html',locals())

def send(request):
    if request.method=='GET':
        id=request.GET.get('id')
        username = request.GET.get('name')
        email = request.GET.get('email')
        return render(request,'email01/send.html',locals())
def send_email(request):
    print(request.method)
    if request.method=='GET':
        return render(request,'email01/send.html')
    elif request.method=='POST':
        id=request.POST.get('id')
        text=request.POST.get('text')
        email=request.POST.get('email')
        try:
            EmailList.objects.get(id=id,adress=email)
        except:
            return HttpResponse('erro')
        else:
            mail.send_mail(
                subject='tyu',
                message='%s' % text,
                from_email='760343741@qq.com',
                recipient_list=[email],
            )
            print(55555)
            return HttpResponseRedirect('/index/email_list/')
            # return render(request,'email01/email_list.html')
        
            

