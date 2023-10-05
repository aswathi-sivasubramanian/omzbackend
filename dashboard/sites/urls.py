from django.urls import path,include
# from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'sites', SitesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
