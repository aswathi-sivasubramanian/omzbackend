from django.urls import path,include

from .views import *

urlpatterns = [
    path('get_sites',view=get_sites, name='get_sites')
]
