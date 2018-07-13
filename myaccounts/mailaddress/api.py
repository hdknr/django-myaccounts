from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()
router.register(r'mailaddress',
                viewsets.MailAddressViewSet, base_name='mailaddress')

urlpatterns = [
    path(r'', include(router.urls)),
]
