from django.conf.urls import url

from . import views

urlpatterns = [
   
    url(r'^home/$', views.Home, name='home'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
]