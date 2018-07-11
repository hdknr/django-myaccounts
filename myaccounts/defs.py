from django.db import models


class MailAddress(models.Model):
    address = models.EmailField()
    is_verified = models.BooleanField(default=False)

    class Meta:
        abstract = True