from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import generics, status, views, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from .serializers import RegisterSerializer, UserSerializer, UserDetailSerializer

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.urls import reverse
import requests
import os

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

        # token = RefreshToken.for_user(user).access_token
    
        return Response(user_data, status = status.HTTP_201_CREATED)
    
    # def get(self, request):
    #     user = User.objects.all()
    #     serializer = RegisterSerializer(user)
    #     return Response(serializer.data)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.filter(roles = "psg")
    serializer_class = UserSerializer

@csrf_exempt   
def login_request(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserDetailSerializer(user)
            appl_user = 'WNklYpnuGRgMf4Pf4Gs639sRBbkdYzLoXLM3Djky'
            appl_pass = '3V3vRcrvLBuhxHJwFpwSUMCpDJ98c8xgPITmfiEh2pSpXwRYhAhEcXDZp0GW1ygudPawNIGUVLcJRNfdEMqIo9Oj5Yb7hThz7MFxhXzIDCRVqYNBYlWIUgy2g7sNea0d'
            print(appl_user, appl_pass)
            response = requests.post('http://127.0.0.1:8000/o/token/', data={"grant_type":"password", "username":username ,"password":password},  auth=(appl_user, appl_pass))
            json_response = response.json();
            edited_list = dict(serializer.data)
            edited_list.update(json_response)
            print(edited_list)
            return JsonResponse(edited_list, status=status.HTTP_200_OK)
            # return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({'error': 'Wrong username or password'}, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'GET':
        return JsonResponse({'error': 'No access to this data'}, status=status.HTTP_400_BAD_REQUEST)