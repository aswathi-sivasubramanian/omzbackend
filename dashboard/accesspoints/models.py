from django.db import models

# Create your models here.
class AccessPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    provider = models.CharField(max_length=40)
    remarks = models.CharField(max_length=100)
    ssid = models.CharField(max_length=25)
    activated =models.DateTimeField()
    