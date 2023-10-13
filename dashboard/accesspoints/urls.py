from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'accesspoints', AccessPointsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('geojson_accesspoints',geojson_accesspoints),
]
