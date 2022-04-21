from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    id_number = models.PositiveIntegerField(max_length=20)
    room = models.CharField(max_length=20)
    hall = models.CharField(max_length=100)
    complain1 = models.TextField(max_length=1000)
    complain2 = models.TextField(max_length=1000)
    complain3 = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)