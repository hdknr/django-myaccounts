from django.urls import path, include
from . import views, api

# TODO: profile api: configurable

urlpatterns = [
    path('social/', include('social.apps.django_app.urls', namespace='social')),
    path('oauth2/api/profile', api.profile, name="api_profile"),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]