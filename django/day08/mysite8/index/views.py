import csv
from django.core import mail

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from gevent import os

from mysite8 import settings
from .models import Book, Email_list


def mymiddle(request):
    print('---views start---')
    return HttpResponse('---views start---')
def book(request):
    #带分页的book列表页
    all_books=Book.objects.all()
    #初始化paginator对象
    paginator=Paginator(all_books,2)#从所有列表中规定每2个为一页

    #http://127.0.0.1:8000/index/book?page=1
    current_page=request.GET.get('page',1)
    page=paginator.page(current_page)
    return render(request,'index/book.html',locals())
def test_upload(request, setting=None):#上传文件
    if request.method=='GET':
        return render(request,'index/test_upload.html')
    elif request.method=='POST':
        myfile=request.FILES['myfile']#取出文件内容
        file_path=os.path.join(settings.MEDIA_ROOT,myfile.name)#拼接存放路径
        with open(file_path,'wb') as f:
            data=myfile.file.read()
            f.write(data)
        return HttpResponse('上传成功')


def book_csv(request):#生成csv文件 并响应给浏览器

    #http://127.0.0.1:8000/index/book_csv?page=1
    #1.改响应头中的Content_Type
    response=HttpResponse(content_type='text/csv')
    #2.响应头中添加特殊的 附件头
    response['Content-Disposition']='attachment;filename=book.csv'

    # 带分页的book列表页
    all_books = Book.objects.all()
    # 初始化paginator对象
    paginator = Paginator(all_books, 2)  # 从所有列表中规定每2个为一页

    # http://127.0.0.1:8000/index/book?page=1
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)

    #生成csv的写对象
    writer=csv.writer(response)
    #写数据
    writer.writerow(['id','title'])
    for book in page:
        writer.writerow([book.id,book.title])
    return response


def email(request):
    all_email=Email_list.objects.all()
    return render(request,'index/email_list.html',locals())#locals()把函数内部所有的\
                                                  # 局部变量以字典的形式打包存储
def email_list(request):
    if request.method=='GET':
        username=request.GET.get('name')
        id=request.GET.get('id')
        email=request.GET.get('email')

        return render(request,'index/send_email.html',locals())#locals()把函数内部所有的\
                                          # 局部变量以字典的形式打包存储
    
def send(request):
    if request.method == 'POST':
        text=request.POST.get('text')
        email=request.POST.get('email')
        print(text,email)
        mail.send_mail(
            subject='tyu',
            message='%s'%text,
            from_email='760343741@qq.com',
            recipient_list=[email],
        )
        return HttpResponseRedirect('/index/email')