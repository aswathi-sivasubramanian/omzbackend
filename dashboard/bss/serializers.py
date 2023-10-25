from .models import Bss
from rest_framework import serializers

class BssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bss
        fields = '__all__'