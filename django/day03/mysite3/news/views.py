from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#file:sports/views.py

def index(request):
    return HttpResponse('新闻')

