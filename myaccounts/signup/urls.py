from django.urls import re_path, path, include
from myaccounts.utils import UIDB64, TOKEN
from . import views


urlpatterns = [
    re_path(f'activate/{UIDB64}/{TOKEN}/$', 
            views.activate, name="accounts/signup/activate"),
]