from django.db import models
from django.urls import reverse
from events.models import Event

class Schedule(Event):
	"""
	a list of events in chronological order
	"""
	def __str__(self):
		return self.name


class Occurrence(models.Model):
	"""
	model extends events.Event representing the state of an event
	"""

	# event = models.OneToOneField(Event,on_delete=models.CASCADE)

  # def get_absolute_url(self):
  #   """
  #   Returns the url to access a particular event occurrance.
  #   """
  #   return reverse('event-detail', args=[str(self.id)])

	def __str__(self):
		return self.name

	# class Meta:
	# 	ordering = ["date"]


class ScheduleManager(models.Model):
	"""
	manages the logic for tagging and notifications
	"""


class Notify(models.Model):
	"""
	notifies through email the necessary staff
	"""





