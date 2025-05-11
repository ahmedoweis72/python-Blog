from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name
