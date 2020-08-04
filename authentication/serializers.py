from  rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68 , min_length= 6, write_only= True)
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname','email', 'username', 'password']
    
    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric character')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname','email', 'telephone', 'username', 'password', 'roles', 'is_active', 'is_staff']
        extra_kwargs = {
            'roles'    : {'read_only':True},
            'is_active'    : {'read_only':True},
            'is_staff'    : {'read_only':True},
        }