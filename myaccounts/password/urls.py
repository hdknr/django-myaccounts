from django.urls import re_path, path, include
from . import views, UIDB64, TOKEN

# TODO: profile api: configurable

urlpatterns = [
    path('reset', views.reset_form, name="password-reset-form"),
    path('reset/accepted', views.reset_accepted, name="password-reset-accepted"),
    re_path(f'reset/confirm/{UIDB64}/{TOKEN}/$', views.reset_confirm, name="password-reset-confirm"),
    path('reset/complete', views.reset_complete, name="password-reset-complete"),
]