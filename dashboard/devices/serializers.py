from .models import Devices
from  rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'