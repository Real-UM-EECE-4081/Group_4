from django.db import models

class Metric(models.Model):
    # The name of the metric
    name = models.CharField(max_length=100)
    # The value of the metric, stored as a float
    value = models.FloatField()
    # Automatically stores the timestamp of the last update
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# group4/models.py
from django.db import models

class Metric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
from django.db import models

class Metric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

