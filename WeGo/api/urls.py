from django.urls import path,include
from WeGo.api.view import PassengerView, DriverView, BusView,ManagerView, RideRequestView
from rest_framework import routers # this help us to have single url but with many actions

router = routers.DefaultRouter()
router.register('passengers', PassengerView)
router.register('drivers', DriverView)
router.register('buses', BusView)
router.register('Manager', ManagerView)
router.register('RideRequest',RideRequestView)


app_name = 'WeGo'

urlpatterns = [
	path('',include(router.urls))
	
]