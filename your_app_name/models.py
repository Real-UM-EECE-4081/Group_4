# models.py

from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.value}"


# Create your models here.
