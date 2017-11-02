from django.conf.urls import url
from myaccounts import api


urlpatterns = [
    url("^profile", api.profile, name="profile"),
]
