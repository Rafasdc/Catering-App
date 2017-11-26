from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from register.models import *

# Create your models here.



class Role(models.Model):
	"""
	Model for an employee role
	"""
	NONE = 'NONE'
	COOK = 'COOOK'
	WAITER = 'WAITER'
	DELIVERY = 'DELIVERY'
	ROLE_CHOICES = (
		(COOK, 'COOK'),
		(WAITER, 'WAITER'),
		(DELIVERY, 'DELIVERY'),
	)

	role = models.CharField(max_length=15, help_text="Choose role", choices=ROLE_CHOICES, unique=True, null=True)

	def __str__(self):
		return self.role

class Employee(models.Model):
	"""
	Model to represent an employee
	"""
	profile = models.OneToOneField(UserProfile)
	event = models.ManyToManyField(Event, help_text="Assign employee to event",blank=True)
	wage_hour = models.DecimalField(max_digits=4, decimal_places=2, blank=False, default=15.30)

	def __str__(self):
		return self.profile.user.first_name

#class Customer(Person):
	"""
	Model to represent users
	"""

