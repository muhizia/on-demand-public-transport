from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from WeGo.models import Passenger
from WeGo.api.serializer import PassengerSerializer


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
# delete
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