from rest_framework import serializers

from WeGo.models import Passenger,Route
from WeGo.models import Driver, Bus,Manager,RideRequest,BusStop,Zone
from django.contrib.auth.models import User




class ManagerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Manager
        fields = ('id','firstName','lastName',
        'address','telephone','profilePicture','roles')
        extra_kwargs = {
            'roles'    : {'read_only':True},
        }
    



class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('id','firstName','lastName',
        'address','telephone','profilePicture','roles')
        extra_kwargs = {
            'roles'    : {'read_only':True},
        }

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id','firstName','lastName',
        'address','telephone','profilePicture','roles')
        extra_kwargs = {
            'roles'    : {'read_only':True},
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


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ('id','name')

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone
        fields = ('id','routes','zoneName')
    
class BusStopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusStop
        fields = ('id','zones','busStopName')


