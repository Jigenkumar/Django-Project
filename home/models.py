from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=180)

class Review(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    msg = models.CharField(max_length=200)
    rate = models.CharField(max_length=20)
    satisfied = models.CharField(max_length=20)
    prices = models.CharField(max_length=20)
    support = models.CharField(max_length=20)
