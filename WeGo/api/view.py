from rest_framework import status,viewsets, permissions,generics
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from WeGo.models import Passenger, Bus, Driver,Manager,RideRequest,BusStop,Route,Zone
from WeGo.api.serializer import (PassengerSerializer,
BusSerializer,DriverSerializer,ManagerSerializer,
RideRequestSerializer,BusStopSerializer,RouteSerializer,ZoneSerializer)






class ManagerView(viewsets.ModelViewSet):
    queryset         = Manager.objects.all()
    serializer_class = ManagerSerializer
    

class PassengerView(viewsets.ModelViewSet):
    queryset            = Passenger.objects.all()
    serializer_class   = PassengerSerializer
    
    

class DriverView(viewsets.ModelViewSet):
    queryset         = Driver.objects.all()
    serializer_class = DriverSerializer

class BusView(viewsets.ModelViewSet):
    queryset         = Bus.objects.all()
    serializer_class = BusSerializer

class RideRequestView(viewsets.ModelViewSet):
    queryset         = RideRequest.objects.all()
    serializer_class = RideRequestSerializer

class RouteView(viewsets.ModelViewSet):
    queryset      = Route.objects.all()
    serializer_class = RouteSerializer

class BusStopView(viewsets.ModelViewSet):
	queryset    = BusStop.objects.all()
	serializer_class = BusStopSerializer
	
class ZoneView(viewsets.ModelViewSet):
	queryset = Zone.objects.all()
	serializer_class = ZoneSerializer

class ZonesByRouteList(generics.ListAPIView):
	serializer_class = ZoneSerializer

	def get_queryset(self):

		route = self.kwargs['routes']
		return Zone.objects.filter(routes=route)

class BusStopsByZoneList(generics.ListAPIView):
	serializer_class = BusStopSerializer

	def get_queryset(self):
		zone = self.kwargs['zones']
		return BusStop.objects.filter(zones=zone)


