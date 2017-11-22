from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.
class Person(models.Model):
	"""
	Model for all employees (and customers?)
	"""
	name = models.CharField(max_length=50, help_text="Enter name", blank=False)
	address = models.CharField(max_length=200, help_text="Enter address", blank=False)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(help_text="Enter phone number",validators=[phone_regex], max_length=15, blank=False) # validators should be a list

	class Meta:
		abstract = True


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

class Employee(Person):
	"""
	Model to represent an employee
	"""
	role = models.ManyToManyField(Role,blank=True)
	event = models.ManyToManyField(Event, help_text="Assign employee to event",blank=True)

	def __str__(self):
		return self.name


class Customer(Person):
	"""
	Model to represent users
	"""
