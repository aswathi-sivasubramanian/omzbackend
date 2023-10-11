from django.http import HttpResponse, JsonResponse
import requests

def index(request):
    return HttpResponse("Hello Openmynz, please see API endpoints at /api/v1/(app_name)")

def get_accesspoints(request):
    api_url = "http://192.168.3.55:8080/api/v1/accesspoints/"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        geojson_data = {
            "type": "FeatureCollection",
            "features": []
        }  
        for accesspoint in data:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [accesspoint["Longitude"], accesspoint["Latitude"]]
                },
                "properties": {
                    "OBJECTID": accesspoint["OBJECTID"],
                    "Borough": accesspoint["Borough"],
                    "Provider": accesspoint["Provider"],
                    "Type": accesspoint["Type"],
                    "Activated": accesspoint["Activated"]
                }
            }
            geojson_data['features'].append(feature)
        return JsonResponse(geojson_data)
    else:
        return JsonResponse({'error': 'Failed to fetch accesspoints data'})