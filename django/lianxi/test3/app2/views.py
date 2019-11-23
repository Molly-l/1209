from django.shortcuts import render

# Create your views here.
from app2.models import Book
from django.http import HttpResponse,HttpResponseRedirect

def add(request):
    if request.method=='GET':
        return render(request,'app2/add.html')

    title1=request.POST.get('book1')
    price1=request.POST.get('book2')
    Book.objects.create(title=title1,price=price1)
    return HttpResponse('ok')

def all(request):
    all=Book.objects.all()
    return render(request,'app2/all.html',locals())


def update(request,id):
    return render(request, 'app2/upd.html',locals())

def tiaozhuan(request,id):
    price1 = request.POST.get('price1')
    try:
        upd = Book.objects.get(id=id)

    except:
        return HttpResponse('错误')
    upd.price = price1
    upd.save()
    # all = Book.objects.all()
    # return render(request, 'app2/all.html',locals())
    return HttpResponseRedirect('/index/all')

def delete(request,id):

    try:
        upd = Book.objects.get(id=id)
        upd.delete()
    except:
        return HttpResponse('错误')

    return HttpResponseRedirect('/index/all')
