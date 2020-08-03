from django.urls import path
from . import views

app_name = 'ondemandUssd'

urlpatterns = [
    path('',views.home, name='home'),
]