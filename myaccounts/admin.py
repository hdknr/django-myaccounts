from django.contrib import admin
from myaccounts import models


@admin.register(models.MailAddress)
class MailAddressAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.MailAddress._meta.fields]
    raw_id_fields = ['user']