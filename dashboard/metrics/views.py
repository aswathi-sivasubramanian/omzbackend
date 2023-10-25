from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets

class Accesspoint_metricsViewSet(viewsets.ModelViewSet):
    queryset = Accesspoint_metrics.objects.all()
    serializer_class = Accesspoint_metricsSerializer
    
class Interface_metricsViewSet(viewsets.ModelViewSet):
    queryset = Interface_metrics.objects.all()
    serializer_class = Interface_metricsSerializer
    
class Bss_metricsViewSet(viewsets.ModelViewSet):
    queryset = Bss_metrics.objects.all()
    serializer_class = Bss_metricsSerializer