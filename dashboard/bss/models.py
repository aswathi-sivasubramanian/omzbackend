from django.db import models

# Create your models here.
class Bss(models.Model):
    bss_id = models.IntegerField(primary_key=True)
    ssid_name = models.CharField(max_length=20)
    passphrase = models.CharField(max_length=20)
    security_mode = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    num_clients = models.IntegerField()
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_errors = models.IntegerField()
    rx_errors = models.IntegerField()