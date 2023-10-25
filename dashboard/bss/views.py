from django.shortcuts import render
from .models import Bss
from rest_framework import viewsets
from .serializers import BssSerializer

# Create your views here.
class BssViewSet(viewsets.ModelViewSet):
    queryset = Bss.objects.all()
    serializer_class = BssSerializer