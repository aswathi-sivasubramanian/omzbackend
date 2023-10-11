from django.db import models


# Create your models here.
class Sites(models.Model):
    Borough = models.CharField(max_length=2, null=True,default="null")
    Name = models.CharField(max_length=50, null=True,default="null")
    Location = models.CharField(max_length=50, null=True,default="null")
    Latitude = models.FloatField(null=True,default="null")
    Longitude = models.FloatField(null=True,default="null")
    X = models.DecimalField(max_digits=20, decimal_places=5, null=True,default="null")
    Y = models.DecimalField(max_digits=20, decimal_places=5, null=True,default="null")
    Location_T = models.CharField(max_length=50, null=True,default="null")
    City = models.CharField(max_length=30, null=True,default="null")
    BoroCode = models.IntegerField(null=True,default="null")
    BoroName = models.CharField(max_length=20, null=True,default="null")
    NTACode = models.CharField(max_length=5,null=True,default="null")
    NTAName = models.CharField(max_length=40, null=True,default="null")
    CounDist = models.IntegerField(null=True,default="null")
    Postcode = models.IntegerField(null=True,default="null")
