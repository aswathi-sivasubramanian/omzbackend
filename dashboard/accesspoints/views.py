from django.shortcuts import render
from .models import AccessPoints
from .serializers import AccessPointsSerializer
from rest_framework import viewsets

# Create your views here.

class AccessPointsViewSet(viewsets.ModelViewSet):
    queryset = AccessPoints.objects.all()
    serializer_class = AccessPointsSerializer
