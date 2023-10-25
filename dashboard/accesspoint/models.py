from django.db import models

# Create your models here.
class Accesspoint(models.Model):
    ap_id = models.IntegerField(primary_key=True)
    borough = models.CharField(max_length=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=20)