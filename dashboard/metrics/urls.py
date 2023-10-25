from django.urls import path,include 
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'accesspoint_metrics',Accesspoint_metricsViewSet)
router.register(r'interface_metrics',Interface_metricsViewSet)
router.register(r'bss_metrics',Bss_metricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]