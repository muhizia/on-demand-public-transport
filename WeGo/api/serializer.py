from rest_framework import serializers

from WeGo.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Passenger
        fields = ['id','name',
        'address','telephone','email',]
    
   
