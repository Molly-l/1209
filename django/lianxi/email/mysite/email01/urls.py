from django.conf.urls import url, include
from django.contrib import admin

from email01 import views

urlpatterns = [
    
    url(r'^email_list/', views.email_list),
    url(r'^send/$', views.send),
    url(r'^send_email/', views.send_email),

]
