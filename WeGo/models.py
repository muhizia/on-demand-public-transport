from django.db import models
from location_field.models.plain import PlainLocationField
from authentication.views import User





# class for Passengers' account
class Manager(models.Model):
    
    firstName       = models.CharField(max_length=100,null=True, blank=True)
    lastName        = models.CharField(max_length=100,null=True, blank=True)
    telephone       = models.CharField(max_length=11)
    address         = models.CharField (max_length= 100,blank=True)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True)
    roles           = models.CharField(default="manager",max_length= 50)
    # this method is used as toString for java.
    def __str__(self):
        return  self.firstName+' '+ lastName

  
    

# class for Passengers' account
class Passenger(models.Model):
    
    firstName       = models.CharField(max_length=100,null=True, blank=True)
    lastName        = models.CharField(max_length=100,null=True, blank=True)
    telephone       = models.CharField(max_length=11, blank=True)
    address         = models.CharField (max_length= 100,blank=True, null=True)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True)
    roles            = models.CharField(default="passenger", max_length= 50)
    # this method is used as toString for java.
    def __str__(self):
        return self.firstName +' '+ self.lastName

    

# class for Driver account
class Driver(models.Model):
    firstName       = models.CharField(max_length=100)
    lastName        = models.CharField(max_length=100)
    telephone       = models.CharField(max_length=11)
    address         = models.CharField (max_length= 100,blank=True)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True)
    roles           = models.CharField(default="driver",max_length=50)
    
    
    def __str__(self):
        return self.firstName +' '+ self.lastName

    # this method remove the space after the name
    


#oneToMany relationship with Drivers
class Bus(models.Model):
    CATEGORY    = (('True','True'),('False','False'))
    id          = models.AutoField(primary_key = True)
    plateNumber = models.CharField(unique=True, max_length=11)
    available   = models.BooleanField(choices=CATEGORY)
    issuingDate = models.DateTimeField(blank=True, null=True, default=None)
    driver      = models.ForeignKey(Driver, on_delete= models.CASCADE)

    def __str__(self):
        return self.plateNumber

    # this method remove the space after the name
    def clean(self):
        if self.plateNumber:
            self.plateNumber = self.plateNumber.strip()

# class for route
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

#class for Zone that are located on route
class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    routes = models.ForeignKey(Route, on_delete=models.CASCADE)
    zoneName = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.zoneName
    
    class Meta:
        unique_together =(("routes", "zoneName"),)

# Bus stop located in a specific zone
class BusStop(models.Model):
    id = models.AutoField(primary_key=True)
    zones = models.ForeignKey(Zone, on_delete=models.CASCADE)
    busStopName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.busStopName

    class Meta:
        unique_together = (("zones", "busStopName"),) 

        
# class for requesting a ride
class RideRequest(models.Model):
    pickupTime          = models.DateTimeField(blank=True, null = True, default=None)
    departureCity       = models.CharField(max_length=255, blank=True)
    departureLocation   = PlainLocationField(based_fields=['departureCity'], zoom=13,null=True, blank=True)
    destinationCity     = models.CharField(max_length=255, blank=True)
    destinationLocation = PlainLocationField(based_fields=['destinationCity'], zoom=13, null=True, blank=True)
    numberOfSeets       = models.PositiveIntegerField(null=True)
    disabledPoeple      = models.PositiveIntegerField(null=True)
    passengers          = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True) 


