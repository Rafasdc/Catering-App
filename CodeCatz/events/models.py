from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

	eventID = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	numGuests = models.IntegerField()
	startTime = models.DateTimeField()
	# menu = models.ManyToManyField()

	def __str__(self):
		return self.user
