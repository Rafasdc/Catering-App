from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	numGuests = models.IntegerField('Number of Guests')
	startTime = models.TimeField(null=True, blank=True)
	date = models.DateField(null=True, blank=True)
	location = models.CharField(null=True, blank=True, max_length=255)
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
		return reverse('event-detail', args=[str(self.eventID)])
