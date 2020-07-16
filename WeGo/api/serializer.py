from rest_framework import serializers

from WeGo.models import Passenger
from WeGo.models import Driver, Bus,Manager,RideRequest



class ManagerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Manager
        fields = ('id','name',
        'address','telephone','email','password')

class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Passenger
        fields = ('id','name',
        'address','telephone','email','password')
    

class DriverSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Driver
        fields = ('id','name', 'address','telephone','email','password')



class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ('id','plateNumber','available','driver','issuingDate')

class RideRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideRequest
        fields = ('id','pickupTime','departureCity','destinationCity',
        'passengers')



