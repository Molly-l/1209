from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from  .models import BookStore,Book

# Create your views here.
def add_book(request):

    if request.method=='GET':
        return render(request,'bookstore/add_book.html')
    elif request.method=='POST':
        title=request.POST.get('title')
        if not title:
            return HttpResponse('数据有误，请退回重新填写')
        pub=request.POST.get('pub')
        price=request.POST.get('price')
        market_price=request.POST.get('m_price')
        #创建数据
        Book.objects.create(title=title,pub=pub,price=price,\
                            market_price=market_price)

        return HttpResponse('添加成功')
def all_book(request):
    all_book=Book.objects.all()
    # l_b=[]
    # for book in all_book:
    #     d={}
    #     d['title']=book.title
    #     d['price']=book.price
    #     d['market_price']=book.market_price
    #     d['pub']=book.pub
    #

        # l_b.append(d)
    return render(request,'bookstore/all_book.html',locals())

def detail(request,book_id):
    #书籍的详情页面
    try:
        book=Book.objects.get(id=book_id)
    except Exception('查询有误'):
        pass

    return render(request,'bookstore/detail.html',locals())

def update_book(request,book_id):
    books=Book.objects.filter(id=book_id)
    if not books:
        return HttpResponse('查询有误')
    if request.method!='POST':
        return HttpResponse('异常')
    market_price=request.POST.get('m_price')
    book=books[0]
    book.market_price=market_price
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request, book_id):
    # 书籍的详情页面
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
    except Exception as e:
        return HttpResponse('查询有误')
    return HttpResponseRedirect('/bookstore/all_book')


    # return render(request,'bookstore/detail.html',locals())