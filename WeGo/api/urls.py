from django.urls import path,include
from WeGo.api.view import (PassengerView, 
DriverView, BusView,ManagerView, RideRequestView, BusStopView,RouteView)
from authentication.views import UserViewSet, login_request
from rest_framework import routers # this help us to have single url but with many actions

router = routers.DefaultRouter()
router.register('passengers', PassengerView)
router.register('drivers', DriverView)
router.register('buses', BusView)
router.register('Manager', ManagerView)
router.register('RideRequest',RideRequestView)
router.register('busstop',BusStopView)
router.register('routes',RouteView)

router.register('users', UserViewSet)


app_name = 'WeGo'

urlpatterns = [
	path('',include(router.urls)),
	path("login", login_request, name="login"),
]