from  rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


   
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname','email', 'telephone', 'username', 'password', 'roles', 'is_active', 'is_staff']
        extra_kwargs = {
            'roles'    : {'read_only':True},
            'is_active'    : {'read_only':True},
            'is_staff'    : {'read_only':True},
        }