from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import generics, status, views, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from .serializers import RegisterSerializer, UserSerializer



from rest_framework import permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# take url and give us a path
from django.urls import reverse

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    def post(self, request):
        user = request.data
        serializer =  self.serializer_class(data = user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        user_data = serializer.data
         # to provide a token to the user, it gives two token one for refresh and add for access
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token
    
        return Response(user_data, status = status.HTTP_201_CREATED)
    
    def get(self, request):
        user = User.objects.all()
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.filter(roles = "psg")
    serializer_class = UserSerializer