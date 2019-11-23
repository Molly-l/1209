from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^reg/',views.reg),
    # url(r'', views.get_cookies)
    url(r'^login$', views.login_view), # 1
    url(r'^index$', views.index),  #  4
    url(r'^logout$', views.logout_view),

]