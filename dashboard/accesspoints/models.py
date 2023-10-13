from django.db import models
import datetime


# Create your models here.
class AccessPoints(models.Model):
    OBJECTID = models.IntegerField(primary_key=True)
    Borough = models.CharField(max_length=2, null=True,default="null")
    Type = models.CharField(max_length=30, null=True,default="null")
    Provider = models.CharField(max_length=40, null=True,default="null")
    Remarks = models.CharField(max_length=100, default="null", null=True)
    SSID = models.CharField(max_length=25, default="null", null=True)
    Activated = models.DateField(null=True,default="null")
    Latitude = models.FloatField(null=True,default="null")
    Longitude = models.FloatField(null=True,default="null")