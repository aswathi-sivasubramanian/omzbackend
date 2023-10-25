from .models import *
from rest_framework import serializers

class Accesspoint_metricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesspoint_metrics
        fields = '__all__'
        
class Interface_metricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface_metrics
        fields = '__all__'
        
class Bss_metricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bss_metrics
        fields = '__all__'