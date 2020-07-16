from django.db import models



# class for Passengers' account
class Manager(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique= True)
    telephone = models.CharField(max_length=11)
    address = models.CharField (max_length= 100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length= 10)

    # this method is used as toString for java.
    def __str__(self):
        return  self.name

    def clean(self):
    	if self.name:
    		self.name = self.name.strip()

# class for Passengers' account
class Passenger(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique= True)
    telephone = models.CharField(max_length=11)
    address = models.CharField (max_length= 100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length= 10)

    # this method is used as toString for java.
    def __str__(self):
        return  self.name

    def clean(self):
    	if self.name:
    		self.name = self.name.strip()

# class for Driver account
class Driver(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(unique=True, max_length=100)
    telephone = models.CharField(max_length= 11)
    address = models.CharField (max_length= 100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length= 10)

    def __str__(self):
        return self.name

    # this method remove the space after the name
    def clean(self):
        if self.name:
            self.name = self.name.strip()


#oneToMany relationship
class Bus(models.Model):
    CATEGORY = (('True','True'),('False','False'))
    id = models.AutoField(primary_key = True)
    plateNumber = models.CharField(unique=True, max_length=11)
    available = models.BooleanField(choices=CATEGORY)
    issuingDate = models.DateTimeField(blank=True, null=True, default=None)
    driver = models.ForeignKey(Driver, on_delete= models.CASCADE)

    def __str__(self):
        return self.plateNumber

    # this method remove the space after the name
    def clean(self):
        if self.plateNumber:
            self.plateNumber = self.plateNumber.strip()


class RideRequest(models.Model):
    pickupTime = models.DateTimeField(blank=True, null = True, default=None)
    departureCity = models.CharField(max_length=255)
    destinationCity = models.CharField(max_length=255)
    passengers = models.ManyToManyField(Passenger, blank = True) 



    


