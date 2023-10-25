from .models import Accesspoint
from rest_framework import serializers

class AccesspointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesspoint
        fields = '__all__'