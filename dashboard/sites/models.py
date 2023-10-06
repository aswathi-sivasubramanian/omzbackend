from django.db import models


# Create your models here.
class Sites(models.Model):
    boro = models.CharField(max_length=2, null=True)
    area = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    x_coord = models.DecimalField(max_digits=9, decimal_places=8, null=True)
    y_coord = models.DecimalField(max_digits=9, decimal_places=8, null=True)
    location_type = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True)
    borocode = models.IntegerField(null=True)
    boroname = models.CharField(max_length=20, null=True)
    ntacode = models.IntegerField(null=True)
    nta = models.CharField(max_length=20, null=True)
    council_district = models.IntegerField(null=True)
    zipcode = models.IntegerField(null=True)
