from django.shortcuts import render
from .models import Book
from django.http import  HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    Book.objects.create(title='书名1',price=60)
    return HttpResponse('OK')