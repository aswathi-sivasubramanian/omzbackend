from django.db import models
import datetime


# Create your models here.
class AccessPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30, null=True)
    provider = models.CharField(max_length=40, null=True)
    remarks = models.CharField(max_length=100, default="null", null=True)
    ssid = models.CharField(max_length=25, default="null", null=True)
    activated = models.DateField(null=True)
