from django.db import models

# Create your models here.
class AccessPoints(models.Model):
    name = models.CharField(max_length=100)