from django.shortcuts import render
from .models import Sites
from .serializers import SitesSerializer
from rest_framework import viewsets

# Create your views here.

class SitesViewSet(viewsets.ModelViewSet):
    queryset = Sites.objects.all()
    serializer_class = SitesSerializer

