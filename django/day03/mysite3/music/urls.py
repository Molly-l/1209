from django.conf.urls import url
from . import views

#file:music/urls.py
urlpatterns=[
    #http://127.0.0.1:8000/sports/index
    url(r'^index$',views.index)



]