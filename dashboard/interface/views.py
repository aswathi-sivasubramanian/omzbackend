from django.shortcuts import render

# Create your views here.
from .models import Interface
from .serializers import InterfaceSerializer
from rest_framework import viewsets

class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer