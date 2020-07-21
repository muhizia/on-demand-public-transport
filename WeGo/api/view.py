from rest_framework import status,viewsets, permissions
from rest_framework.response import Response 
from rest_framework.decorators import api_view


from WeGo.models import Passenger, Bus, Driver,Manager,RideRequest
from WeGo.api.serializer import (PassengerSerializer,
BusSerializer,DriverSerializer,ManagerSerializer,RideRequestSerializer)







"""
# view one passenger
@api_view(['GET', ])
def api_detail_passenger(request, name):
	try:
		passenger_detail = Passenger.objects.get(name=name)	
	except Passenger.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the passenger is not available
	
	if request.method == "GET":
		serialiser = PassengerSerializer(passenger_detail) # convert passenger into serializer
		return Response(serialiser.data)
# view all passengers
@api_view(['GET', ])
def api_all_passengers(request):
	passengers = Passenger.objects.all()
	serialiser = PassengerSerializer(passengers, many=True)
	return Response(serialiser.data)

#put as update
@api_view(['PUT', ])
def api_update_passenger(request, name):
	try:
		passenger_detail = Passenger.objects.get(name=name)	
	except Passenger.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the passenger is not available
	
	if request.method == "PUT":
		serialiser = PassengerSerializer(passenger_detail, data = request.data)
		data = {} # initialize data for JSON
		if serialiser.is_valid():
		 	serialiser.save()
		 	data["success"] = "update successful"
		 	return Response(data=data)
		 	# if not updated
		return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
# delete passenger
@api_view(['DELETE', ])
def api_delete_passenger(request, name):
	try:
		passenger_detail = Passenger.objects.get(name=name)	
	except Passenger.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the passenger is not available
	
	if request.method == "DELETE":
		operation = passenger_detail.delete()
		data = {} # initialize data for JSON
		if operation:

		 	data["success"] = "deleted successful"
		else:

		 	data["failure"] = "delete failed"
		return Response(data=data)


@api_view(['POST'])
def api_create_passenger(request):
	if request.method == "POST":
		serialiser = PassengerSerializer(data=request.data)
		if serialiser.is_valid():
			serialiser.save()
			return Response(serialiser.data, status=status.HTTP_201_CREATED)
		return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


# these are the methods for Drivers' account.
@api_view(['POST'])
def api_create_driver(request):
	if request.method == "POST":
		serialiser = DriverSerializer(data=request.data)
		if serialiser.is_valid():
			serialiser.save()
			return Response(serialiser.data, status=status.HTTP_201_CREATED)
		return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)


#update the Driver
@api_view(['PUT', ])
def api_update_driver(request, name):
	try:
		driver_detail = Driver.objects.get(name=name)	
	except Driver.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the driver is not available
	
	if request.method == "PUT":
		serialiser = DriverSerializer(driver_detail, data = request.data)
		data = {} # initialize data for JSON
		if serialiser.is_valid():
		 	serialiser.save()
		 	data["success"] = "Driver is successful updated"
		 	return Response(data=data)
		 	# if not updated
		return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

# view all Drivers
@api_view(['GET', ])
def api_all_driver(request):
	drivers = Driver.objects.all()
	serialiser = DriverSerializer(drivers, many=True)
	return Response(serialiser.data)

# view one Driver
@api_view(['GET', ])
def api_detail_driver(request, name):
	try:
		driver_detail = Driver.objects.get(name=name)	
	except Driver.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the driver is not available
	
	if request.method == "GET":
		serialiser = DriverSerializer(driver_detail) # convert driver model into serializer
		return Response(serialiser.data)


#delete Driver
@api_view(['DELETE', ])
def api_delete_driver(request, name):
	try:
		driver_detail = Driver.objects.get(name=name)	
	except Driver.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the driver is not available
	
	if request.method == "DELETE":
		operation = driver_detail.delete()
		data = {} # initialize data for JSON
		if operation:

		 	data["success"] = "Driver is successful deleted"
		else:

		 	data["failure"] = "delete failed"
		return Response(data=data)


#create bus
@api_view(['POST'])
def api_create_driver(request,name):

	try:
		driver_detail = Driver.objects.get(name = name)
	except Driver.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND) # if the driver is not available


	if request.method == "POST" and driver_detail.is_valid():

		serialiserDriver = BusSerializer(data=request.data)
		if serialiserDriver.is_valid():

			serialiserDriver.save()
			return Response(serialiser.data, status=status.HTTP_201_CREATED)
		return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)

"""
class ManagerView(viewsets.ModelViewSet):
	
	queryset         = Manager.objects.all()
	serializer_class = ManagerSerializer

class PassengerView(viewsets.ModelViewSet):
	queryset 		   = Passenger.objects.all()
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

