from django.utils.functional import cached_property
from collections import OrderedDict
from rest_framework import (
    permissions, viewsets, pagination, response, decorators)
from . import serializers, filters
from myaccounts import models, paginations


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        # TODO
        return True


class BaseViewSet(viewsets.ModelViewSet):
    pagination_class = paginations.Pagination
    permission_classes = [UserPermission, ]
    USER_QUERY = []         # Relation

    def get_queryset(self):
        '''override: only owndata'''
        qs = super(BaseViewSet, self).get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return qs

            if self.USER_QUERY:
                query = '__'.join(self.USER_QUERY + ['user'])
            else:
                query = 'user'
            return self.request.user.is_superuser and qs \
                or qs.filter(**{query: self.request.user}) # NOQA

        return qs.none()


class MailAddressViewSet(BaseViewSet):
    queryset = models.MailAddress.objects.all()
    serializer_class = serializers.MailAddressSerializer
    filter_class = filters.MailAddressFilter