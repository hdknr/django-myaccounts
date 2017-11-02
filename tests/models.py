from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
