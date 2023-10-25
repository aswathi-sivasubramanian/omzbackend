from django.db import models
from accesspoint.models import Accesspoint
from interface.models import Interface
from bss.models import Bss

# Create your models here.
class Accesspoint_metrics(models.Model):
    ap_id = models.ForeignKey(Accesspoint, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    backhaul_utilisation = models.FloatField()
    total_clients = models.IntegerField()
    
class Interface_metrics(models.Model):
    interface_id = models.ForeignKey(Interface, on_delete=models.CASCADE)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_fail =  models.IntegerField()
    rx_fail = models.IntegerField()
    tx_retry = models.IntegerField()
    rx_retry = models.IntegerField()
    
class Bss_metrics(models.Model):
    bss_id = models.ForeignKey(Bss, on_delete=models.CASCADE)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_drop = models.IntegerField()
    rx_drop = models.IntegerField()