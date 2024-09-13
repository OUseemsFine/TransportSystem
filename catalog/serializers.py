from rest_framework import serializers

from .models import Station, Busline, StationSequence, VehicleInstance, Vehicle
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
        
#Station Sequence:
class StationSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationSequence
        fields = ['id', 'station', 'busline', 'order']
        
class StationDataSerializer(serializers.Serializer):
    """Serializer for updating station sequences."""
    station_id = serializers.IntegerField()
    order = serializers.IntegerField()
    
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
    
class VehicleInstanceSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    busline = BuslineSerializer(allow_null=True)
    class Meta:
        model = VehicleInstance
        fields = '__all__'
        

class VehicleInstanceAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInstance
        fields = '__all__'  
        

class VehicleInstanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInstance
        fields = ['busline', 'status']  
        