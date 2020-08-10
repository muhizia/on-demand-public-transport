from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import generics, status, views, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from .serializers import UserSerializer



from rest_framework import permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# take url and give us a path
from django.urls import reverse



    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.filter(roles = "psg")
    serializer_class = UserSerializer