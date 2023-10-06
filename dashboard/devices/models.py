from django.db import models


# Create your models here.
class Devices(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
