from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'accesspoint', AccesspointViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('geojson_accesspoint',geojson_accesspoint),
]