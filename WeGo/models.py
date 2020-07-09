from django.db import models

class Passenger(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique= True)
    telephone = models.CharField(max_length=11)
    address = models.CharField (max_length= 100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return  self.name

    def clean(self):
    	if self.name:
    		self.name = self.name.strip()
