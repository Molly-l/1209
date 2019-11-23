from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logon$', views.logon),
    url(r'^index$', views.index),
    url(r'^phone$', views.phone),
    url(r'^check_login$', views.check_login),
    url(r'^load_goods$', views.load_goods),

]