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
	"""
	def create_profile(sender, **kwargs):
		user = kwargs["instance"]
		if kwargs["created"]:
			employee_profile = Employee(user=user)
			employee_profile.save()
	post_save.connect(create_profile, sender=User)
	"""

	def __str__(self):
		return self.profile.user.first_name

#class Customer(Person):
	"""
	Model to represent users
	"""

