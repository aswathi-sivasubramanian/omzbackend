from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Openmynz, please see API endpoints at /api/v1/(app_name)")

