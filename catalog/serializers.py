from rest_framework import serializers

from .models import Station
class StationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['sName', 'latitude', 'longitude']

class StationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'sName', 'status', 'latitude', 'longitude']  