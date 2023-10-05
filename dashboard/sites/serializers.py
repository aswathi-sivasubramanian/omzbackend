from .models import Sites
from  rest_framework import serializers


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = '__all__'