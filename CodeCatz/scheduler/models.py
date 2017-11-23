from django.db import models
from django.urls import reverse
from events.models import Event
from django.contrib.auth.models import User
import datetime
from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

class Notify(models.Model):
	"""
	notifies through email the necessary staff
	"""

	def sendEmail(emailto):
		from_email = settings.DEFAULT_FROM_EMAIL
		subject = 'Some subject'
		recipient_list = ['jasonsanche@gmail.com']
		EMAIL_MESSAGE = {
			'Pending': 'A new event has been requested. Please review and approve',
			'Approved': 'Your requested event with Cats Catering has been approved',
		}
		html_message = '<h1>This is my HTML test</h1>'
		res = send_mail(subject, EMAIL_MESSAGE['Pending'], from_email, emailto,
		 fail_silently=False, html_message=html_message)
		return HttpResponse('%s'%res)

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





