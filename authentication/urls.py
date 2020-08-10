from django.urls import path,include
from .views import UserViewSet


urlpatterns = [
	path('register/',UserViewSet, name="register"),
]