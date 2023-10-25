from django.shortcuts import render
from .models import Accesspoint
from .serializers import *
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.
class AccesspointViewSet(viewsets.ModelViewSet):
    queryset = Accesspoint.objects.all().order_by('ap_id')
    serializer_class = AccesspointSerializer
    
def geojson_accesspoint(request):
    features = []
    accesspoints = Accesspoint.objects.all()
    for accesspoint in accesspoints:
        feature = {
            "type" : "Feature",
            "geometry" : {
                "type" : "Point",
                "coordinates" : [accesspoint.longitude, accesspoint.latitude]
            },
            "properties" : {
                "ap_id" : accesspoint.ap_id,
                "borough" : accesspoint.borough,
                "location" : accesspoint.location,
                "status" : accesspoint.status,
            }
        }
        features.append(feature)
    geojson_data = {
        "type" : "FeatureCollection",
        "features" : features
    }
    return JsonResponse(geojson_data, safe=False)