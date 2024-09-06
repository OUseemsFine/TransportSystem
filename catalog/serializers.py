from rest_framework import serializers

from .models import Station, Busline
#Station:
class StationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['sName', 'latitude', 'longitude']

class StationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'sName', 'status', 'latitude', 'longitude']  


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['sName', 'status', 'latitude', 'longitude']
        
#Busline:
class BuslineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busline
        fields = '__all__'
        
