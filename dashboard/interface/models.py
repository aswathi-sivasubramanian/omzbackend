from django.db import models
from accesspoint.models import Accesspoint
from bss.models import Bss

# Create your models here.
class Interface(models.Model):
    interface_id = models.IntegerField(primary_key=True)
    interface_name = models.CharField(max_length=20)
    interface_type = models.CharField(max_length=20)
    ap_id = models.ForeignKey(Accesspoint, on_delete=models.CASCADE)
    bss_id = models.ForeignKey(Bss, on_delete=models.CASCADE)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_errors = models.IntegerField()
    rx_errors = models.IntegerField()