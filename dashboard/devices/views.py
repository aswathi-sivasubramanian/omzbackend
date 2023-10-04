from django.shortcuts import render
from .models import Devices
from .serializers import DeviceSerializer
from rest_framework import viewsets

# Create your views here.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DeviceSerializer




