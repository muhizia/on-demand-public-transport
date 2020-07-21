from django.db import models
from location_field.models.plain import PlainLocationField



# class for Passengers' account
class Manager(models.Model):
    id              = models.AutoField(primary_key = True)
    firstName       = models.CharField(max_length=100,null=True, blank=True)
    lastName        = models.CharField(max_length=100,null=True, blank=True)
    userName        = models.CharField(max_length=100, unique= True)
    telephone       = models.CharField(max_length=11)
    address         = models.CharField (max_length= 100,blank=True)
    email           = models.EmailField(max_length=100,unique= True,null=True, blank=True)
    password        = models.CharField(max_length= 10)
    passwordConfirm = models.CharField(max_length=10)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True)
    # this method is used as toString for java.
    def __str__(self):
        return  self.name

    def clean(self):
    	if self.name:
    		self.name = self.name.strip()
    

# class for Passengers' account
class Passenger(models.Model):
    id              = models.AutoField(primary_key = True)
    firstName       = models.CharField(max_length=100,null=True, blank=True)
    lastName        = models.CharField(max_length=100,null=True, blank=True)
    userName        = models.CharField(max_length=100, unique= True)
    telephone       = models.CharField(max_length=11)
    address         = models.CharField (max_length= 100,blank=True)
    email           = models.EmailField(max_length=100,unique= True,null=True, blank=True)
    password        = models.CharField(max_length= 10)
    passwordConfirm = models.CharField(max_length=10)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True)
    # this method is used as toString for java.
    def __str__(self):
        return self.firstName +' '+ self.lastName

    

# class for Driver account
class Driver(models.Model):
    id              = models.AutoField(primary_key = True)
    firstName       = models.CharField(max_length=100)
    lastName        = models.CharField(max_length=100)
    userName        = models.CharField(max_length=100, unique= True)
    telephone       = models.CharField(max_length=11)
    address         = models.CharField (max_length= 100,blank=True)
    email           = models.EmailField(max_length=100,unique= True)
    password        = models.CharField(max_length= 10)
    passwordConfirm = models.CharField(max_length=10)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True)
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

# class for requesting a ride
class RideRequest(models.Model):
    pickupTime          = models.DateTimeField(blank=True, null = True, default=None)
    departureCity       = models.CharField(max_length=255)
    departureLocation   = PlainLocationField(based_fields=['departureCity'], zoom=2)
    destinationCity     = models.CharField(max_length=255)
    destinationLocation = PlainLocationField(based_fields=['destinationCity'], zoom=2)
    numberOfSeets       = models.PositiveIntegerField(null=False)
    disabledPoeple      = models.PositiveIntegerField(null=True)
    passengers          = models.ManyToManyField(Passenger, blank = True) 
