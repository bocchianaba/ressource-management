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
