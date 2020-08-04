from django.db import models



class Passenger(models.Model):
    names     = models.CharField(max_length=25, blank=True, null=True, unique=True)
    telephone = models.CharField(max_length=13, null=False, unique=True, primary_key=True)
    password  = models.CharField(max_length=25, unique=True)
   

    def __str__(self):
        self.telephone

class Session_levels(models.Model):
    session_id  = models.TextField(primary_key=True)
    telephone = models.CharField(max_length=25, null=False)
    level       = models.IntegerField(null=True, default=0)

    def __str__(self):
        self.telephone

class UssdRideRequest(models.Model):
    pickupTime          = models.DateTimeField(blank=True, null = True, default=None)
    departureCity       = models.CharField(max_length=255, blank=True)
    destinationCity     = models.CharField(max_length=255, blank=True)
    numberOfSeets       = models.PositiveIntegerField(null=True, default=1)
    disabledPoeple      = models.PositiveIntegerField(null=True, default=0)
    passengers          = models.ManyToManyField(Passenger, blank = True) 

  
