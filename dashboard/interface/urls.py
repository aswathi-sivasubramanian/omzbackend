from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import InterfaceViewSet

router = DefaultRouter()
router.register(r'interface',InterfaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]