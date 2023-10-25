from django.urls import path,include 
from rest_framework.routers import DefaultRouter

from .views import BssViewSet

router = DefaultRouter()
router.register(r'bss',BssViewSet)

urlpatterns = [
    path('',include(router.urls)),
]