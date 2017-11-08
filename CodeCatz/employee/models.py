from django.db import models

# Create your models here.
class Person(models.Model):
	"""
	Model for all employees (and customers?)
	"""

	name = models.CharField(max_length=50, help_text="Enter name")
	address = models.CharField(max_length=200, help_text="Enter address")
	phone = models.IntegerField()


class Role(models.Model):
	"""
	Model for an employee role
	"""
	ROLE_CHOICES = (
		('COOK', 'Cook'),
		('WAITER', 'Waiter'),
		('DELIVERY', 'Delivery'),
	)

	role = models.CharField(max_length=50, help_text="Enter an employee role", choices=ROLE_CHOICES)

	def __str__(self):
		return self.name

class Employee(models.Model):
	"""
	Model to represent an employee
	"""
	contact = models.ForeignKey(Person, on_delete=models.CASCADE)
	expertise = models.ManyToManyField(Role, help_text="Assign role to employee")
	"""event = models.OneToOne(Event, help_text="Assign to an event")"""

