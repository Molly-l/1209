from django.conf.urls import url, include
from django.contrib import admin

from ajax import views

urlpatterns = [
    
    url(r'^rest_load/$', views.rest_load),
    url(r'^rest_load_server/$', views.rest_load_server),

]