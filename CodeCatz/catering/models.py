from django.db import models

#Create your models here.

class TotalEvent(models.Model):
    CustomerID = models.CharField(max_length=30)
    eventID = models.CharField(max_length=100)
    eventPlace = models.CharField(max_length=100)
    eventStartTime = models.TimeField(auto_now=False)
    eventDate = models.DateField(auto_now=False)
    Guests=models.IntegerField(null= False , default=10)