from django.db import models

# Create your models here.

from datetime import timezone
import datetime
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=20)


class Contract(models.Model):
    name = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField(default="")
    provider = models.CharField(max_length=20)
    budget = models.PositiveBigIntegerField(default=0)
    duration = models.IntegerField(default=0)
    max_changes =models.BigIntegerField(default=0)