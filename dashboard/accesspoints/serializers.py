from .models import AccessPoints
from  rest_framework import serializers


class AccessPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPoints
        fields = '__all__'