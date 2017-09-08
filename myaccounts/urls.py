# coding: utf-8
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^social/',
        include('social.apps.django_app.urls', namespace='social')),
    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
]
