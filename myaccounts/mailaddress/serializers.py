from django.db.models import Model
from rest_framework import serializers, fields

from myaccounts import models


class MailAddressSerializer(serializers.ModelSerializer):
    endpoint = serializers.HyperlinkedIdentityField(
        view_name='mailaddress-detail', read_only=True, source="id")

    class Meta:
        model = models.MailAddress
        fields = '__all__'