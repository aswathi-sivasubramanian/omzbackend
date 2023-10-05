from django.db import models

# Create your models here.
class Sites(models.Model):
    boro = models.CharField(max_length=2)
    area = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    x_coord = models.DecimalField(max_digits=9, decimal_places=8)
    y_coord = models.DecimalField(max_digits=9, decimal_places=8)
    location_type = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    borocode = models.IntegerField()
    boroname = models.CharField(max_length=20)
    ntacode = models.IntegerField()
    nta = models.CharField(max_length=20)
    council_district = models.IntegerField()
    zipcode = models.IntegerField()