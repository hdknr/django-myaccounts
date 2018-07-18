from django.urls import re_path, path, include
from . import views, api

# TODO: profile api: configurable

urlpatterns = [
    path('signup/', include('myaccounts.signup.urls')),
    path('password/', include('myaccounts.password.urls')),
    path('mailaddress/', include('myaccounts.mailaddress.urls')),
    path('social/', include('social.apps.django_app.urls', namespace='social')),
    path('oauth2/api/profile', api.profile, name="api_profile"),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path('^login', views.login, name="login"),
    re_path('^logout', views.logout, name="logout"),
]