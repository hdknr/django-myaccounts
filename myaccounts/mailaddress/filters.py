'''
https://django-filter.readthedocs.io/en/master/
'''

import django_filters as filters
from myaccounts import models


class MailAddressFilter(filters.FilterSet):

    class Meta:
        model = models.MailAddress
        exclude = ['']