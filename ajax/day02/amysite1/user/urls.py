from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
   
    url(r'^register$', views.register),
    url(r'^check_username$', views.check_username),
    # url(r'^get_xhr_server/', views.get_xhr_server),
   

]