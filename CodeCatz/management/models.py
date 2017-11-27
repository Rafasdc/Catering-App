from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from register.models import *
import datetime
import decimal

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
	hours = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
	payment = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default = 0.00)

	def calculate_hours_worked(self):
		hours_worked_dec = 0
		for events_worked in self.event.all():
			time_start = datetime.datetime.combine(events_worked.date, events_worked.startTime)
			time_end = datetime.datetime.combine(events_worked.endDate, events_worked.endTime)
			hours_worked = time_end - time_start
			hours_worked_dec += hours_worked.total_seconds() / 3600
		self.hours = round(hours_worked_dec, 2)
		self.save()
			
	def calculate_payment(self):
		payment = decimal.Decimal(self.hours) * self.wage_hour
		self.payment = round(payment, 2)
		self.save()


	def __str__(self):
		return self.profile.user.first_name

#class Customer(Person):
	"""
	Model to represent users
	"""

