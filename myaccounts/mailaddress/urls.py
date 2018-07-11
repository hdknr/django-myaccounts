from django.urls import re_path, path, include
from myaccounts.utils import UIDB64, TOKEN
from . import views


urlpatterns = [
    path('verify', views.verify_form, name="mailaddress-verify-form"),
    path('verify/accepted', views.verify_accepted, name="mailaddress-verify-accepted"),
    re_path(f'verify/confirm/(?P<id>\d+)/{UIDB64}/{TOKEN}/$', 
            views.verify_confirm, name="mailaddress-verify-confirm"),
    path('verify/complete/<int:id>', views.reset_complete, name="mailaddress-verify-complete"),
]