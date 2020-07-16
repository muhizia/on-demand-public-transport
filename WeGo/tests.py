import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from WeGo.api.serializer import PassengerSerializer
from WeGo.models import Passenger

class PassengerCreateTest(APITestCase):

    def test_passenger(self):

        data = {"name" : "Pazo", "telephone" : "0728447917", "address" : "kigali kimironko","email" : "pazo@gmail.com", "password" : "thepazo"}
        response = self.client.post("/api/WeGo/passengers/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passenger.objects.get().name , "Pazo")

class PassengerUpdateTest(APITestCase):

    def test_passenger(self):

        data = {"name" : "Pazo", "telephone" : "0728447917", "address" : "kigali kimironko","email" : "pazo@gmail.com", "password" : "thepazo"}
        response = self.client.put("/api/WeGo/passengers/1", data)
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)


   
    
