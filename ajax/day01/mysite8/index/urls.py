from django.conf.urls import url
from index import views

urlpatterns=[

    url(r'^mymiddles$',views.mymiddle),
    url(r'^book$', views.book),
    url(r'^test_upload$', views.test_upload),
    url(r'^book_csv$', views.book_csv),
    url(r'^email_list$', views.email_list),
    url(r'^email$', views.email),
    url(r'^send$', views.send),

]