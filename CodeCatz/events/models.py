from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

from menu.models import Menu

class Event(models.Model):
    	
	EVENT_TYPE = (
		('Wedding', 'Wedding'),
		('Corporate', 'Corporate'),
		('Private','Private'),
		('Social', 'Social'),
		('Bar', 'Bar'),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event_type = models.CharField(max_length=50, choices=EVENT_TYPE, blank=True, default='Social', help_text='Event type.')
	numGuests = models.IntegerField('Number of Guests', help_text="Enter the number of guests.")
	date = models.DateField(default = datetime.datetime.today,help_text="Enter date of event.")
	startTime = models.TimeField(default=datetime.datetime.now, help_text="Specify start time of event.")
	endDate = models.DateField(default = datetime.datetime.today, help_text="If event goes into next day, please edit.")
	endTime = models.TimeField(default = datetime.time(22, 00), help_text="Enter end time.")
	location = models.CharField(max_length=255, help_text="Enter location")
	menu = models.ForeignKey(Menu, null=True, blank=True, help_text="Choose a menu")
	# menu = models.ManyToManyField()
	EVENT_STATUS = (
		('p', 'Pending'),
		('n', 'Notified'),
		('w', 'WorkingOn'),
		('c', 'Complete'),
	)

	status = models.CharField(max_length=1, choices=EVENT_STATUS, blank=True, default='p',
		help_text='Event Status')

	def __str__(self):
		return "%s, %s guests" % (self.user, self.numGuests)

	def get_absolute_url(self):
		return reverse('events')

