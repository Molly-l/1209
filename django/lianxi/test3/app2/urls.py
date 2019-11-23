from django.conf.urls import url, include
from django.contrib import admin

from app2 import views

urlpatterns = [
    
    url(r'^add',views.add),
    url(r'^all', views.all),
    url(r'^update/(?P<id>\d+)', views.update),
    url(r'^tiaozhuan/(?P<id>\d+)', views.tiaozhuan),

    url(r'^delete/(?P<id>\d+)', views.delete),

]