from django.urls import path,include
from rest_framework import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
