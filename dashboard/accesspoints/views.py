from django.shortcuts import render
from .models import AccessPoints
from .serializers import *
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.

class AccessPointsViewSet(viewsets.ModelViewSet):
    queryset = AccessPoints.objects.all()
    serializer_class = AccessPointsSerializer
    

def geojson_accesspoints(request):
    features = []

    access_points = AccessPoints.objects.all()

    for access_point in access_points:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [access_point.Latitude, access_point.Longitude]
            },
            "properties": {
                "OBJECTID": access_point.OBJECTID,
                "Borough": access_point.Borough,
                "Provider": access_point.Provider,
                "Type": access_point.Type,
                "Activated": access_point.Activated.strftime("%Y-%m-%d") if access_point.Activated else None
            }
        }

        features.append(feature)

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson_data, safe=False)