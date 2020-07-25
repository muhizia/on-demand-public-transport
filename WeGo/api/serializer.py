from rest_framework import serializers

from WeGo.models import Passenger,Route
from WeGo.models import Driver, Bus,Manager,RideRequest,BusStop
from django.contrib.auth.models import User





class ManagerSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Manager
        fields = ('firstName','lastName','userName',
        'address','telephone','email','password','passwordConfirm','profilePicture','roles')
        extra_kwargs = {
            'password': {'write_only':True},
            'roles'    : {'read_only':True}
        }
    



class PassengerSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Passenger
        fields = ('firstName','lastName','userName',
        'address','telephone','email','password','passwordConfirm','profilePicture','roles')
        extra_kwargs = {
            'password': {'write_only':True},
            'roles'   : {'read_only':True}
        }

class DriverSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Driver
        fields = ('firstName','lastName','userName',
        'address','telephone','email','password','passwordConfirm','profilePicture','roles')
        extra_kwargs = {
            'password': {'write_only':True},
            'roles'   : {'read_only':True}
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

class BusStopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusStop
        fields = ('id','routes','busStopName')
class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ('id','name')



