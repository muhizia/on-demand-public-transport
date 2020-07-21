from rest_framework import serializers

from WeGo.models import Passenger
from WeGo.models import Driver, Bus,Manager,RideRequest



class ManagerSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Manager
        fields = ('id','name',
        'address','telephone','email','password','passwordConfirm')
        extra_kwargs = {
            'password': {'write_only':True}
        }
    


class PassengerSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Passenger
        fields = ('id','name',
        'address','telephone','email','password','passwordConfirm')
        extra_kwargs = {
            'password': {'write_only':True}
        }

class DriverSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Driver
        fields = ('id','name', 'address','telephone','email','password','passwordConfirm')
        extra_kwargs = {
            'password': {'write_only':True}
        }


class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ('id','plateNumber','available','driver','issuingDate')

class RideRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RideRequest
        fields = ('id','pickupTime','departureCity','departureLocation','destinationCity','destinationLocation',
        'numberOfSeets','disabledPoeple','passengers')



