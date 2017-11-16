from django.db import models
from django.urls import reverse

class Schedule(models.Model):
	"""
	a list of events in chronological order
	"""
	def __str__(self):
		return self.name


class Occurrence(models.Model):
	"""
	model representing the state of an event
	"""

#	occurrance = models.OneToOneField(events.Event,on_delete=models.CASCADE,primary_key=True,)

	EVENT_STATUS = (
		('p', 'Pending'),
		('n', 'Notified'),
		('w', 'WorkingOn'),
		('c', 'Complete'),
	)

	status = models.CharField(max_length=1, choices=EVENT_STATUS, blank=True, default='p',
		help_text='Event Status')

  # def get_absolute_url(self):
  #   """
  #   Returns the url to access a particular event occurrance.
  #   """
  #   return reverse('event-detail', args=[str(self.id)])

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["occurrence__date"]


class ScheduleManager(models.Model):
	"""
	manages the logic for tagging and notifications
	"""


class Notify(models.Model):
	"""
	notifies through email the necessary staff
	"""





