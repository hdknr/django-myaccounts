from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from . import defs


class MailAddress(defs.MailAddress):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Mail Address')
        verbose_name_plural = _('Mail Addresses')

    def __str__(self):
        return self.address
