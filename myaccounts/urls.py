# coding: utf-8
from django.conf.urls import url, include
from . import views, api


# TODO: profile api: configurable

urlpatterns = [
    url(r'^social/',
        include('social.apps.django_app.urls', namespace='social')),
    url(r'^oauth2/api/profile', api.profile, name="api_profile"),
    url(r'^oauth2/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
]
