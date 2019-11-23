"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from mysite3 import views
#file:mysite3/urls.py 主路由

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^shebao', views.shebao),
    url(r'^test_url', views.test_url),
    url(r'^page$', views.page_view,name='pp'),
    url(r'^page(\d+)', views.page_view, name='pn'),
    url(r'^test_static', views.test_static),
    #http://127.0.0.1:8000/sports/xxx/xxx/xxx
    url(r'^sports/', include('sports.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^news/', include('news.urls')),

]
