from django.conf.urls import url
from django.contrib import admin

from app4 import views

urlpatterns = [
    url(r'^img/',views.img),
    url(r'^(\d{4})/(\d{1,2})/(\d{1,2})', views.date),
    url(r'^count', views.count),

]