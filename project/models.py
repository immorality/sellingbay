from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
    index = models.CharField(max_length=24, unique=True)
    description = models.CharField(max_length=48)
    amount = models.IntegerField()
    price = models.FloatField()
