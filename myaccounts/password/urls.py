from django.urls import re_path, path, include
from myaccounts.utils import UIDB64, TOKEN
from . import views

# TODO: profile api: configurable

urlpatterns = [
    path('reset', views.reset_form, name="password/reset/form"),
    path('reset/accepted', views.reset_accepted, name="password/reset/accepted"),
    re_path(f'reset/confirm/{UIDB64}/{TOKEN}/$', views.reset_confirm, name="password/reset/confirm"),
    path('reset/complete', views.reset_complete, name="password/reset/complete"),
    path('change/complete', views.change_complete, name="password/change/complete"),
    path('change', views.change_form, name="password/change/form"),
]